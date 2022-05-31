import os

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

PC_USER = 'windows_username';
DIRECTORY_TO_WATCH = f"C:/Users/{PC_USER}/Downloads/";
IMAGES_DIR = DIRECTORY_TO_WATCH + "Images/";
VIDEOS_DIR = DIRECTORY_TO_WATCH + "Videos/";
EXCEL_DIR = DIRECTORY_TO_WATCH + "Excel/";

class Watcher:


    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error");

        self.observer.join()


class Handler(FileSystemEventHandler):

    def on_any_event(self, event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - %s." % event.src_path);
            self.moveFiles();

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print("Received modified event - %s." % event.src_path);
            self.moveFiles();

    def moveFiles(self):
        entries = os.listdir(DIRECTORY_TO_WATCH);
        for entry in entries:
            time.sleep(1);
            if entry.endswith(".jpg") or entry.endswith(".png") or entry.endswith(".gif"):
                try:
                    os.rename(DIRECTORY_TO_WATCH + entry, IMAGES_DIR + entry);
                except:
                    print("Error moving file: " + entry);
            elif entry.endswith(".mp4") or entry.endswith(".avi") or entry.endswith(".mkv"):
                try:
                    os.rename(DIRECTORY_TO_WATCH + entry, VIDEOS_DIR + entry);
                except:
                    print("Error moving file: " + entry);
            elif entry.endswith(".xlsx") or entry.endswith(".xls") or entry.endswith(".csv"):
                try:
                    os.rename(DIRECTORY_TO_WATCH + entry, EXCEL_DIR + entry);
                except:
                    print("Error moving file: " + entry);
            else:
                print(f"{entry} is not a supported file type.");


if __name__ == '__main__':
    w = Watcher()
    w.run()


