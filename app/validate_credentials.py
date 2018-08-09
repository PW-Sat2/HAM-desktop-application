import json


class ValidateCredentials:
    def __init__(self, credentials_path):
        self.credentials_path = credentials_path
        self.credentials_data = None
        self.load()

    def load(self):
        with open(self.credentials_path) as credentials:
            self.credentials_data = json.load(credentials)

    def file_valid(self):
        try:
            self.credentials_data['identifier']
            self.credentials_data['password']
            return True
        except KeyError:
            return False

    def file_blank(self):
        return self.credentials_data['identifier'] == "" and self.credentials_data['password'] == ""

