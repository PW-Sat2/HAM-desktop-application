from sink import FrameSink
from frame_factory import FrameFactory
from setup_log import _setup_log
import argparse
import colorlog
import logging

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", required=False, default="test_frames",
                    help="Path to directory containing only binary frames (*.raw files).")
parser.add_argument("-v", "--verbose", required=False, default=False, action="store_true",
                    help="Increase output verbosity.")
parser.add_argument("--min", required=False, default=0.1, type=float,
                    help="Min. interval between frames in seconds.")
parser.add_argument("--max", required=False, default=1.0, type=float,
                    help="Max. interval between frames in seconds.")
args = parser.parse_args()

demodulator = FrameSink()
factory = FrameFactory(args.directory)

root_logger = _setup_log(args.verbose)
root_logger.log(logging.INFO, "Use Ctrl-C to terminate.")
root_logger.log(logging.INFO, "Starting frame sink")

while True:
    try:
        demodulator.sink(factory.get_random_frame())
        factory.random_sleep(args.min, args.max)
    except KeyboardInterrupt:
        root_logger.log(logging.INFO, "Terminated.")
        break
