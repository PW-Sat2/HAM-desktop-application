import logging
import colorlog
import datetime
import time
import os


def setup_log(debug):
    logging.Formatter.converter = time.gmtime
    root_logger_std = logging.getLogger()
    root_logger_file = logging.getLogger()
    console_handler = colorlog.StreamHandler()
    current_time = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    file_handler = logging.FileHandler(os.path.join(os.path.dirname(__file__), '..', 'logs', 'pw-sat2_gs_log_{0}.log'
                                                    .format(current_time)))

    formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)-15s %(levelname)s: [%(name)s] %(message)s",
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
    )

    formatter_filelog = logging.Formatter(
        "%(asctime)-15s %(levelname)s: [%(name)s] %(message)s"
    )

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter_filelog)

    root_logger_std.addHandler(console_handler)
    root_logger_file.addHandler(file_handler)

    if debug:
        root_logger_std.setLevel(logging.DEBUG)
    else:
        root_logger_std.setLevel(logging.INFO)

    root_logger_file.setLevel(logging.DEBUG)
