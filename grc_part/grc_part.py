import argparse
import UserList
import UserString
import UserDict
import itertools
import collections
import future.backports.misc
import gnuradio
import sys
from PyQt4 import QtGui
import threading

try:
    import grc.source.file_source.iq_file_main as file_source
except:
    print "Cannot import file_source"

try:
    import grc.source.ssb_audio_source.ssb_audio_source_main as ssb_audio_source
except:
    print "Cannot import file_source"

try:
    import grc.source.funcube_source.funcube_source_source_parameter as funcube_source_source_parameter
except:
    print "Cannot import funcube_source"

try:
    import grc.source.plutosdr_source.plutosdr_source_source_parameter as plutosdr_source_source_parameter
except:
    print "Cannot import plutosdr_source"

try:
    import grc.source.rtl_sdr_source.rtl_sdr_source_source_parameter as rtl_sdr_source_source_parameter
except:
    print "Cannot import rtl_sdr_source"

try:
    import grc.downlink as demodulator
except:
    print "Cannot import demodulator"

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", required=False, default=False, action="store_true",
                    help="Increase output verbosity.")
parser.add_argument("-p", "--path", required=False, default="",
                    help="Path for IQ recording (for File IQ source)")
parser.add_argument("-s", "--source", required=True, default="",
                    help="Source:")
args = parser.parse_args()


class ParamshWrapper:
    def __init__(self, device):
        self.device = str(device)


class DeviceName(QtGui.QWidget):
    def __init__(self):
        super(DeviceName, self).__init__()

    def dialog(self, window_title, text_label, default_text):
        return QtGui.QInputDialog.getText(self, window_title, text_label, QtGui.QLineEdit.Normal, default_text)


def show_dialog(window_title, text_label, default_text):
    app = QtGui.QApplication(sys.argv)
    ex = DeviceName()
    resp = ex.dialog(window_title, text_label, default_text)
    return resp



if args.source == "iq_file":
    print "IQ File"
    file_source.application()

elif args.source == "pluto":
    resp = show_dialog("Select Pluto SDR source address", 
        "<b>Click OK to use default IP address.</b><br>"
        "Otherwise enter custom IP address in field below:",
        "ip:192.168.2.1")
    if resp[1]:
        params = ParamshWrapper(resp[0])
        
        print "Pluto"
        t = threading.Thread(target=plutosdr_source_source_parameter.main, kwargs={"options" : params})
        t.start()
        t.join()
        

elif args.source == "fcd+":
    resp = show_dialog("Select FUNcube Dongle Pro+ source device name",
        "<b>Leave empty field for default device name.</b><br>"
        "Otherwise enter custom ALSA device name e.g.:<br>"
        "<i>hw:1</i> or <i>plughw:1,0</i>.",
        "")
    if resp[1]:
        params = ParamshWrapper(resp[0])

        print "Funcube Dongle Plus"
        t = threading.Thread(target=funcube_source_source_parameter.main, kwargs={"options" : params})
        t.start()
        t.join()

elif args.source == "rtl-sdr":
    resp = show_dialog("Select RTL-SDR source device number",
        "<b>Click OK to use default RTL-SDR number.</b>.<br>"
        "Otherwise enter custom device number e.g. <i>rtl=1</i> (or higher).",
        "rtl=0")
    if resp[1]:
        params = ParamshWrapper(resp[0])

        print "RTL-SDR"
        t = threading.Thread(target=rtl_sdr_source_source_parameter.main, kwargs={"options" : params})
        t.start()
        t.join()

elif args.source == "ssb":
    print "ssb audio"
    ssb_audio_source.application()

elif args.source == "demodulator":
    print "demodulator"
    demodulator.main()

else:
    print "Wrong parameter!"
