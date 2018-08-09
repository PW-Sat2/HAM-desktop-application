import sys
import os
from PyQt4 import QtGui
import logging
import shutil

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from app.validate_credentials import ValidateCredentials


class LoadCredentialsFile:
    @staticmethod
    def load_with_dialog():
        logger = logging.getLogger(__name__)
        try:
            file_dialog = QtGui.QFileDialog()
            path = file_dialog.getOpenFileName(None, 'OpenFile', '.', "Credentials file (*.json)")
            logger.log(logging.DEBUG, "Selected file: " + path)
            validate_credentials = ValidateCredentials(path)

            if validate_credentials.file_valid() and not validate_credentials.file_blank():
                logger.log(logging.DEBUG, "File valid")
                shutil.copyfile(path, 'credentials.json')
                logger.log(logging.DEBUG, "File copied")
                return True
            else:
                logger.log(logging.DEBUG, "Wrong file")
                return False
        except:
            logger.log(logging.DEBUG, "Load file exception")
            return False
