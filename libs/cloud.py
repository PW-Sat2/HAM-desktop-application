import json
import requests
import base64
import logging


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
        self.credentials_path = credentials_path
        self.load_credentials()
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def authenticate(self):
        url = self.base_url + '/api/authenticate'
        response = requests.post(url, data=json.dumps(self.credentials), headers=self.headers, timeout=5)
        return response.cookies

    def validate_auth(self, auth_response):
        return len(auth_response.items()) > 0

    def put_packet(self, packet):
        url = self.base_url + '/communication/frame'

        payload = {'frame': base64.b64encode(packet['frame']),
                   'timestamp': int(packet['timestamp']*1000),
                   'traffic': 'Rx'}

        response = requests.put(url, data=json.dumps(payload), headers=self.headers, cookies=self.authenticate(),
                                timeout=5)
        return CloudUploadResponse(response)

    def load_credentials(self):
        with open(self.credentials_path) as f:
            self.credentials = json.load(f)
