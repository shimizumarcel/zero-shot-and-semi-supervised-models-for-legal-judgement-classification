# download_data.py
import gdown
import os

# Configuration
FOLDER_ID = "1Et6VoWyHnN_F9E21-9xTU4ZSKJWYZqNS?usp=sharing"
FOLDER_URL = f"https://drive.google.com/drive/folders/1Et6VoWyHnN_F9E21-9xTU4ZSKJWYZqNS?usp=sharing"
OUTPUT_DIR = "./data/"

def download_folder(folder_url, output_dir):
    """Downloads all files from a shared Google Drive folder."""
    os.makedirs(output_dir, exist_ok=True)
    os.chdir(output_dir)  # Download directly into ./data/
    gdown --folder "{folder_url}"
    print(f"\nAll files downloaded to: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    print("Downloading data files...")
    download_folder(FOLDER_URL, OUTPUT_DIR)
