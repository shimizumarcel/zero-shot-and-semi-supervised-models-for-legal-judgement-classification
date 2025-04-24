import gdown
import os

FOLDER_ID = "1Et6VoWyHnN_F9E21-9xTU4ZSKJWYZqNS?usp=sharing"
OUTPUT_DIR = "./data/"

# Força o gdown a não criar subpasta
os.makedirs(OUTPUT_DIR, exist_ok=True)
gdown.download_folder(
    url=f"https://drive.google.com/drive/folders/{FOLDER_ID}",
    output=OUTPUT_DIR,
    quiet=False,
    use_cookies=False,
    remaining_ok=True
)
