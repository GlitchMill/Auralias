import os
import shutil
import sys
from tinytag import TinyTag

# This Function Sucks ass ngl!
# Function to get album name and composer
def get_album_info(file_path):
    tag = TinyTag.get(file_path)
    album = tag.album if tag.album else "Unknown Album"
    composer = tag.composer if tag.composer else "Unknown Composer"
    return album, composer

# Function to sort files
def sort_files(root_dir):
    sorted_dir = os.path.join(root_dir, "sorted")
    
    # Check if sorted directory exists
    if not os.path.exists(sorted_dir):
        os.makedirs(sorted_dir)

    # Iterate through files in root directory
    for filename in os.listdir(root_dir):
        if filename.endswith(".flac") or filename.endswith(".m4a"):
            file_path = os.path.join(root_dir, filename)
            # Get album info
            album, composer = get_album_info(file_path)
            # Create directory if it doesn't exist
            album_dir = os.path.join(sorted_dir, f"{album}")
            if not os.path.exists(album_dir):
                os.makedirs(album_dir)
            # Move file to album directory
            shutil.move(file_path, os.path.join(album_dir, filename))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_directory>")
        sys.exit(1)

    root_directory = sys.argv[1]
    print(f"Sorting files in directory: {root_directory}")

    sort_files(root_directory)
