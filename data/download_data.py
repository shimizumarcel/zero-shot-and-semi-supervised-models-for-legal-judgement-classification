import gdown
import os

FOLDER_ID = "1Et6VoWyHnN_F9E21-9xTU4ZSKJWYZqNS?usp=sharing"
OUTPUT_DIR = os.path.join(os.getcwd(), "downloaded_data")

def download_to_local():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    gdown.download_folder(
        url=f"https://drive.google.com/drive/folders/{FOLDER_ID}",
        output=OUTPUT_DIR,
        quiet
