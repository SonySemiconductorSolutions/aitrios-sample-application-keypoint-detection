"""
Copyright 2023 Sony Semiconductor Solutions Corp. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import yaml
from threading import Event
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO

from console_access_api.aitrios_console import AitriosConsole
from console_access_api.utils import Utils
from .pipeline.pipeline import DataPipeline

# Load Console access settings
with open(os.path.join(os.getcwd(), "src", "config", "console_access_settings.yaml")) as file:
    yaml_load = yaml.safe_load(file)
    BASE_URL = yaml_load["console_access_settings"]["console_endpoint"]
    CLIENT_ID = yaml_load["console_access_settings"]["client_id"]
    CLIENT_SECRET = yaml_load["console_access_settings"]["client_secret"]
    GCS_OKTA_DOMAIN = yaml_load["console_access_settings"]["portal_authorization_endpoint"]

# Init Instances
console_access_api = AitriosConsole(BASE_URL, CLIENT_ID, CLIENT_SECRET, GCS_OKTA_DOMAIN)
data_pipeline = DataPipeline(sender_queue_size=5)

# Flask app configuration
app = Flask(__name__)
CORS(app)
app.config["SECRET_KEY"] = "your-secret-key"
socketio = SocketIO(app, cors_allowed_origins="*", async_mode=None)

# Socket emitting flag
started = Event()


@app.route("/devices", methods=["GET"])
def get_devices():
    """
    Get the list of devices.

    This endpoint retrieves the list of available devices through the console access API.

    Returns:
        tuple: A tuple containing a JSON response and an HTTP status code.
            - If devices are retrieved successfully:
                JSON response containing the list of devices.
            - If an error occurs:
                JSON response indicating an internal server error.
    """
    try:
        response = console_access_api.GetDevices()

        if "result" in response and response["result"] == "ERROR":
            return jsonify(response), 500

        devices = {"devices": []}
        for device in response["devices"]:
            devices["devices"].append(device["device_id"])

        return jsonify(devices), 200

    except Exception as error:
        error_message = {"result": "ERROR", "message": str(error)}
        return jsonify(error_message), 500


@app.route("/devices/<string:device_id>/models", methods=["GET"])
def get_models(device_id):
    """
    Get the list of models for a specific device.

    This endpoint retrieves the list of models associated with a specific device through the
    console access API.

    Args:
        device_id (str): The ID of the device for which to retrieve models.

    Returns:
        tuple: A tuple containing a JSON response and an HTTP status code.
            - If models are retrieved successfully:
                JSON response containing the list of models for the specified device.
            - If an error occurs:
                JSON response indicating an internal server error.
    """
    try:
        if device_id == "":
            error_response = {
                "result": "ERROR",
                "message": "Device ID is not specified.",
            }
            return jsonify(error_response), 400

        response = console_access_api.GetDevices()

        if "result" in response and response["result"] == "ERROR":
            return jsonify(response), 500

        models = {"models": []}
        for device in response["devices"]:
            if device["device_id"] == device_id:
                model_dict_list = device["models"]
                for model_dict in model_dict_list:
                    models["models"].append(model_dict["model_version_id"].split(":")[0])

        return jsonify(models), 200

    except Exception as error:
        error_message = {"result": "ERROR", "message": str(error)}
        return jsonify(error_message), 500


@app.route("/devices/<string:device_id>/command_parameter_file", methods=["GET"])
def get_command_parameter_file(device_id):
    """
    Get the command parameter file for a specific device.

    This endpoint retrieves the command parameter file associated with a specific device
    through the console access API.

    Args:
        device_id (str): The ID of the device for which to retrieve the command parameter file.

    Returns:
        tuple: A tuple containing a JSON response and an HTTP status code.
            - If the command parameter file is retrieved successfully:
                JSON response containing the command parameter file information.
            - If the device ID is not specified or the command parameter file is not found:
                JSON response indicating an error.
            - If an error occurs:
                JSON response indicating an internal server error.
    """
    try:
        if device_id == "":
            error_response = {
                "result": "ERROR",
                "message": "Device ID is not specified.",
            }
            return jsonify(error_response), 400

        response = console_access_api.GetCommandParameterFile()

        if "result" in response and response["result"] == "ERROR":
            return jsonify(response), 500

        file_name = ""
        param_list = response["parameter_list"]

        """
        Obtain a list of devices to which the CommandParameterFile is bound
        with the key "device_ids" and search for the device ID of the request.

        "parameter_list": [
          { ...,
            "device_ids": [
              "sid-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            ],
          },
          ...
        ]
        """
        for param in param_list:
            device_ids = param["device_ids"]
            if device_id in device_ids:
                file_name = param["file_name"]
                command_parameter = param["parameter"]
                break

        if file_name == "":
            error_response = {
                "result": "ERROR",
                "message": "Command Parameter File is not bound to the specified device.",
            }
            return jsonify(error_response), 400

        command_parameter_file = {
            "file_name": file_name,
            "command_parameter": command_parameter,
        }

        return jsonify(command_parameter_file), 200

    except Exception as error:
        error_message = {"result": "ERROR", "message": str(error)}
        return jsonify(error_message), 500


@app.route("/command_parameter_file/<string:file_name>", methods=["PUT"])
def update_command_parameter_file(file_name):
    """
    Update the command parameter file.

    This endpoint allows updating the content of the command parameter file identified by its name.

    Args:
        file_name (str): The name of the command parameter file to be updated.

    Returns:
        tuple: A tuple containing a JSON response and an HTTP status code.
            - If the command parameter file is updated successfully:
                JSON response indicating the result of the update.
            - If the command parameter or file name is not specified:
                JSON response indicating an error.
            - If an error occurs:
                JSON response indicating an internal server error.
    """
    try:
        request_param = request.get_json()
        command_parameter = Utils.Base64EncodedStr(request_param["command_param"])

        if command_parameter == "" or file_name == "":
            error_response = {
                "result": "ERROR",
                "message": "Command Parameter or file name not specified.",
            }
            return jsonify(error_response), 400

        payload = {"parameter": command_parameter}

        response = console_access_api.UpdateCommandParameterFile(
            file_name=file_name, payload=payload
        )

        if "result" in response and response["result"] == "ERROR":
            return jsonify(response), 500

        return jsonify(response), 200

    except Exception as error:
        error_message = {"result": "ERROR", "message": str(error)}
        return jsonify(error_message), 500


@app.route("/devices/<string:device_id>/start_processing", methods=["POST"])
def start_processing(device_id):
    """
    Start processing for the specified device.

    This endpoint allows the initiation of a processing task for a specific device.

    Args:
        device_id (str): The ID of the device to start processing for.

    Returns:
        dict: A JSON response indicating the status of the request.
            - If processing starts successfully:
                {"message": "Inference started."}
            - If an error occurs:
                {"message": "Internal server error"}
    """
    if device_id == "":
        error_response = {
            "result": "ERROR",
            "message": "Device ID is not specified.",
        }
        return jsonify(error_response), 400

    loader_param = {"device_id": device_id}

    try:
        response = console_access_api.StartUploadInferenceResult(device_id=device_id)

        if "result" in response and response["result"] == "ERROR":
            return jsonify(response), 500

        data_pipeline.start_processing(loader_param)

        started.set()
        return {"message": "Inference started."}, 200
    except Exception:
        return {"message": "Internal server error"}, 500


@app.route("/devices/<string:device_id>/stop_processing", methods=["POST"])
def stop_processing(device_id):
    """
    Stop processing for the specified device.

    This endpoint allows the termination of a processing task for a specific device.

    Args:
        device_id (str): The ID of the device to stop processing for.

    Returns:
        dict: A JSON response indicating the status of the request.
            - If processing stops successfully:
                {"message": "Inference stopped"}
            - If an error occurs:
                {"message": "Internal server error"}
    """
    try:
        started.clear()

        response = console_access_api.StopUploadInferenceResult(device_id=device_id)

        if "result" in response and response["result"] == "ERROR":
            return jsonify(response), 500

        data_pipeline.stop_processing()
        return {"message": "Inference stopped"}, 200
    except Exception:
        return {"message": "Internal server error"}, 500


def sender_thread():
    """
    Sender thread for emitting processed data over Socket.IO.

    This function is responsible for sending processed data to connected clients using Socket.IO.

    Notes:
        - This function assumes the existence of a `data_pipeline` object.
        - It relies on a `sender_queue` which should be provided by `data_pipeline.get_sender_queue
        - It emits data under the event name "processed_data".

    Important:
        - This function runs indefinitely and should be executed in a separate thread.

    Returns:
        None
    """
    sender_queue = data_pipeline.get_sender_queue()
    while True:
        started.wait()
        if len(sender_queue) > 0:
            processed_data = sender_queue.popleft()
            socketio.emit("processed_data", processed_data)


socketio.start_background_task(sender_thread)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
