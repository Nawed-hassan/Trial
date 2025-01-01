import os

# Specify the directory path
directory_path = 'E:\CODES\CWH'

# Get the list of files and directories in the specified path
contents = os.listdir(directory_path)
print(f"Contents of '{directory_path}':")
for item in contents:
    print(item)
