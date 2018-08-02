import json
import requests
import time
import base64


class CloudUploadResponse:
    def __init__(self, response):
        self.status = self.__get_status(response)
        self.uuid = self.__get_uuid(response)

    def __get_uuid(self, response):
        return response.text.split()[-1]

    def __get_status(self, response):
        success_reponse = "frame added:"
        return response.text[0:len(success_reponse)] == success_reponse


class Cloud:
    def __init__(self, base_url, credentials_path):
        self.headers = {'content-type': 'application/json'}
        self.base_url = base_url
        self.credentials = None
        self.load_credentials(credentials_path)

    def authenticate(self):
        url = self.base_url + '/api/authenticate'
        response = requests.post(url, data=json.dumps(self.credentials), headers=self.headers)
        return response.cookies

    def validate_auth(self, auth_response):
        return len(auth_response.items()) > 0

    def put_packet(self, packet):
        url = self.base_url + '/communication/frame'

        payload = {'frame': base64.b64encode(packet['frame']),
                   'timestamp': int(packet['timestamp']*1000),
                   'traffic': 'Rx'}

        response = requests.put(url, data=json.dumps(payload), headers=self.headers, cookies=self.authenticate())
        return CloudUploadResponse(response)

    def load_credentials(self, path):
        with open(path) as f:
            self.credentials = json.load(f)
