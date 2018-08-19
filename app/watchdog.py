from threading import Thread
import sys
import os
import logging


class Watchdog(Thread):
    def __init__(self, stop_event, file_save_thread, frames_receiver_thread, upload_cloud_thread,
                 auth_status_thread, conn_status_thread, item_widgets_thread, item_widgets_update_thread):
        Thread.__init__(self)

        self.stop_event = stop_event

        self.python_threads = [file_save_thread, frames_receiver_thread, upload_cloud_thread]
        self.qt_threads = [auth_status_thread, conn_status_thread, item_widgets_thread, item_widgets_update_thread]

        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def run(self):
        while not self.stop_event.wait(1):
            try:
                for thread in self.python_threads:
                    if not thread.is_alive():
                        thread.start()
                        self.logger.log(logging.DEBUG, "Starting thread that was not alive " + str(thread))

                for thread in self.qt_threads:
                    if not thread.isRunning():
                        thread.start()
                        self.logger.log(logging.DEBUG, "Starting thread that was not alive " + str(thread))
            except:
                self.logger.log(logging.DEBUG, "Exception in Watchdog thread!")
        self.logger.log(logging.DEBUG, "Finished Watchdog")
