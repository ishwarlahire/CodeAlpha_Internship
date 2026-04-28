# Task Automation with Python Scripts
import os
import shutil
import re
import requests

print("TASK AUTOMATION WITH PYTHON")
print("1. Move JPG Files")
print("2. Extract Emails from TXT File")
print("3. Get Website Title")
print("4. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    source_folder = input("Enter source folder name: ")
    destination_folder = input("Enter destination folder name: ")

    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)

    files = os.listdir(source_folder)

    for file in files:
        if file.endswith(".jpg"):
            shutil.move(source_folder + "/" + file,
                        destination_folder + "/" + file)
            print(file, "moved successfully")

    print("All JPG files moved.")

elif choice == "2":
    file = open("data.txt", "r")
    data = file.read()

    emails = re.findall(r'\S+@\S+', data)

    save = open("emails.txt", "w")

    for email in emails:
        save.write(email + "\n")

    print("Emails extracted successfully.")

elif choice == "3":
    try:
        url = input("Enter website URL: ")

        response = requests.get(url)
        html = response.text

        start = html.find("<title>") + 7
        end = html.find("</title>")

        title = html[start:end]

        file = open("title.txt", "w")
        file.write(title)

        print("Website title saved:", title)

    except:
        print("Invalid URL")

elif choice == "4":
    print("Program closed.")

else:
    print("Invalid choice")