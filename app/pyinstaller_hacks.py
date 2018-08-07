import sys
import os
import shutil


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


'''TO DO: Temporary, ugly thing to unpack some data from exe because of cloud side limitations in folders zipping'''
try:
    sys._MEIPASS
    if not os.path.exists("saved_frames"):
        os.makedirs("saved_frames")

    for i in range(1, 6):
        shutil.copyfile(resource_path('saved_frames/test_{0}.frames'.format(i)), 'saved_frames/test_{0}.frames'.format(i))
except AttributeError:
    pass
