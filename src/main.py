import os
import json
import argparse


parser = argparse.ArgumentParser(description='Create directory structure from json file')
parser.add_argument('json_file', type=str, help='json file containing the directory structure')
parser.add_argument('output_dir', type=str, help='output directory')
args = parser.parse_args()


# A function to open a file and return the content
def open_file(file_path: str) -> str:
    # Open the file
    with open(file_path, "r") as file:
        # Return the content
        return file.read()

# A function wich creates a directory structure and creates files if there is an extention based on a JSON
def create_directory_structure(json_data: dict, path: str = ""):
    # Loop through the JSON data
    for key in json_data:
        # If the value of the key is a dict, it means we are at a folder
        if isinstance(json_data[key], dict):
            # Create the folder
            os.mkdir(os.path.join(path, key))
            # Call the function again with the new path
            create_directory_structure(json_data[key], os.path.join(path, key))
        # If the value of the key is not a dict, it means we are at a file
        else:
            # Create the file
            open(os.path.join(path, key), "w").close()


schema2 = open_file(args.json_file)
json_object = json.loads(schema2)
create_directory_structure(json_object, args.output_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create directory structure from json file')
    parser.add_argument('json_file', type=str, help='json file containing the directory structure')
    parser.add_argument('output_dir', type=str, help='output directory')
    args = parser.parse_args()
    schema2 = open_file(args.json_file)
    json_object = json.loads(schema2)
    create_directory_structure(json_object, args.output_dir)
