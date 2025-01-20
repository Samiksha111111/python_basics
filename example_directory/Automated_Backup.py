import os
import datetime
import shutil

directory = "./example_directory"

def backup(directory):
    if os.path.isdir(directory):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") 
        backup = f"Backup_{timestamp}" 
        shutil.make_archive(backup, 'zip', directory)
        print(f"Backup created: {backup}.zip")
    else:
        print("Invalid format")  

backup(directory)


        














