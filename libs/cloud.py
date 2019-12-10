import json
import requests
import base64
import logging
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



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
        self.MAX_IDLE_TIME = 30
        self.base_url = base_url
        self.credentials = None
        self.credentials_path = credentials_path
        self.load_credentials()
        self.last_connection_time = 0
        self.session = self.create_session()
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def create_session(self):
        s = requests.Session()
        s.verify = False
        s.headers = {'content-type': 'application/json'}

        resp = s.post(url=self.base_url + '/api/authenticate', json=self.credentials)

        self.last_connection_time = time.time()
        return s

    def authenticate(self):
        url = self.base_url + '/api/authenticate'
        response = requests.post(url, data=json.dumps(self.credentials), headers={'content-type': 'application/json'}, timeout=5)
        return response

    def validate_auth(self, auth_response):
        return len(auth_response.text) > 0

    def put_packet(self, packet):
        if (time.time() - self.last_connection_time) > self.MAX_IDLE_TIME:
            self.session = self.create_session()
            self.logger.log(logging.DEBUG, "MAX_IDLE_TIME over! Creating new session.")
        else:
            self.last_connection_time = time.time()

        url = self.base_url + '/communication/frame'

        payload = {'frame': base64.b64encode(packet['frame']),
                   'timestamp': int(packet['timestamp']*1000),
                   'traffic': 'Rx'}

        response = self.session.put(url, json=payload, timeout=10)     
        return CloudUploadResponse(response)

    def load_credentials(self):
        with open(self.credentials_path) as f:
            self.credentials = json.load(f)
