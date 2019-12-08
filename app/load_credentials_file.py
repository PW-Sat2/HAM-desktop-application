import sys
import os
from PyQt4 import QtGui
import logging
import shutil
import unzip_credentials

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from app.validate_credentials import ValidateCredentials


class EmptyPath:
    pass

class WrongOrEmptyCredentials:
    pass

class CorrectCredentials:
    pass

class UnknownError:
    pass


class LoadCredentialsFile:
    @staticmethod
    def load_with_dialog(config):
        logger = logging.getLogger(__name__)
        try:
            file_dialog = QtGui.QFileDialog()
            path = str(file_dialog.getOpenFileName(None, 'OpenFile', '.', "Credentials file (*.json *.zip)"))
            logger.log(logging.DEBUG, "Selected file: " + path)

            if path == "":
                return EmptyPath
            else:
                path = unzip_credentials.unzip_if_needed(path)
                validate_credentials = ValidateCredentials(path)

                if validate_credentials.file_valid() and not validate_credentials.file_blank():
                    logger.log(logging.DEBUG, "File valid")
                    shutil.copyfile(path, os.path.join(os.path.dirname(__file__), '..', config['CREDENTIALS_FILE']))
                    logger.log(logging.DEBUG, "File copied")
                    return CorrectCredentials
                else:
                    logger.log(logging.DEBUG, "Wrong file")
                    return WrongOrEmptyCredentials
        except:
            logger.log(logging.ERROR, "Load file exception")
            return UnknownError
