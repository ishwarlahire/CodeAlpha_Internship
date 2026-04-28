import os
import shutil

source_folder = "photos"
destination_folder = "images"

if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        source_path = source_folder + "/" + file
        destination_path = destination_folder + "/" + file

        shutil.move(source_path, destination_path)
        print(file, "moved successfully")

print("All JPG files moved.")