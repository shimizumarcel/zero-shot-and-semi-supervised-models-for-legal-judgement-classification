# download_data.py
import gdown
import os

FOLDER_ID = "1Et6VoWyHnN_F9E21-9xTU4ZSKJWYZqNS?usp=sharing"
FOLDER_URL = f"https://drive.google.com/drive/folders/{FOLDER_ID}"
OUTPUT_DIR = "./data/"

def download_folder(folder_url, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    

    gdown.download_folder(
        url=folder_url,
        output=output_dir,
        quiet=False,
        use_cookies=False
    )

if __name__ == "__main__":
    print("Downloading files...")
    download_folder(FOLDER_URL, OUTPUT_DIR)
