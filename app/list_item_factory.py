import sys
import os
import datetime
from PyQt4 import QtGui

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from ui.frame_list_element import UiFrameListWidget
from libs.frame_recognizer import FrameRecognizer
from ui.frame_colours import get_frame_type_colour
import webbrowser


class UiFrameListWidgetFactory:
    @staticmethod
    def get(packet):
        widget = UiFrameListWidget()
        widget.uuidValueLabel.setOpenExternalLinks(True)
        widget.timestampLabel.setText(UiFrameListWidgetFactory.__format_timestamp(packet))
        widget.timestampLabel.setToolTip(UiFrameListWidgetFactory.__generate_tooltip("Timestamp"))
        widget = UiFrameListWidgetFactory.set_not_send(widget)
        widget = UiFrameListWidgetFactory.__format_frame_type(packet, widget)
        return widget

    @staticmethod
    def __format_timestamp(packet):
        return datetime.datetime.utcfromtimestamp(packet["timestamp"]).strftime("%Y-%m-%d %H:%M:%S.%f")[0:-3]

    @staticmethod
    def set_not_send(widget):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cloud-offline/img/cloud-offline.svg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        widget.uploadStatusIconButton.setIcon(icon)

        widget.uuidValueLabel.setText("-")

        widget.uploadStatusIconButton.setToolTip(
            UiFrameListWidgetFactory.__generate_tooltip("Frame not send to cloud yet!"))
        widget.uuidValueLabel.setToolTip(
            UiFrameListWidgetFactory.__generate_tooltip("Send the frame to cloud to get an uuid"))
        widget.uuidTextLabel.setToolTip(
            UiFrameListWidgetFactory.__generate_tooltip("Frame identifier on server"))
        return widget

    @staticmethod
    def set_sent(widget, uuid, server):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cloud-online/img/cloud-online.svg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        widget.uploadStatusIconButton.setIcon(icon)

        widget.uuidValueLabel.setText(UiFrameListWidgetFactory.__generate_uuid_formatted_link(uuid, server))

        widget.uploadStatusIconButton.setToolTip(
            UiFrameListWidgetFactory.__generate_tooltip("Frame send to cloud, thanks!"))
        widget.uuidValueLabel.setToolTip(
            UiFrameListWidgetFactory.__generate_tooltip("Click to see frame contents"))
        widget.uuidTextLabel.setToolTip(
            UiFrameListWidgetFactory.__generate_tooltip("Frame identifier on server"))

        widget.uploadStatusIconButton.clicked.connect(lambda: webbrowser.open(UiFrameListWidgetFactory.__generate_uuid_link(uuid, server)))
        return widget

    @staticmethod
    def set_send_error(widget):
        widget.uploadStatusIconButton.setToolTip(
            UiFrameListWidgetFactory.__generate_tooltip("Frame send error - try again - push button "
                                                        "\"Cloud Upload --> Re-send Unsuccessful\""
                                                        "or download application from radio.pw-sat.pl again"))
        widget.uuidValueLabel.setToolTip(
            UiFrameListWidgetFactory.__generate_tooltip("Frame send error - try again - push button "
                                                        "\"Cloud Upload --> Re-send Unsuccessful\""
                                                        "or download application from radio.pw-sat.pl again"))
        widget.uuidValueLabel.setText("<span style=\"color: #d50000;\">Error in sending to cloud - try again</span>")
        return widget

    @staticmethod
    def __generate_uuid_formatted_link(uuid, server):
        return "<a style = \"color: #414141;\" href =\"{0}/telemetry/detailed/frame/{1}\">{2}</a>".format(
            server, uuid, uuid)

    @staticmethod
    def __generate_uuid_link(uuid, server):
        return "{0}/telemetry/detailed/frame/{1}".format(server, uuid)

    @staticmethod
    def __generate_tooltip(text):
        return "<span style='font-size: 12pt;'>" + text + "</span>"

    @staticmethod
    def __determine_frame_type(packet):
        frame = packet["frame"]
        apid = FrameRecognizer.get_apid(frame)
        return FrameRecognizer.match_apid(apid)

    @staticmethod
    def __format_frame_type(packet, widget):
        frame_type = UiFrameListWidgetFactory.__determine_frame_type(packet)
        colour = get_frame_type_colour(frame_type)

        widget.frameTypeLabel.setStyleSheet('background-color: {0}; color:#ffffff; border: none; '
                                            'font-weight: bold; font-size: 11px;'.format(colour))
        widget.frameTypeLabel.setText(frame_type)
        return widget






