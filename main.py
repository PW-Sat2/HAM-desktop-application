import sys
import os
from PyQt4 import QtCore, QtGui
from PyQt4 import QtSvg
from app.receive_distribute import ReceiveDistribute
from app.upload_cloud import UploadCloud
from app.save_frames_file import SaveFramesFileThread
from threading import Event
from app.setup_log import setup_log
import imp
import Queue
from collections import deque
from zmq import *
from app.gui_pyqt import StartQT4
from app.pyinstaller_hacks import resource_path
import shutil
import argparse
from ui.credentials_choose import CredentialsChooseWidget
import colorlog

if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the pyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", required=False, default=False, action="store_true",
                    help="Increase output verbosity.")
args = parser.parse_args()

setup_log(args.verbose)
config = imp.load_source('config', os.path.join(application_path, 'config.py'))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gui_queue = deque()
    cloud_tx_queue = deque()
    cloud_rx_queue = deque()
    error_queue = deque()
    file_queue = Queue.Queue()
    path_queue = Queue.Queue()

    stop_event = Event()
    send_active = Event()

    upload_cloud_thread = UploadCloud(stop_event, config.config, cloud_rx_queue, cloud_tx_queue, error_queue,
                                      send_active)
    upload_cloud_thread.start()

    file_save_thread = SaveFramesFileThread(stop_event, config.config, file_queue, path_queue)
    file_save_thread.start()

    frames_receiver_thread = ReceiveDistribute(stop_event, config.config, gui_queue, file_queue)
    frames_receiver_thread.start()

    hamApp = StartQT4(stop_event, config, gui_queue, cloud_tx_queue, cloud_rx_queue, error_queue, path_queue,
                      send_active, upload_cloud_thread, application_path)

    hamApp.show()

    status = app.exec_()
    stop_event.set()
    upload_cloud_thread.join()
    frames_receiver_thread.join()
    file_save_thread.join()
    sys.exit(status)
