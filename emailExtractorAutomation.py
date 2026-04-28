import re

file = open("data.txt", "r")
data = file.read()

emails = re.findall(r'\S+@\S+', data)

save = open("emails.txt", "w")

for email in emails:
    save.write(email + "\n")

print("Emails Extracted Successfully")