import os
import time

# Define the directory you want to clean.
directory_to_clean = "C:/Path/To/Your/Directory"

# Define the threshold in seconds (7 days).
threshold = 7 * 24 * 60 * 60

# Define the log file.
log_file = "cleanup_log.txt"

def cleanup_directory(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            file_age = time.time() - os.path.getctime(file_path)
            
            if file_age > threshold:
                print(f"Deleting file: {file_path}")
                os.remove(file_path)
                with open(log_file, "a") as log:
                    log.write(f"Deleted file: {file_path}\n")
                
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            folder_age = time.time() - os.path.getctime(folder_path)
            
            if folder_age > threshold:
                print(f"Deleting folder: {folder_path}")
                os.rmdir(folder_path)
                with open(log_file, "a") as log:
                    log.write(f"Deleted folder: {folder_path}\n")

if __name__ == "__main__":
    cleanup_directory(directory_to_clean)
