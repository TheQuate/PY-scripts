import os
import shutil

# Function to move files to folders based on the first three letters
def sort_files(source_folder, destination_folder):
    for filename in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, filename)):
            # Get the first three characters of the file name
            first_three_letters = filename[:3].upper()  # Convert to uppercase for consistency
            
            # Define the destination folder based on the first three letters
            destination_folder_based_on_name = os.path.join(destination_folder, first_three_letters)
            
            # Move the file to the destination folder if the folder exists
            if os.path.exists(destination_folder_based_on_name) and os.path.isdir(destination_folder_based_on_name):
                shutil.move(os.path.join(source_folder, filename), os.path.join(destination_folder_based_on_name, filename))
            else:
                print(f"No matching folder found for '{first_three_letters}' - File '{filename}' not moved.")

# Set paths for source and destination folders
source_folder_path = 'C:/temp/Skjema'  # Path to the folder containing the files you want to sort
destination_folder_path = 'C:/temp'  # Path to the main folder where you want to sort the files

# Get the full paths by joining with the current working directory
source_folder = os.path.join(os.getcwd(), source_folder_path)
destination_folder = os.path.join(os.getcwd(), destination_folder_path)

# Call the function to sort files
sort_files(source_folder, destination_folder)
