import json
import os

PROJECT_NAME = "saki"

# getting full path to the ini file
dir = os.path.dirname(__file__)
filename = os.path.join(dir, "./code.json")

# opening
with open(filename) as f:
    reader = json.load(f)

# reading all the file objects in json file
files = reader.get('files')

# iterating through all files and writing data to appropriate files
for file in files:
    with open(file.get("location").format(PROJECT_NAME), 'w') as f:
        f.write(
            "\n".join(file.get("content")).format(PROJECT_NAME)
        )
