import requests
import json
from .utils import Utils


class AitriosConsole:
    def __init__(self, baseURL, client_id, client_secret, gcs_okta_domain):
        # Project information

        self.BASE_URL = baseURL
        CLIENT_ID = client_id
        CLIENT_SECRET = client_secret
        self.GCS_OKTA_DOMAIN = gcs_okta_domain
        self.AUTHORIZATION_CODE = Utils.Base64EncodedStr(CLIENT_ID + ":" + CLIENT_SECRET)

    ##########################################################################
    # Low Level APIs
    ##########################################################################
    def GetToken(self):
        headers = {
            "accept": "application/json",
            "authorization": "Basic " + self.AUTHORIZATION_CODE,
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded",
        }

        data = {
            "grant_type": "client_credentials",
            "scope": "system",
        }

        response = requests.post(
            url=self.GCS_OKTA_DOMAIN,
            data=data,
            headers=headers,
        )
        analysis_info = json.loads(response.text)
        token = analysis_info["access_token"]
        return token

    def GetHeaders(self, payload):
        token = self.GetToken()
        headers = {"Accept": "application/json", "Authorization": "Bearer " + token}
        if payload != {}:
            headers.setdefault("Content-Type", "application/json")
        return headers

    def Request(self, url, method, **kwargs):
        params = {}
        payload = {}
        files = {}
        url = self.BASE_URL + url

        # set parameters
        for key, val in kwargs.items():
            if val != None:
                if key == "payload":
                    # payload
                    payload = json.dumps(val)
                elif key == "files":
                    # multipart/form-data
                    files = val
                else:
                    # check parameters
                    if "{" + key + "}" in url:
                        # path parameter
                        url = url.replace("{" + key + "}", val)
                    else:
                        # query parameter
                        params.setdefault(key, str(val))

        # create header
        headers = self.GetHeaders(payload=payload)

        # call request
        try:
            response = requests.request(
                method=method, url=url, headers=headers, params=params, data=payload, files=files
            )
            analysis_info = json.loads(response.text)
        except Exception as e:
            return response.text
        return analysis_info

    ##################################################################
    # Generated APIs from resources/openapi.json
    # python src/GenetateAitriosApi.py > api.txt
    ##################################################################

    ##################################################################
    #
    # GetQrCodeForProvisioning
    #   tag     : 'Provisioning'
    #   url     : '/provisioning/qrcode'
    #   method  : 'GET'
    #   params  : 'ntp' in query (required)
    #           : 'auto' in query
    #           : 'wifi_ssid' in query
    #           : 'wifi_pass' in query
    #           : 'proxy_url' in query
    #           : 'proxy_port' in query
    #           : 'proxy_user_name' in query
    #           : 'proxy_pass' in query
    #           : 'ip_address' in query
    #           : 'subnet_mask' in query
    #           : 'gateway' in query
    #           : 'dns' in query
    #   payload :
    ##################################################################
    def GetQrCodeForProvisioning(
        self,
        ntp,
        auto=None,
        wifi_ssid=None,
        wifi_pass=None,
        proxy_url=None,
        proxy_port=None,
        proxy_user_name=None,
        proxy_pass=None,
        ip_address=None,
        subnet_mask=None,
        gateway=None,
        dns=None,
    ):
        ret = self.Request(
            url="/provisioning/qrcode",
            method="GET",
            ntp=ntp,
            auto=auto,
            wifi_ssid=wifi_ssid,
            wifi_pass=wifi_pass,
            proxy_url=proxy_url,
            proxy_port=proxy_port,
            proxy_user_name=proxy_user_name,
            proxy_pass=proxy_pass,
            ip_address=ip_address,
            subnet_mask=subnet_mask,
            gateway=gateway,
            dns=dns,
        )
        return ret

    ##################################################################
    #
    # EnrollDevice
    #   tag     : 'Certificate'
    #   url     : '/devices'
    #   method  : 'POST'
    #   params  :
    #   payload : {
    #           :    "device_name" : string, (required)
    #           :    "device_type" : string, (required)
    #           :    "primary_certificate" : string, (required)
    #           : }
    #
    ##################################################################
    def EnrollDevice(self, payload):
        ret = self.Request(url="/devices", method="POST", payload=payload)
        return ret

    ##################################################################
    #
    # GetDevices
    #   tag     : 'Manage Devices'
    #   url     : '/devices'
    #   method  : 'GET'
    #   params  : 'connectionState' in query
    #           : 'device_name' in query
    #           : 'device_id' in query
    #           : 'device_group_id' in query
    #   payload :
    ##################################################################
    def GetDevices(
        self, connectionState=None, device_name=None, device_id=None, device_group_id=None
    ):
        ret = self.Request(
            url="/devices",
            method="GET",
            connectionState=connectionState,
            device_name=device_name,
            device_id=device_id,
            device_group_id=device_group_id,
        )
        return ret

    ##################################################################
    #
    # GetDevice
    #   tag     : 'Manage Devices'
    #   url     : '/devices/{device_id}'
    #   method  : 'GET'
    #   params  : 'device_id' in path (required)
    #   payload :
    ##################################################################
    def GetDevice(self, device_id):
        ret = self.Request(url="/devices/{device_id}", method="GET", device_id=device_id)
        return ret

    ##################################################################
    #
    # DeleteDevice
    #   tag     : 'Certificate'
    #   url     : '/devices/{device_id}'
    #   method  : 'DELETE'
    #   params  : 'device_id' in path (required)
    #   payload :
    ##################################################################
    def DeleteDevice(self, device_id):
        ret = self.Request(url="/devices/{device_id}", method="DELETE", device_id=device_id)
        return ret

    ##################################################################
    #
    # GetDeviceCertificates
    #   tag     : 'Certificate'
    #   url     : '/certificate/devices'
    #   method  : 'GET'
    #   params  :
    #   payload :
    ##################################################################
    def GetDeviceCertificates(self):
        ret = self.Request(url="/certificate/devices", method="GET")
        return ret

    ##################################################################
    #
    # GetDeviceCertificate
    #   tag     : 'Certificate'
    #   url     : '/certificate/devices/{device_id}'
    #   method  : 'GET'
    #   params  : 'device_id' in path (required)
    #   payload :
    ##################################################################
    def GetDeviceCertificate(self, device_id):
        ret = self.Request(
            url="/certificate/devices/{device_id}", method="GET", device_id=device_id
        )
        return ret

    ##################################################################
    #
    # UpdateDeviceCertificate
    #   tag     : 'Certificate'
    #   url     : '/certificate/devices/{device_id}'
    #   method  : 'PUT'
    #   params  : 'device_id' in path (required)
    #   payload : {
    #           :    "primary_certificate" : string, (required)
    #           : }
    #
    ##################################################################
    def UpdateDeviceCertificate(self, device_id, payload):
        ret = self.Request(
            url="/certificate/devices/{device_id}",
            method="PUT",
            device_id=device_id,
            payload=payload,
        )
        return ret

    ##################################################################
    #
    # StartUploadInferenceResult
    #   tag     : 'Device Command'
    #   url     : '/devices/{device_id}/inferenceresults/collectstart'
    #   method  : 'POST'
    #   params  : 'device_id' in path (required)
    #   payload :
    ##################################################################
    def StartUploadInferenceResult(self, device_id):
        ret = self.Request(
            url="/devices/{device_id}/inferenceresults/collectstart",
            method="POST",
            device_id=device_id,
        )
        return ret

    ##################################################################
    #
    # StopUploadInferenceResult
    #   tag     : 'Device Command'
    #   url     : '/devices/{device_id}/inferenceresults/collectstop'
    #   method  : 'POST'
    #   params  : 'device_id' in path (required)
    #   payload :
    ##################################################################
    def StopUploadInferenceResult(self, device_id):
        ret = self.Request(
            url="/devices/{device_id}/inferenceresults/collectstop",
            method="POST",
            device_id=device_id,
        )
        return ret

    ##################################################################
    #
    # Reboot
    #   tag     : 'Device Command'
    #   url     : '/devices/{device_id}/reboot'
    #   method  : 'POST'
    #   params  : 'device_id' in path (required)
    #   payload :
    ##################################################################
    def Reboot(self, device_id):
        ret = self.Request(url="/devices/{device_id}/reboot", method="POST", device_id=device_id)
        return ret

    ##################################################################
    #
    # ResetDevice
    #   tag     : 'Device Command'
    #   url     : '/devices/{device_id}/reset'
    #   method  : 'POST'
    #   params  : 'device_id' in path (required)
    #   payload :
    ##################################################################
    def ResetDevice(self, device_id):
        ret = self.Request(url="/devices/{device_id}/reset", method="POST", device_id=device_id)
        return ret

    ##################################################################
    #
    # SetDeviceLog
    #   tag     : 'Device Command'
    #   url     : '/devices/{device_id}/configuration/logdestination'
    #   method  : 'PUT'
    #   params  : 'device_id' in path (required)
    #           : 'level' in query
    #           : 'destination' in query
    #           : 'SensorRegister' in query
    #   payload :
    ##################################################################
    def SetDeviceLog(self, device_id, level=None, destination=None, SensorRegister=None):
        ret = self.Request(
            url="/devices/{device_id}/configuration/logdestination",
            method="PUT",
            device_id=device_id,
            level=level,
            destination=destination,
            SensorRegister=SensorRegister,
        )
        return ret

    ##################################################################
    #
    # GetDirectImage
    #   tag     : 'Device Command'
    #   url     : '/devices/{device_id}/images/latest'
    #   method  : 'GET'
    #   params  : 'device_id' in path (required)
    #   payload :
    ##################################################################
    def GetDirectImage(self, device_id):
        ret = self.Request(
            url="/devices/{device_id}/images/latest", method="GET", device_id=device_id
        )
        return ret

    ##################################################################
    #
    # ChangePassword
    #   tag     : 'Device Command'
    #   url     : '/devices/{device_id}/password'
    #   method  : 'PATCH'
    #   params  : 'device_id' in path (required)
    #   payload : {
    #           :    "password" : string, (required)
    #           : }
    #
    ##################################################################
    def ChangePassword(self, device_id, payload):
        ret = self.Request(
            url="/devices/{device_id}/password",
            method="PATCH",
            device_id=device_id,
            payload=payload,
        )
        return ret

    ##################################################################
    #
    # GetCommandParameterFile
    #   tag     : 'Command Parameter File'
    #   url     : '/command_parameter_files'
    #   method  : 'GET'
    #   params  :
    #   payload :
    ##################################################################
    def GetCommandParameterFile(self):
        ret = self.Request(url="/command_parameter_files", method="GET")
        return ret

    ##################################################################
    #
    # RegistCommandParameterFile
    #   tag     : 'Command Parameter File'
    #   url     : '/command_parameter_files'
    #   method  : 'POST'
    #   params  :
    #   payload : {
    #           :    "file_name" : string, (required)
    #           :    "parameter" : string, (required)
    #           :    "comment" : string
    #           : }
    #
    ##################################################################
    def RegistCommandParameterFile(self, payload):
        ret = self.Request(url="/command_parameter_files", method="POST", payload=payload)
        return ret

    ##################################################################
    #
    # UpdateCommandParameterFile
    #   tag     : 'Command Parameter File'
    #   url     : '/command_parameter_files/{file_name}'
    #   method  : 'PATCH'
    #   params  : 'file_name' in path (required)
    #   payload : {
    #           :    "parameter" : string, (required)
    #           :    "comment" : string
    #           : }
    #
    ##################################################################
    def UpdateCommandParameterFile(self, file_name, payload):
        ret = self.Request(
            url="/command_parameter_files/{file_name}",
            method="PATCH",
            file_name=file_name,
            payload=payload,
        )
        return ret

    ##################################################################
    #
    # DeleteCommandParameterFile
    #   tag     : 'Command Parameter File'
    #   url     : '/command_parameter_files/{file_name}'
    #   method  : 'DELETE'
    #   params  : 'file_name' in path (required)
    #   payload :
    ##################################################################
    def DeleteCommandParameterFile(self, file_name):
        ret = self.Request(
            url="/command_parameter_files/{file_name}", method="DELETE", file_name=file_name
        )
        return ret

    ##################################################################
    #
    # ExportCommandParameterFile
    #   tag     : 'Command Parameter File'
    #   url     : '/command_parameter_files/{file_name}/export'
    #   method  : 'GET'
    #   params  : 'file_name' in path (required)
    #   payload :
    ##################################################################
    def ExportCommandParameterFile(self, file_name):
        ret = self.Request(
            url="/command_parameter_files/{file_name}/export", method="GET", file_name=file_name
        )
        return ret

    ##################################################################
    #
    # SetDefaultCommandParameterFile
    #   tag     : 'Command Parameter File'
    #   url     : '/command_parameter_files/{file_name}/default'
    #   method  : 'PATCH'
    #   params  : 'file_name' in path (required)
    #   payload :
    ##################################################################
    def SetDefaultCommandParameterFile(self, file_name):
        ret = self.Request(
            url="/command_parameter_files/{file_name}/default", method="PATCH", file_name=file_name
        )
        return ret

    ##################################################################
    #
    # ApplyCommandParameterFileToDevice
    #   tag     : 'Command Parameter File'
    #   url     : '/devices/configuration/command_parameter_files/{file_name}'
    #   method  : 'PUT'
    #   params  : 'file_name' in path (required)
    #   payload : {
    #           :    "device_ids" : string, (required)
    #           : }
    #
    ##################################################################
    def ApplyCommandParameterFileToDevice(self, file_name, payload):
        ret = self.Request(
            url="/devices/configuration/command_parameter_files/{file_name}",
            method="PUT",
            file_name=file_name,
            payload=payload,
        )
        return ret

    ##################################################################
    #
    # CancelCommandParameterFile
    #   tag     : 'Command Parameter File'
    #   url     : '/devices/configuration/command_parameter_files/{file_name}'
    #   method  : 'DELETE'
    #   params  : 'file_name' in path (required)
    #   payload : {
    #           :    "device_ids" : string, (required)
    #           : }
    #
    ##################################################################
    def CancelCommandParameterFile(self, file_name, payload):
        ret = self.Request(
            url="/devices/configuration/command_parameter_files/{file_name}",
            method="DELETE",
            file_name=file_name,
            payload=payload,
        )
        return ret

    ##################################################################
    #
    # SetPermission
    #   tag     : 'Manage Devices'
    #   url     : '/devices/{device_id}/configuration/permission'
    #   method  : 'PUT'
    #   params  : 'device_id' in path (required)
    #           : 'factory_reset' in query (required)
    #   payload :
    ##################################################################
    def SetPermission(self, device_id, factory_reset):
        ret = self.Request(
            url="/devices/{device_id}/configuration/permission",
            method="PUT",
            device_id=device_id,
            factory_reset=factory_reset,
        )
        return ret

    ##################################################################
    #
    # GetDeployConfigurations
    #   tag     : 'Deploy'
    #   url     : '/deployconfigurations'
    #   method  : 'GET'
    #   params  :
    #   payload :
    ##################################################################
    def GetDeployConfigurations(self):
        ret = self.Request(url="/deployconfigurations", method="GET")
        return ret

    ##################################################################
    #
    # CreateDeployConfiguration
    #   tag     : 'Deploy'
    #   url     : '/deployconfigurations'
    #   method  : 'POST'
    #   params  : 'config_id' in query (required)
    #           : 'comment' in query
    #           : 'sensor_loader_version_number' in query
    #           : 'sensor_version_number' in query
    #           : 'model_id' in query
    #           : 'model_version_number' in query
    #           : 'ap_fw_version_number' in query
    #   payload :
    ##################################################################
    def CreateDeployConfiguration(
        self,
        config_id,
        comment=None,
        sensor_loader_version_number=None,
        sensor_version_number=None,
        model_id=None,
        model_version_number=None,
        ap_fw_version_number=None,
    ):
        ret = self.Request(
            url="/deployconfigurations",
            method="POST",
            config_id=config_id,
            comment=comment,
            sensor_loader_version_number=sensor_loader_version_number,
            sensor_version_number=sensor_version_number,
            model_id=model_id,
            model_version_number=model_version_number,
            ap_fw_version_number=ap_fw_version_number,
        )
        return ret

    ##################################################################
    #
    # GetDeployConfiguration
    #   tag     : 'Deploy'
    #   url     : '/deployconfigurations/{config_id}'
    #   method  : 'GET'
    #   params  : 'config_id' in path (required)
    #   payload :
    ##################################################################
    def GetDeployConfiguration(self, config_id):
        ret = self.Request(
            url="/deployconfigurations/{config_id}", method="GET", config_id=config_id
        )
        return ret

    ##################################################################
    #
    # DeployByConfiguration
    #   tag     : 'Deploy'
    #   url     : '/deployconfigurations/{config_id}'
    #   method  : 'PUT'
    #   params  : 'config_id' in path (required)
    #           : 'device_ids' in query (required)
    #           : 'replace_model_id' in query
    #           : 'comment' in query
    #   payload :
    ##################################################################
    def DeployByConfiguration(self, config_id, device_ids, replace_model_id=None, comment=None):
        ret = self.Request(
            url="/deployconfigurations/{config_id}",
            method="PUT",
            config_id=config_id,
            device_ids=device_ids,
            replace_model_id=replace_model_id,
            comment=comment,
        )
        return ret

    ##################################################################
    #
    # DeleteDeployConfiguration
    #   tag     : 'Deploy'
    #   url     : '/deployconfigurations/{config_id}'
    #   method  : 'DELETE'
    #   params  : 'config_id' in path (required)
    #   payload :
    ##################################################################
    def DeleteDeployConfiguration(self, config_id):
        ret = self.Request(
            url="/deployconfigurations/{config_id}", method="DELETE", config_id=config_id
        )
        return ret

    ##################################################################
    #
    # CancelDeployment
    #   tag     : 'Deploy'
    #   url     : '/devices/{device_id}/deploys/{deploy_id}'
    #   method  : 'PUT'
    #   params  : 'device_id' in path (required)
    #           : 'deploy_id' in path (required)
    #   payload :
    ##################################################################
    def CancelDeployment(self, device_id, deploy_id):
        ret = self.Request(
            url="/devices/{device_id}/deploys/{deploy_id}",
            method="PUT",
            device_id=device_id,
            deploy_id=deploy_id,
        )
        return ret

    ##################################################################
    #
    # GetDeployHistory
    #   tag     : 'Deploy'
    #   url     : '/devices/{device_id}/deploys'
    #   method  : 'GET'
    #   params  : 'device_id' in path (required)
    #   payload :
    ##################################################################
    def GetDeployHistory(self, device_id):
        ret = self.Request(url="/devices/{device_id}/deploys", method="GET", device_id=device_id)
        return ret

    ##################################################################
    #
    # DeployDeviceModel
    #   tag     : 'Deploy'
    #   url     : '/models/{model_id}/devices/{device_id}/deploys'
    #   method  : 'PUT'
    #   params  : 'model_id' in path (required)
    #           : 'device_id' in path (required)
    #           : 'version_number' in query
    #           : 'replace_model_id' in query
    #           : 'comment' in query
    #   payload :
    ##################################################################
    def DeployDeviceModel(
        self, model_id, device_id, version_number=None, replace_model_id=None, comment=None
    ):
        ret = self.Request(
            url="/models/{model_id}/devices/{device_id}/deploys",
            method="PUT",
            model_id=model_id,
            device_id=device_id,
            version_number=version_number,
            replace_model_id=replace_model_id,
            comment=comment,
        )
        return ret

    ##################################################################
    #
    # GetDeviceGroups
    #   tag     : 'Manage Devices'
    #   url     : '/devicegroups'
    #   method  : 'GET'
    #   params  : 'device_group_id' in query
    #           : 'comment' in query
    #           : 'device_id' in query
    #   payload :
    ##################################################################
    def GetDeviceGroups(self, device_group_id=None, comment=None, device_id=None):
        ret = self.Request(
            url="/devicegroups",
            method="GET",
            device_group_id=device_group_id,
            comment=comment,
            device_id=device_id,
        )
        return ret

    ##################################################################
    #
    # CreateDeviceGroup
    #   tag     : 'Manage Devices'
    #   url     : '/devicegroups'
    #   method  : 'POST'
    #   params  : 'device_group_id' in query (required)
    #           : 'comment' in query
    #           : 'device_id' in query
    #           : 'del_from_dgroup' in query
    #   payload :
    ##################################################################
    def CreateDeviceGroup(
        self, device_group_id, comment=None, device_id=None, del_from_dgroup=None
    ):
        ret = self.Request(
            url="/devicegroups",
            method="POST",
            device_group_id=device_group_id,
            comment=comment,
            device_id=device_id,
            del_from_dgroup=del_from_dgroup,
        )
        return ret

    ##################################################################
    #
    # GetDeviceGroup
    #   tag     : 'Manage Devices'
    #   url     : '/devicegroups/{device_group_id}'
    #   method  : 'GET'
    #   params  : 'device_group_id' in path (required)
    #   payload :
    ##################################################################
    def GetDeviceGroup(self, device_group_id):
        ret = self.Request(
            url="/devicegroups/{device_group_id}", method="GET", device_group_id=device_group_id
        )
        return ret

    ##################################################################
    #
    # DeleteDeviceGroup
    #   tag     : 'Manage Devices'
    #   url     : '/devicegroups/{device_group_id}'
    #   method  : 'DELETE'
    #   params  : 'device_group_id' in path (required)
    #   payload :
    ##################################################################
    def DeleteDeviceGroup(self, device_group_id):
        ret = self.Request(
            url="/devicegroups/{device_group_id}", method="DELETE", device_group_id=device_group_id
        )
        return ret

    ##################################################################
    #
    # UpdateDeviceGroup
    #   tag     : 'Manage Devices'
    #   url     : '/devicegroups/{device_group_id}'
    #   method  : 'PATCH'
    #   params  : 'device_group_id' in path (required)
    #           : 'comment' in query
    #           : 'device_id' in query
    #           : 'del_from_dgroup' in query
    #   payload :
    ##################################################################
    def UpdateDeviceGroup(
        self, device_group_id, comment=None, device_id=None, del_from_dgroup=None
    ):
        ret = self.Request(
            url="/devicegroups/{device_group_id}",
            method="PATCH",
            device_group_id=device_group_id,
            comment=comment,
            device_id=device_id,
            del_from_dgroup=del_from_dgroup,
        )
        return ret

    ##################################################################
    #
    # GetTrainingKits
    #   tag     : 'Train Model'
    #   url     : '/models/training_kits'
    #   method  : 'GET'
    #   params  : 'training_kit_type' in query
    #           : 'order_by' in query
    #   payload :
    ##################################################################
    def GetTrainingKits(self, training_kit_type=None, order_by=None):
        ret = self.Request(
            url="/models/training_kits",
            method="GET",
            training_kit_type=training_kit_type,
            order_by=order_by,
        )
        return ret

    ##################################################################
    #
    # GetTrainingKit
    #   tag     : 'Train Model'
    #   url     : '/models/training_kits/{training_kit_id}'
    #   method  : 'GET'
    #   params  : 'training_kit_id' in path (required)
    #   payload :
    ##################################################################
    def GetTrainingKit(self, training_kit_id):
        ret = self.Request(
            url="/models/training_kits/{training_kit_id}",
            method="GET",
            training_kit_id=training_kit_id,
        )
        return ret

    ##################################################################
    #
    # GetProjects
    #   tag     : 'Train Model'
    #   url     : '/model_projects'
    #   method  : 'GET'
    #   params  : 'project_name' in query
    #           : 'model_platform' in query
    #           : 'project_type' in query
    #           : 'device_id' in query
    #           : 'include_training_flg' in query
    #   payload :
    ##################################################################
    def GetProjects(
        self,
        project_name=None,
        model_platform=None,
        project_type=None,
        device_id=None,
        include_training_flg=None,
    ):
        ret = self.Request(
            url="/model_projects",
            method="GET",
            project_name=project_name,
            model_platform=model_platform,
            project_type=project_type,
            device_id=device_id,
            include_training_flg=include_training_flg,
        )
        return ret

    ##################################################################
    #
    # CreateBaseProject
    #   tag     : 'Train Model'
    #   url     : '/model_projects/base'
    #   method  : 'POST'
    #   params  : 'project_name' in query (required)
    #           : 'training_kit' in query (required)
    #           : 'comment' in query
    #   payload :
    ##################################################################
    def CreateBaseProject(self, project_name, training_kit, comment=None):
        ret = self.Request(
            url="/model_projects/base",
            method="POST",
            project_name=project_name,
            training_kit=training_kit,
            comment=comment,
        )
        return ret

    ##################################################################
    #
    # CreateDeviceProject
    #   tag     : 'Train Model'
    #   url     : '/model_projects/device'
    #   method  : 'POST'
    #   params  : 'project_name' in query (required)
    #           : 'model_id' in query (required)
    #           : 'device_id' in query (required)
    #           : 'version_number' in query
    #           : 'comment' in query
    #   payload :
    ##################################################################
    def CreateDeviceProject(
        self, project_name, model_id, device_id, version_number=None, comment=None
    ):
        ret = self.Request(
            url="/model_projects/device",
            method="POST",
            project_name=project_name,
            model_id=model_id,
            device_id=device_id,
            version_number=version_number,
            comment=comment,
        )
        return ret

    ##################################################################
    #
    # GetProject
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_name}'
    #   method  : 'GET'
    #   params  : 'project_name' in path (required)
    #           : 'include_training_flg' in query
    #   payload :
    ##################################################################
    def GetProject(self, project_name, include_training_flg=None):
        ret = self.Request(
            url="/model_projects/{project_name}",
            method="GET",
            project_name=project_name,
            include_training_flg=include_training_flg,
        )
        return ret

    ##################################################################
    #
    # DeleteProject
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_name}'
    #   method  : 'DELETE'
    #   params  : 'project_name' in path (required)
    #   payload :
    ##################################################################
    def DeleteProject(self, project_name):
        ret = self.Request(
            url="/model_projects/{project_name}", method="DELETE", project_name=project_name
        )
        return ret

    ##################################################################
    #
    # SaveModel
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_name}/save'
    #   method  : 'POST'
    #   params  : 'project_name' in path (required)
    #           : 'model_id' in query
    #           : 'initial_version_number' in query
    #           : 'functionality' in query
    #           : 'vendor_name' in query
    #           : 'comment' in query
    #   payload :
    ##################################################################
    def SaveModel(
        self,
        project_name,
        model_id=None,
        initial_version_number=None,
        functionality=None,
        vendor_name=None,
        comment=None,
    ):
        ret = self.Request(
            url="/model_projects/{project_name}/save",
            method="POST",
            project_name=project_name,
            model_id=model_id,
            initial_version_number=initial_version_number,
            functionality=functionality,
            vendor_name=vendor_name,
            comment=comment,
        )
        return ret

    ##################################################################
    #
    # GetRelearnStatus
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_name}/relearn'
    #   method  : 'GET'
    #   params  : 'project_name' in path (required)
    #   payload :
    ##################################################################
    def GetRelearnStatus(self, project_name):
        ret = self.Request(
            url="/model_projects/{project_name}/relearn", method="GET", project_name=project_name
        )
        return ret

    ##################################################################
    #
    # Relearn
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_name}/relearn'
    #   method  : 'POST'
    #   params  : 'project_name' in path (required)
    #           : 'training_type' in query
    #           : 'reserved_budget_in_hours' in query
    #           : 'epochs' in query
    #   payload :
    ##################################################################
    def Relearn(
        self, project_name, training_type=None, reserved_budget_in_hours=None, epochs=None
    ):
        ret = self.Request(
            url="/model_projects/{project_name}/relearn",
            method="POST",
            project_name=project_name,
            training_type=training_type,
            reserved_budget_in_hours=reserved_budget_in_hours,
            epochs=epochs,
        )
        return ret

    ##################################################################
    #
    # CancelRelearn
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_name}/relearn'
    #   method  : 'DELETE'
    #   params  : 'project_name' in path (required)
    #   payload :
    ##################################################################
    def CancelRelearn(self, project_name):
        ret = self.Request(
            url="/model_projects/{project_name}/relearn",
            method="DELETE",
            project_name=project_name,
        )
        return ret

    ##################################################################
    #
    # ImportImagesFromFiles
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_name}/images/files'
    #   method  : 'POST'
    #   params  : 'project_name' in path (required)
    #   payload : {
    #           :    "images" : array, (required)
    #           :    "tags_name" : array
    #           : }
    #
    ##################################################################
    def ImportImagesFromFiles(self, project_name, payload):
        ret = self.Request(
            url="/model_projects/{project_name}/images/files",
            method="POST",
            project_name=project_name,
            payload=payload,
        )
        return ret

    ##################################################################
    #
    # ImportImagesFromScblob
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_name}/images/scbloburls'
    #   method  : 'POST'
    #   params  : 'project_name' in path (required)
    #   payload : {
    #           :    "container_url" : string, (required)
    #           :    "tags_name" : array
    #           : }
    #
    ##################################################################
    def ImportImagesFromScblob(self, project_name, payload):
        ret = self.Request(
            url="/model_projects/{project_name}/images/scbloburls",
            method="POST",
            project_name=project_name,
            payload=payload,
        )
        return ret

    ##################################################################
    #
    # GetProjectIterations
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_id}/iterations'
    #   method  : 'GET'
    #   params  : 'project_id' in path (required)
    #           : 'overlap_threshold' in query
    #           : 'threshold' in query
    #   payload :
    ##################################################################
    def GetProjectIterations(self, project_id, overlap_threshold=None, threshold=None):
        ret = self.Request(
            url="/model_projects/{project_id}/iterations",
            method="GET",
            project_id=project_id,
            overlap_threshold=overlap_threshold,
            threshold=threshold,
        )
        return ret

    ##################################################################
    #
    # GetProjectImages
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_id}/images'
    #   method  : 'GET'
    #   params  : 'project_id' in path (required)
    #           : 'iteration_id' in query
    #           : 'order_by' in query
    #           : 'number_of_images' in query
    #           : 'skip' in query
    #           : 'image_size_type' in query
    #   payload :
    ##################################################################
    def GetProjectImages(
        self,
        project_id,
        iteration_id=None,
        order_by=None,
        number_of_images=None,
        skip=None,
        image_size_type=None,
    ):
        ret = self.Request(
            url="/model_projects/{project_id}/images",
            method="GET",
            project_id=project_id,
            iteration_id=iteration_id,
            order_by=order_by,
            number_of_images=number_of_images,
            skip=skip,
            image_size_type=image_size_type,
        )
        return ret

    ##################################################################
    #
    # DeleteProjectImages
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_id}/images'
    #   method  : 'DELETE'
    #   params  : 'project_id' in path (required)
    #           : 'image_ids' in query (required)
    #   payload :
    ##################################################################
    def DeleteProjectImages(self, project_id, image_ids):
        ret = self.Request(
            url="/model_projects/{project_id}/images",
            method="DELETE",
            project_id=project_id,
            image_ids=image_ids,
        )
        return ret

    ##################################################################
    #
    # GetProjectImagesById
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_id}/images/id'
    #   method  : 'GET'
    #   params  : 'project_id' in path (required)
    #           : 'image_ids' in query (required)
    #           : 'iteration_id' in query
    #           : 'image_size_type' in query
    #   payload :
    ##################################################################
    def GetProjectImagesById(self, project_id, image_ids, iteration_id=None, image_size_type=None):
        ret = self.Request(
            url="/model_projects/{project_id}/images/id",
            method="GET",
            project_id=project_id,
            image_ids=image_ids,
            iteration_id=iteration_id,
            image_size_type=image_size_type,
        )
        return ret

    ##################################################################
    #
    # GetImageRegionProposals
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_id}/images/{image_id}/regionproposals'
    #   method  : 'GET'
    #   params  : 'project_id' in path (required)
    #           : 'image_id' in path (required)
    #   payload :
    ##################################################################
    def GetImageRegionProposals(self, project_id, image_id):
        ret = self.Request(
            url="/model_projects/{project_id}/images/{image_id}/regionproposals",
            method="GET",
            project_id=project_id,
            image_id=image_id,
        )
        return ret

    ##################################################################
    #
    # CreateProjectImageRegions
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_id}/images/regions'
    #   method  : 'POST'
    #   params  : 'project_id' in path (required)
    #   payload : {
    #           :    "regions" : array
    #           : }
    #
    ##################################################################
    def CreateProjectImageRegions(self, project_id, payload):
        ret = self.Request(
            url="/model_projects/{project_id}/images/regions",
            method="POST",
            project_id=project_id,
            payload=payload,
        )
        return ret

    ##################################################################
    #
    # UpdateProjectImageRegions
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_id}/images/regions'
    #   method  : 'PATCH'
    #   params  : 'project_id' in path (required)
    #   payload : {
    #           :    "regions" : array
    #           : }
    #
    ##################################################################
    def UpdateProjectImageRegions(self, project_id, payload):
        ret = self.Request(
            url="/model_projects/{project_id}/images/regions",
            method="PATCH",
            project_id=project_id,
            payload=payload,
        )
        return ret

    ##################################################################
    #
    # DeleteProjectImageRegions
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_id}/images/regions/{region_id}'
    #   method  : 'DELETE'
    #   params  : 'project_id' in path (required)
    #           : 'region_id' in path (required)
    #   payload :
    ##################################################################
    def DeleteProjectImageRegions(self, project_id, region_id):
        ret = self.Request(
            url="/model_projects/{project_id}/images/regions/{region_id}",
            method="DELETE",
            project_id=project_id,
            region_id=region_id,
        )
        return ret

    ##################################################################
    #
    # GetProjectTags
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_id}/tags'
    #   method  : 'GET'
    #   params  : 'project_id' in path (required)
    #           : 'iteration_id' in query
    #           : 'order_by' in query
    #   payload :
    ##################################################################
    def GetProjectTags(self, project_id, iteration_id=None, order_by=None):
        ret = self.Request(
            url="/model_projects/{project_id}/tags",
            method="GET",
            project_id=project_id,
            iteration_id=iteration_id,
            order_by=order_by,
        )
        return ret

    ##################################################################
    #
    # CreateProjectTag
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_id}/tags'
    #   method  : 'POST'
    #   params  : 'project_id' in path (required)
    #           : 'tag_name' in query (required)
    #           : 'description' in query
    #   payload :
    ##################################################################
    def CreateProjectTag(self, project_id, tag_name, description=None):
        ret = self.Request(
            url="/model_projects/{project_id}/tags",
            method="POST",
            project_id=project_id,
            tag_name=tag_name,
            description=description,
        )
        return ret

    ##################################################################
    #
    # DeleteProjectTag
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_id}/tags/{tag_id}'
    #   method  : 'DELETE'
    #   params  : 'project_id' in path (required)
    #           : 'tag_id' in path (required)
    #   payload :
    ##################################################################
    def DeleteProjectTag(self, project_id, tag_id):
        ret = self.Request(
            url="/model_projects/{project_id}/tags/{tag_id}",
            method="DELETE",
            project_id=project_id,
            tag_id=tag_id,
        )
        return ret

    ##################################################################
    #
    # UpdateProjectTag
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_id}/tags/{tag_id}'
    #   method  : 'PATCH'
    #   params  : 'project_id' in path (required)
    #           : 'tag_id' in path (required)
    #   payload : {
    #           :    "name" : string, (required)
    #           :    "description" : string
    #           :    "type" : string, (required)
    #           : }
    #
    ##################################################################
    def UpdateProjectTag(self, project_id, tag_id, payload):
        ret = self.Request(
            url="/model_projects/{project_id}/tags/{tag_id}",
            method="PATCH",
            project_id=project_id,
            tag_id=tag_id,
            payload=payload,
        )
        return ret

    ##################################################################
    #
    # GetProjectTaggedImages
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_id}/tags/tagged_images'
    #   method  : 'GET'
    #   params  : 'project_id' in path (required)
    #           : 'tag_ids' in query
    #           : 'iteration_id' in query
    #           : 'number_of_images' in query
    #           : 'skip' in query
    #           : 'order_by' in query
    #           : 'image_size_type' in query
    #   payload :
    ##################################################################
    def GetProjectTaggedImages(
        self,
        project_id,
        tag_ids=None,
        iteration_id=None,
        number_of_images=None,
        skip=None,
        order_by=None,
        image_size_type=None,
    ):
        ret = self.Request(
            url="/model_projects/{project_id}/tags/tagged_images",
            method="GET",
            project_id=project_id,
            tag_ids=tag_ids,
            iteration_id=iteration_id,
            number_of_images=number_of_images,
            skip=skip,
            order_by=order_by,
            image_size_type=image_size_type,
        )
        return ret

    ##################################################################
    #
    # GetProjectUntaggedImages
    #   tag     : 'Train Model'
    #   url     : '/model_projects/{project_id}/tags/untagged_images'
    #   method  : 'GET'
    #   params  : 'project_id' in path (required)
    #           : 'iteration_id' in query
    #           : 'number_of_images' in query
    #           : 'skip' in query
    #           : 'order_by' in query
    #           : 'image_size_type' in query
    #   payload :
    ##################################################################
    def GetProjectUntaggedImages(
        self,
        project_id,
        iteration_id=None,
        number_of_images=None,
        skip=None,
        order_by=None,
        image_size_type=None,
    ):
        ret = self.Request(
            url="/model_projects/{project_id}/tags/untagged_images",
            method="GET",
            project_id=project_id,
            iteration_id=iteration_id,
            number_of_images=number_of_images,
            skip=skip,
            order_by=order_by,
            image_size_type=image_size_type,
        )
        return ret

    ##################################################################
    #
    # GetModels
    #   tag     : 'Train Model'
    #   url     : '/models'
    #   method  : 'GET'
    #   params  : 'model_id' in query
    #           : 'comment' in query
    #           : 'project_name' in query
    #           : 'model_platform' in query
    #           : 'project_type' in query
    #           : 'device_id' in query
    #           : 'latest_type' in query
    #   payload :
    ##################################################################
    def GetModels(
        self,
        model_id=None,
        comment=None,
        project_name=None,
        model_platform=None,
        project_type=None,
        device_id=None,
        latest_type=None,
    ):
        ret = self.Request(
            url="/models",
            method="GET",
            model_id=model_id,
            comment=comment,
            project_name=project_name,
            model_platform=model_platform,
            project_type=project_type,
            device_id=device_id,
            latest_type=latest_type,
        )
        return ret

    ##################################################################
    #
    # ImportBaseModel
    #   tag     : 'Train Model'
    #   url     : '/models'
    #   method  : 'POST'
    #   params  :
    #   payload : {
    #           :    "model_id" : string, (required)
    #           :    "model" : string, (required)
    #           :    "converted" : boolean
    #           :    "vendor_name" : string
    #           :    "comment" : string
    #           :    "input_format_param" : string
    #           :    "network_config" : string
    #           :    "network_type" : string
    #           : }
    #
    ##################################################################
    def ImportBaseModel(self, payload):
        ret = self.Request(url="/models", method="POST", payload=payload)
        return ret

    ##################################################################
    #
    # PublishModel
    #   tag     : 'Train Model'
    #   url     : '/models/{model_id}'
    #   method  : 'POST'
    #   params  : 'model_id' in path (required)
    #           : 'device_id' in query
    #   payload :
    ##################################################################
    def PublishModel(self, model_id, device_id=None):
        ret = self.Request(
            url="/models/{model_id}", method="POST", model_id=model_id, device_id=device_id
        )
        return ret

    ##################################################################
    #
    # DeleteModel
    #   tag     : 'Train Model'
    #   url     : '/models/{model_id}'
    #   method  : 'DELETE'
    #   params  : 'model_id' in path (required)
    #   payload :
    ##################################################################
    def DeleteModel(self, model_id):
        ret = self.Request(url="/models/{model_id}", method="DELETE", model_id=model_id)
        return ret

    ##################################################################
    #
    # UpdateModel
    #   tag     : 'Train Model'
    #   url     : '/models/{model_id}'
    #   method  : 'PATCH'
    #   params  : 'model_id' in path (required)
    #           : 'comment' in query
    #           : 'version_number' in query
    #   payload :
    ##################################################################
    def UpdateModel(self, model_id, comment=None, version_number=None):
        ret = self.Request(
            url="/models/{model_id}",
            method="PATCH",
            model_id=model_id,
            comment=comment,
            version_number=version_number,
        )
        return ret

    ##################################################################
    #
    # GetBaseModelStatus
    #   tag     : 'Train Model'
    #   url     : '/models/{model_id}/base'
    #   method  : 'GET'
    #   params  : 'model_id' in path (required)
    #           : 'latest_type' in query
    #   payload :
    ##################################################################
    def GetBaseModelStatus(self, model_id, latest_type=None):
        ret = self.Request(
            url="/models/{model_id}/base", method="GET", model_id=model_id, latest_type=latest_type
        )
        return ret

    ##################################################################
    #
    # GetBaseModelVersions
    #   tag     : 'Train Model'
    #   url     : '/models/{model_id}/base/versions'
    #   method  : 'GET'
    #   params  : 'model_id' in path (required)
    #           : 'version_number' in query
    #   payload :
    ##################################################################
    def GetBaseModelVersions(self, model_id, version_number=None):
        ret = self.Request(
            url="/models/{model_id}/base/versions",
            method="GET",
            model_id=model_id,
            version_number=version_number,
        )
        return ret

    ##################################################################
    #
    # UpdateBaseModelVersion
    #   tag     : 'Train Model'
    #   url     : '/models/{model_id}/base/versions/{version_number}'
    #   method  : 'PATCH'
    #   params  : 'model_id' in path (required)
    #           : 'version_number' in path (required)
    #   payload : {
    #           :    "comment" : string
    #           :    "input_format_param" : string
    #           :    "network_config" : string
    #           : }
    #
    ##################################################################
    def UpdateBaseModelVersion(self, model_id, version_number, payload):
        ret = self.Request(
            url="/models/{model_id}/base/versions/{version_number}",
            method="PATCH",
            model_id=model_id,
            version_number=version_number,
            payload=payload,
        )
        return ret

    ##################################################################
    #
    # GetDeviceModelStatus
    #   tag     : 'Train Model'
    #   url     : '/models/{model_id}/devices/{device_id}'
    #   method  : 'GET'
    #   params  : 'model_id' in path (required)
    #           : 'device_id' in path (required)
    #           : 'latest_type' in query
    #   payload :
    ##################################################################
    def GetDeviceModelStatus(self, model_id, device_id, latest_type=None):
        ret = self.Request(
            url="/models/{model_id}/devices/{device_id}",
            method="GET",
            model_id=model_id,
            device_id=device_id,
            latest_type=latest_type,
        )
        return ret

    ##################################################################
    #
    # GetDeviceModelVersions
    #   tag     : 'Train Model'
    #   url     : '/models/{model_id}/devices/{device_id}/versions'
    #   method  : 'GET'
    #   params  : 'model_id' in path (required)
    #           : 'device_id' in path (required)
    #           : 'version_number' in query
    #   payload :
    ##################################################################
    def GetDeviceModelVersions(self, model_id, device_id, version_number=None):
        ret = self.Request(
            url="/models/{model_id}/devices/{device_id}/versions",
            method="GET",
            model_id=model_id,
            device_id=device_id,
            version_number=version_number,
        )
        return ret

    ##################################################################
    #
    # UpdateDeviceModelVersion
    #   tag     : 'Train Model'
    #   url     : '/models/{model_id}/devices/{device_id}/versions/{version_number}'
    #   method  : 'PATCH'
    #   params  : 'model_id' in path (required)
    #           : 'device_id' in path (required)
    #           : 'version_number' in path (required)
    #   payload : {
    #           :    "comment" : string, (required)
    #           : }
    #
    ##################################################################
    def UpdateDeviceModelVersion(self, model_id, device_id, version_number, payload):
        ret = self.Request(
            url="/models/{model_id}/devices/{device_id}/versions/{version_number}",
            method="PATCH",
            model_id=model_id,
            device_id=device_id,
            version_number=version_number,
            payload=payload,
        )
        return ret

    ##################################################################
    #
    # GetFirmwares
    #   tag     : 'Firmware'
    #   url     : '/firmwares'
    #   method  : 'GET'
    #   params  : 'firmware_type' in query
    #   payload :
    ##################################################################
    def GetFirmwares(self, firmware_type=None):
        ret = self.Request(url="/firmwares", method="GET", firmware_type=firmware_type)
        return ret

    ##################################################################
    #
    # CreateFirmware
    #   tag     : 'Firmware'
    #   url     : '/firmwares'
    #   method  : 'POST'
    #   params  :
    #   payload : {
    #           :    "firmware_type" : string, (required)
    #           :    "version_number" : string, (required)
    #           :    "comment" : string
    #           :    "file_name" : string, (required)
    #           :    "file_content" : string, (required)
    #           : }
    #
    ##################################################################
    def CreateFirmware(self, payload):
        ret = self.Request(url="/firmwares", method="POST", payload=payload)
        return ret

    ##################################################################
    #
    # GetFirmware
    #   tag     : 'Firmware'
    #   url     : '/firmwares/{firmware_type}/{version_number}'
    #   method  : 'GET'
    #   params  : 'firmware_type' in path (required)
    #           : 'version_number' in path (required)
    #   payload :
    ##################################################################
    def GetFirmware(self, firmware_type, version_number):
        ret = self.Request(
            url="/firmwares/{firmware_type}/{version_number}",
            method="GET",
            firmware_type=firmware_type,
            version_number=version_number,
        )
        return ret

    ##################################################################
    #
    # DeleteFirmware
    #   tag     : 'Firmware'
    #   url     : '/firmwares/{firmware_type}/{version_number}'
    #   method  : 'DELETE'
    #   params  : 'firmware_type' in path (required)
    #           : 'version_number' in path (required)
    #   payload :
    ##################################################################
    def DeleteFirmware(self, firmware_type, version_number):
        ret = self.Request(
            url="/firmwares/{firmware_type}/{version_number}",
            method="DELETE",
            firmware_type=firmware_type,
            version_number=version_number,
        )
        return ret

    ##################################################################
    #
    # GetDeviceApps
    #   tag     : 'Device App'
    #   url     : '/device_apps'
    #   method  : 'GET'
    #   params  :
    #   payload :
    ##################################################################
    def GetDeviceApps(self):
        ret = self.Request(url="/device_apps", method="GET")
        return ret

    ##################################################################
    #
    # ImportDeviceApp
    #   tag     : 'Device App'
    #   url     : '/device_apps'
    #   method  : 'POST'
    #   params  :
    #   payload : {
    #           :    "compiled_flg" : string, (required)
    #           :    "entry_point" : string
    #           :    "app_name" : string, (required)
    #           :    "version_number" : string, (required)
    #           :    "comment" : string
    #           :    "file_name" : string, (required)
    #           :    "file_content" : string, (required)
    #           : }
    #
    ##################################################################
    def ImportDeviceApp(self, payload):
        ret = self.Request(url="/device_apps", method="POST", payload=payload)
        return ret

    ##################################################################
    #
    # GetDeviceApp
    #   tag     : 'Device App'
    #   url     : '/device_apps/{app_name}/{version_number}'
    #   method  : 'GET'
    #   params  : 'app_name' in path (required)
    #           : 'version_number' in path (required)
    #   payload :
    ##################################################################
    def GetDeviceApp(self, app_name, version_number):
        ret = self.Request(
            url="/device_apps/{app_name}/{version_number}",
            method="GET",
            app_name=app_name,
            version_number=version_number,
        )
        return ret

    ##################################################################
    #
    # DeleteDeviceApp
    #   tag     : 'Device App'
    #   url     : '/device_apps/{app_name}/{version_number}'
    #   method  : 'DELETE'
    #   params  : 'app_name' in path (required)
    #           : 'version_number' in path (required)
    #   payload :
    ##################################################################
    def DeleteDeviceApp(self, app_name, version_number):
        ret = self.Request(
            url="/device_apps/{app_name}/{version_number}",
            method="DELETE",
            app_name=app_name,
            version_number=version_number,
        )
        return ret

    ##################################################################
    #
    # ExportDeviceApp
    #   tag     : 'Device App'
    #   url     : '/device_apps/{app_name}/{version_number}/export'
    #   method  : 'GET'
    #   params  : 'app_name' in path (required)
    #           : 'version_number' in path (required)
    #   payload :
    ##################################################################
    def ExportDeviceApp(self, app_name, version_number):
        ret = self.Request(
            url="/device_apps/{app_name}/{version_number}/export",
            method="GET",
            app_name=app_name,
            version_number=version_number,
        )
        return ret

    ##################################################################
    #
    # GetDeviceAppDeploys
    #   tag     : 'Device App'
    #   url     : '/device_apps/{app_name}/{version_number}/deploys'
    #   method  : 'GET'
    #   params  : 'app_name' in path (required)
    #           : 'version_number' in path (required)
    #   payload :
    ##################################################################
    def GetDeviceAppDeploys(self, app_name, version_number):
        ret = self.Request(
            url="/device_apps/{app_name}/{version_number}/deploys",
            method="GET",
            app_name=app_name,
            version_number=version_number,
        )
        return ret

    ##################################################################
    #
    # GetAppDevices
    #   tag     : 'Device App'
    #   url     : '/device_apps/{app_name}/{version_number}/devices'
    #   method  : 'GET'
    #   params  : 'app_name' in path (required)
    #           : 'version_number' in path (required)
    #   payload :
    ##################################################################
    def GetAppDevices(self, app_name, version_number):
        ret = self.Request(
            url="/device_apps/{app_name}/{version_number}/devices",
            method="GET",
            app_name=app_name,
            version_number=version_number,
        )
        return ret

    ##################################################################
    #
    # DeployDeviceApp
    #   tag     : 'Device App'
    #   url     : '/device_apps_deploys'
    #   method  : 'POST'
    #   params  :
    #   payload : {
    #           :    "app_name" : string, (required)
    #           :    "version_number" : string, (required)
    #           :    "device_ids" : string, (required)
    #           :    "comment" : string
    #           : }
    #
    ##################################################################
    def DeployDeviceApp(self, payload):
        ret = self.Request(url="/device_apps_deploys", method="POST", payload=payload)
        return ret

    ##################################################################
    #
    # UndeployDeviceApp
    #   tag     : 'Device App'
    #   url     : '/device_apps_deploys'
    #   method  : 'DELETE'
    #   params  : 'device_ids' in query (required)
    #   payload :
    ##################################################################
    def UndeployDeviceApp(self, device_ids):
        ret = self.Request(url="/device_apps_deploys", method="DELETE", device_ids=device_ids)
        return ret

    ##################################################################
    #
    # ExportImages
    #   tag     : 'Insight'
    #   url     : '/devices/images/export'
    #   method  : 'GET'
    #   params  : 'key' in query (required)
    #           : 'from_datetime' in query
    #           : 'to_datetime' in query
    #           : 'device_id' in query
    #           : 'file_format' in query
    #   payload :
    ##################################################################
    def ExportImages(
        self, key, from_datetime=None, to_datetime=None, device_id=None, file_format=None
    ):
        ret = self.Request(
            url="/devices/images/export",
            method="GET",
            key=key,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            device_id=device_id,
            file_format=file_format,
        )
        return ret

    ##################################################################
    #
    # GetImageDirectories
    #   tag     : 'Insight'
    #   url     : '/devices/images/directories'
    #   method  : 'GET'
    #   params  : 'device_id' in query
    #   payload :
    ##################################################################
    def GetImageDirectories(self, device_id=None):
        ret = self.Request(url="/devices/images/directories", method="GET", device_id=device_id)
        return ret

    ##################################################################
    #
    # GetImages
    #   tag     : 'Insight'
    #   url     : '/devices/{device_id}/images/directories/{sub_directory_name}'
    #   method  : 'GET'
    #   params  : 'device_id' in path (required)
    #           : 'sub_directory_name' in path (required)
    #           : 'order_by' in query
    #           : 'number_of_images' in query
    #           : 'skip' in query
    #   payload :
    ##################################################################
    def GetImages(
        self, device_id, sub_directory_name, order_by=None, number_of_images=None, skip=None
    ):
        ret = self.Request(
            url="/devices/{device_id}/images/directories/{sub_directory_name}",
            method="GET",
            device_id=device_id,
            sub_directory_name=sub_directory_name,
            order_by=order_by,
            number_of_images=number_of_images,
            skip=skip,
        )
        return ret

    ##################################################################
    #
    # GetInferenceResult
    #   tag     : 'Insight'
    #   url     : '/devices/{device_id}/inferenceresults/{id}'
    #   method  : 'GET'
    #   params  : 'device_id' in path (required)
    #           : 'id' in path (required)
    #   payload :
    ##################################################################
    def GetInferenceResult(self, device_id, id):
        ret = self.Request(
            url="/devices/{device_id}/inferenceresults/{id}",
            method="GET",
            device_id=device_id,
            id=id,
        )
        return ret

    ##################################################################
    #
    # GetInferenceResults
    #   tag     : 'Insight'
    #   url     : '/devices/{device_id}/inferenceresults'
    #   method  : 'GET'
    #   params  : 'device_id' in path (required)
    #           : 'NumberOfInferenceresults' in query
    #           : 'filter' in query
    #           : 'raw' in query
    #           : 'time' in query
    #   payload :
    ##################################################################
    def GetInferenceResults(
        self, device_id, NumberOfInferenceresults=None, filter=None, raw=None, time=None
    ):
        ret = self.Request(
            url="/devices/{device_id}/inferenceresults",
            method="GET",
            device_id=device_id,
            NumberOfInferenceresults=NumberOfInferenceresults,
            filter=filter,
            raw=raw,
            time=time,
        )
        return ret

    ##################################################################
    #
    # UpdateIRHubConnector
    #   tag     : 'Connector'
    #   url     : '/connector/ir_hub'
    #   method  : 'PUT'
    #   params  :
    #   payload : {
    #           :    "url" : string
    #           :    "name" : string
    #           : }
    #
    ##################################################################
    def UpdateIRHubConnector(self, payload):
        ret = self.Request(url="/connector/ir_hub", method="PUT", payload=payload)
        return ret

    ##################################################################
    #
    # UpdateStorageConnector
    #   tag     : 'Connector'
    #   url     : '/connector/storage'
    #   method  : 'PUT'
    #   params  :
    #   payload : {
    #           :    "endpoint" : string
    #           :    "connection_string" : string
    #           :    "container_name" : string
    #           : }
    #
    ##################################################################
    def UpdateStorageConnector(self, payload):
        ret = self.Request(url="/connector/storage", method="PUT", payload=payload)
        return ret

    ##########################################################################
    # Other functions
    ##########################################################################
    def GetLatestImage(self, sub_directory_name, number_of_images):
        ret = self.Request(
            url="/devices/{device_id}/images/directories/{sub_directory_name}",
            method="GET",
            device_id=self.DEVICE_ID,
            sub_directory_name=sub_directory_name,
            order_by="desc",
            number_of_images=number_of_images,
        )
        return ret

    def GetLatestInferenceResult(self):
        ret = self.GetInferenceResult(device_id=self.DEVICE_ID, id=None)
        #        print('ret: ' + ret)
        id = ret[0]["id"]
        ret = self.GetInferenceResult(device_id=self.DEVICE_ID, id=id)
        return ret

    def GetDirectImageWithCrop(self, device_id, hoffset=0, voffset=0, hsize=4056, vsize=3040):
        ret = self.Request(
            url="/devices/{device_id}/images/latest",
            method="GET",
            device_id=device_id,
            CropHOffset=hoffset,
            CropVOffset=voffset,
            CropHSize=hsize,
            CropVSize=vsize,
        )
        return ret

    def GetInfo(self):
        print(
            "##############################################################################################################"
        )
        print("# openapi file name  = " + self.OPENAPI_FILE)
        print("# openapi version    = " + self.OPENAPI_VERSION)
        print("# title              = " + self.TITLE)
        print("# version            = " + self.VERSION)
        print("# project file name  = " + self.PROJECT_FILE)
        print("# baseURL            = " + self.BASE_URL)
        print("# gcs_okta_domain    = " + self.GCS_OKTA_DOMAIN)
        print("# authorization_code = " + self.AUTHORIZATION_CODE)
        # print('# command_param_json = ' + self.COMMAND_PARAM_FILE)
        print("# Camera             = " + self.DEVICE_ID + " (" + self.DEVICE_NAME + ")")
        print(
            "##############################################################################################################"
        )

    def UploadFile(self, type_code, file_name, file):
        files = {
            "type_code": (None, type_code),
            "file": (file_name, file, "application/octet-stream")
        }
        ret = self.Request(url="/files", method="POST", files=files)
        return ret

if __name__ == "__main__":
    command_param_file = "resources/isdc_custom_ppl_ISDC-Masa.json"
    file_name = command_param_file.split("/")[-1]

    console = AitriosConsole(
        openapi_json="resources/openapi.json",
        project_json="resources/project.json",
        camera_json="resources/camera_list.json",
        camera_index=0,
    )
    console.GetInfo()

    ret = console.GetDevice(device_id=console.DEVICE_ID)
    connectionState = ret["connectionState"]
    print(connectionState)

    #    ret = console.GetDeployConfigurations()
    #    print(ret)

    f = open(console.COMMAND_PARAM_FILE_PATH, "r")
    json_load = json.load(f)
    json_dump = json.dumps(json_load)
    param_str = Utils.Base64EncodedStr(json_dump)
    payload = {
        "file_name": console.COMMAND_PARAM_FILE,
        "parameter": param_str,
    }
    ret = console.RegistCommandParameterFile(payload=payload)
    print(ret)

    payload = {"device_ids": console.DEVICE_ID}
    # ret = console.ApplyCommandParameterFileToDevice(file_name=console.COMMAND_PARAM_FILE, payload=payload)
    # print(ret)

#    ret = console.CancelCommandParameterFile(file_name=console.COMMAND_PARAM_FILE, payload=payload)
#    print(ret)

#    ret = console.DeleteCommandParameterFile(file_name=console.COMMAND_PARAM_FILE)
#    print(ret)

# ret = console.GetDirectImageWithCrop(device_id=console.DEVICE_ID, hoffset=0, voffset=0, hsize=400, vsize=400)
# print(ret['result'])
