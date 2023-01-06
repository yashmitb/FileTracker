import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = "C:/Users/yashm/Downloads"
to_dir = "C:/Users/yashm/Downloads/Files"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'],
    "Audio_Files": [".wav", ".mp3"]
}

# Event Hanlder Class


class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(event.src_path + " was created!")

    def on_modified(self, event):
        print(event.src_path + " was modfied!")

    def on_moved(self, event):
        print(event.src_path + " was moved!")

    def on_deleted(self, event):
        print(event.src_path + " was deleted!")


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stoped")
    observer.stop()
