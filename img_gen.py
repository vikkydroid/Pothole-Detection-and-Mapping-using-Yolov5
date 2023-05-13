import os
import subprocess

# Set the directory path where the text files are located
directory_path = "C:\\Users\\lenovo\\Desktop\\spothole\\yolov5\\img_list\\labels"

# Create a new text file to store the modified file names
with open("image_list.txt", "w") as f:
    # Get a list of all files in the directory
    file_list = os.listdir(directory_path)
    # Iterate over the files and modify the text file names
    for file_name in file_list:
        if file_name.endswith(".txt"):
            file_name = file_name[:-4] + ".jpg"
        # Write the modified file name to the new text file
        f.write(file_name + "\n")

subprocess.call(['python', 'upload_gps.py'])