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

from .data_loader_base_class import DataLoaderBase
from console_access_api.aitrios_console import AitriosConsole


class ConsoleDataLoader(DataLoaderBase):
    def __init__(self):
        with open(
            os.path.join(
                os.path.dirname(__file__), "..", "..", "config", "console_access_settings.yaml"
            )
        ) as file:
            yaml_load = yaml.safe_load(file)
            BASE_URL = yaml_load["console_access_settings"]["console_endpoint"]
            CLIENT_ID = yaml_load["console_access_settings"]["client_id"]
            CLIENT_SECRET = yaml_load["console_access_settings"]["client_secret"]
            GCS_OKTA_DOMAIN = yaml_load["console_access_settings"]["portal_authorization_endpoint"]

        self.console_access_api = AitriosConsole(
            BASE_URL, CLIENT_ID, CLIENT_SECRET, GCS_OKTA_DOMAIN
        )

    def get_metadata(self, config=None):
        device_id = config["device_id"]

        try:
            response = self.console_access_api.GetInferenceResults(
                device_id=device_id, NumberOfInferenceresults=1, raw=1
            )

            timestamp = response[0]["inference_result"]["Inferences"][0]["T"]
            inference_data = response[0]["inference_result"]["Inferences"][0]["O"]

            timestamp_and_inference = {"timestamp": timestamp, "inference_data": inference_data}

            return timestamp_and_inference
        except Exception as e:
            print("Exception: " + e)
