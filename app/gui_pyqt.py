from PyQt4 import QtCore, QtGui
from ui.main_window import Ui_mainWindow
from app.list_item_factory import UiFrameListWidgetFactory
from app.gui_connection_state import CheckAuthThread, CheckOnlineThread
from app.upload_cloud import UploadCloudError
from app.packet_list_data import PacketListData
from app.from_file_to_gui_queue import FromFileToGuiQueueThreadFactory
from app.queue_to_signal import GetFromQueueToSignalThread
from app.handle_exit import ExitMessageHandler
import json
import webbrowser
from ui.frame_list_empty_element import UiFrameListEmptyWidget


class StartQT4(QtGui.QMainWindow):
    def __init__(self, stop_event, config, gui_queue, cloud_tx_queue, cloud_rx_queue, error_queue, path_queue,
                 send_active):
        QtGui.QWidget.__init__(self, None)

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.exit_message_handler = ExitMessageHandler(gui_queue, cloud_tx_queue, cloud_rx_queue, error_queue,
                                                       path_queue)

        self.config = config
        self.stop_event = stop_event

        self.gui_queue = gui_queue
        self.error_queue = error_queue
        self.cloud_tx_queue = cloud_tx_queue
        self.cloud_rx_queue = cloud_rx_queue
        self.send_active = send_active

        self.first_frame = True

        self.__init_ribbon()

        self.__handle_frames_file_picker()
        self.__create_start_threads()
        self.__set_send_active()
        self.__connect_demodulator_button()
        self.__add_welcome_widget()

    def __add_welcome_widget(self):
        self.ui.framesListWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        item_widget = UiFrameListEmptyWidget()

        item_widget.help_step_1.clicked.connect(lambda: webbrowser.open(self.config.config['HELP_WELCOME_STEP_1']))
        item_widget.help_step_2.clicked.connect(lambda: webbrowser.open(self.config.config['HELP_WELCOME_STEP_2']))
        item_widget.help_step_3.clicked.connect(lambda: webbrowser.open(self.config.config['HELP_WELCOME_STEP_3']))

        item = QtGui.QListWidgetItem(self.ui.framesListWidget)
        item.setSizeHint(QtCore.QSize(0, 400))
        self.ui.framesListWidget.addItem(item)
        self.ui.framesListWidget.setItemWidget(item, item_widget)

    def __remove_welcome_widget(self):
        self.ui.framesListWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.ui.framesListWidget.takeItem(0)

    def __handle_frames_file_picker(self):
        self.from_file_thread = FromFileToGuiQueueThreadFactory(self.stop_event, self.config.config, self.gui_queue)
        self.ui.loadFramesFromFileButton.clicked.connect(self.from_file_thread.load_from_file)

    def __connect_frame_uploads_buttons(self):
        self.ui.autoUploadToolButton.clicked.connect(self.__autosend_handle)
        self.ui.sendUnsuccessfulButton.clicked.connect(self.__resend_errors_handle)

    def __connect_demodulator_button(self):
        self.ui.runDemodulatorButton.clicked.connect(self.__run_demodulator)

    def __run_demodulator(self):
        pass

    def __connect_help_buttons(self):
        self.ui.helpAccountButton.clicked.connect(lambda: webbrowser.open(self.config.config['HELP_ACCOUNT']))
        self.ui.helpSignalSourceButton.clicked.connect(lambda: webbrowser.open(self.config.config['HELP_SOURCE']))
        self.ui.helpDemodulatorButton.clicked.connect(lambda: webbrowser.open(self.config.config['HELP_DEMODULATOR']))
        self.ui.helpCloudUploadButton.clicked.connect(lambda: webbrowser.open(self.config.config['HELP_UPLOAD']))

    def __create_start_threads(self):
        self.item_widgets_thread = GetFromQueueToSignalThread(self.stop_event, 0.05, self.gui_queue)
        self.item_widgets_thread.item_ready.connect(self.__process_frame_data)
        self.item_widgets_thread.start()

        self.item_widgets_update_thread = GetFromQueueToSignalThread(self.stop_event, 0.05, self.cloud_rx_queue)
        self.item_widgets_update_thread.item_ready.connect(self.__update_list)
        self.item_widgets_update_thread.start()

        self.conn_status_thread = CheckOnlineThread(self.stop_event, self.config.config)
        self.conn_status_thread.state_signal.connect(self.set_connection_status)
        self.conn_status_thread.start()

        self.auth_status_thread = CheckAuthThread(self.stop_event, self.config.config)
        self.auth_status_thread.state_signal.connect(self.set_auth_status)
        self.auth_status_thread.start()

    def __set_send_active(self):
        self.send_active.set()

    def __init_ribbon(self):
        self.__connect_help_buttons()
        self.__connect_frame_uploads_buttons()
        self.__init_credential_buttons()
        self.__init_server_connection_status_buttons()

    def __init_server_connection_status_buttons(self):
        self.ui.serverConnectionStatusTextLabel.setToolTip("Checking whether radio.pw-sat.pl is available...")
        self.ui.serverConnectionStatusTextLabel.setText("Checking status")
        self.ui.serverConnectionStatusIconLabel.setToolTip("Checking whether radio.pw-sat.pl is available...")
        self.ui.serverConnectionStatusIconLabel.setPixmap(QtGui.QPixmap(":/cloud-offline/img/cloud-offline.svg"))

    def __init_credential_buttons(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/credentials/img/key-solid-disabled.svg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.ui.credentialsButton.setIcon(icon)
        self.ui.credentialsButton.setText("Signing in...")
        self.ui.credentialsButton.setToolTip("Signing in in progress...")

    def __first_frame(self):
        if self.first_frame:
            self.first_frame = False
            return True
        return False

    def __process_frame_data(self, packet):
        if self.__first_frame():
            self.__remove_welcome_widget()

        data = self.__produce_list_item(packet)
        self.__add_to_list(data)
        self.ui.framesListWidget.scrollToBottom()
        self.cloud_tx_queue.append(data)

    def __produce_list_item(self, packet):
        item_widget = UiFrameListWidgetFactory.get(packet)
        item = QtGui.QListWidgetItem(self.ui.framesListWidget)
        item.setSizeHint(QtCore.QSize(0, 65))
        return PacketListData(item, item_widget, packet)

    def __add_to_list(self, data):
        self.ui.framesListWidget.addItem(data.item)
        self.ui.framesListWidget.setItemWidget(data.item, data.widget_item)

    def __update_list(self, data):
        base_url = self.config.config['CLOUD_URL']
        if data.upload_status:
            UiFrameListWidgetFactory.set_sent(data.widget_item, data.uuid, base_url)
        else:
            UiFrameListWidgetFactory.set_send_error(data.widget_item)

    def __autosend_handle(self):
        if self.ui.autoUploadToolButton.isChecked():
            self.ui.autoUploadToolButton.setText("Auto-Upload Enabled")
            self.send_active.set()
        else:
            self.send_active.clear()
            self.ui.autoUploadToolButton.setText("Auto-Upload Disabled")

    def __resend_errors_handle(self):
        upload = UploadCloudError(self.stop_event, self.config.config, self.cloud_rx_queue, self.error_queue)
        upload.start()

    def set_connection_status(self, status):
        if status:
            self.ui.serverConnectionStatusTextLabel.setToolTip("Server radio.pw-sat.pl is available")
            self.ui.serverConnectionStatusTextLabel.setText("Online")
            self.ui.serverConnectionStatusIconLabel.setToolTip("Server radio.pw-sat.pl is available")
            self.ui.serverConnectionStatusIconLabel.setPixmap(QtGui.QPixmap(":/cloud-online/img/cloud-online.svg"))
        else:
            self.ui.serverConnectionStatusTextLabel.setToolTip("Server radio.pw-sat.pl is not available")
            self.ui.serverConnectionStatusTextLabel.setText("Offline")
            self.ui.serverConnectionStatusIconLabel.setToolTip("Server radio.pw-sat.pl is not available")
            self.ui.serverConnectionStatusIconLabel.setPixmap(QtGui.QPixmap(":/cloud-offline/img/cloud-offline.svg"))

    def set_auth_status(self, status):
        icon = QtGui.QIcon()
        if status:
            with open(self.config.config['CREDENTIALS_FILE']) as credentials:
                credentials_data = json.load(credentials)

                icon.addPixmap(QtGui.QPixmap(":/credentials/img/key-solid.svg"), QtGui.QIcon.Normal,
                               QtGui.QIcon.Off)
                self.ui.credentialsButton.setIcon(icon)
                self.ui.credentialsButton.setText(credentials_data["identifier"])
                self.ui.credentialsButton.setToolTip("Signed up successfully")
        else:
            icon.addPixmap(QtGui.QPixmap(":/credentials/img/key-solid-disabled.svg"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            self.ui.credentialsButton.setText("Cannot sign in, trying again...")
            self.ui.credentialsButton.setToolTip("Cannot sign in - restart application, check internet connection or"
                                                 " download application from radio.pw-sat.pl again.")
        self.ui.credentialsButton.setIcon(icon)

    def closeEvent(self, event):
        self.exit_message_handler.exit_action(event)