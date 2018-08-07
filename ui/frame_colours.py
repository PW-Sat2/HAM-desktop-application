import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from libs.frame_recognizer import FrameRecognizer

label_material_red = "#f44336"
label_material_pink = "#e91e63"
label_material_purple = "#9c27b0"
label_material_deep_purple = "#673ab7"
label_material_indigo = "#3f51b5"
label_material_blue = "#2196f3"
label_material_light_blue = "#03a9f4"
label_material_cyan = "#00bcd4"
label_material_teal = "#0097a7"
label_material_green = "#4caf50"
label_material_light_green = "#8bc34a"
label_material_lime = "#cddc39"
label_material_yellow = "#ffeb3b"
label_material_amber = "#ffc107"
label_material_orange = "#ff9800"
label_material_deep_orange = "#ff5722"
label_material_brown = "#795548"
label_material_grey = "#9e9e9e"
label_material_blue_grey = "#607d8b"


def get_frame_type_colour(frame_type):
    switch = {
        "pong": label_material_red,
        "operation": label_material_pink,
        "error counters": label_material_purple,
        "program upload": label_material_deep_purple,
        "periodic message": label_material_indigo,
        "persistent state": label_material_blue,
        "boot slots info": label_material_light_blue,
        "compile info": label_material_cyan,
        "erase flash": label_material_teal,
        "file remove": label_material_light_green,
        "file send": label_material_indigo,
        "file list": label_material_pink,
        "telemetry": label_material_green,
        "photo": label_material_deep_purple,
        "suns": label_material_yellow,
        "experiment": label_material_amber,
        "error counter configuration": label_material_orange,
        "purge photo": label_material_deep_orange,
        "power cycle": label_material_brown,
        "sail": label_material_blue_grey,
        "time correction": label_material_red,
        "time set": label_material_purple,
        "comm": label_material_blue,
        "set bitrate": label_material_light_blue,
        "disable overheat submode": label_material_teal,
        "i2c": label_material_lime,
        "periodic set": label_material_deep_orange,
        "sail experiment": label_material_brown,
        "unknown": label_material_grey,
    }
    return switch.get(frame_type, label_material_grey)
