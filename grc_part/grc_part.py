import argparse
import gnuradio
import grc.source.file_source.iq_file_main as file_source
import grc.source.funcube_source.funcube_source as funcube_source
import grc.source.plutosdr_source.plutosdr_source as plutosdr_source
import grc.source.rtl_sdr_source.rtl_sdr_source as rtl_sdr_source
import grc.downlink as demodulator

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", required=False, default=False, action="store_true",
                    help="Increase output verbosity.")
parser.add_argument("-p", "--path", required=False, default="",
                    help="Path for IQ recording (for File IQ source)")
parser.add_argument("-s", "--source", required=True, default="",
                    help="Source:")
args = parser.parse_args()

if args.source == "iq_file":
    print "IQ File"
    file_source.application()
elif args.source == "pluto":
    plutosdr_source.main()
    print "Pluto"
elif args.source == "fcd+":
    print "Funcube Dongle Plus"
    funcube_source.main()
elif args.source == "rtl-sdr":
    print "RTL-SDR"
    rtl_sdr_source.main()
elif args.source == "demodulator":
    print "demodulator"
    demodulator.main()
else:
    print "Wrong parameter!"
