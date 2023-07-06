import os
import shutil
import datetime
import zipfile

source_directory = r"C:\Users\vmirzac\OneDrive - ENDAVA\Desktop\AutomationBoringStuffWithPython\2_CopyFolder\SourceFolder"
destination_directory = r"C:\Users\vmirzac\OneDrive - ENDAVA\Desktop\AutomationBoringStuffWithPython\2_CopyFolder\DestinationFolder"

# Create a timestamp for the backup folder
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")

# Append the timestamp to the destination directory
backup_directory = os.path.join(destination_directory, f"backup_{timestamp}")

# Check if the destination directory already exists, and if so, create a unique backup directory name
if os.path.exists(backup_directory):
    counter = 1
    while os.path.exists(backup_directory):
        backup_directory = os.path.join(destination_directory, f"backup_{timestamp}_{counter}")
        counter += 1

# Create the backup directory
os.makedirs(backup_directory)

# Copy files from the source directory to the backup directory
for root, dirs, files in os.walk(source_directory):
    for file in files:
        source_path = os.path.join(root, file)
        destination_path = os.path.join(backup_directory, os.path.relpath(source_path, source_directory))
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        shutil.copy2(source_path, destination_path)

# Create a zip archive of the backup directory
zip_filename = os.path.join(destination_directory, f"backup_{timestamp}.zip")
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(backup_directory):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, backup_directory)
            zipf.write(file_path, arcname)

# Remove the backup directory _ 
shutil.rmtree(backup_directory)

print("Backup and archiving completed successfully.")