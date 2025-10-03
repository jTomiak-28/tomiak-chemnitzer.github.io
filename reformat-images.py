import os, shutil

"""
Quick script to jpgs of manuscripts' first pages and add them all to a folder to use
as thumbnail images for the files.
"""

IMAGE_DIR = r"C:\Users\jtomi\Documents\UVA\concertina-project\Code\images"
OUTPUT_DIR = r"assets\images\manuscript-images"

def main():

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # make output directory if dne
    for dir in os.listdir(IMAGE_DIR):
        first_image = os.listdir(os.path.join(IMAGE_DIR, dir))[0]
        source_path = os.path.join(IMAGE_DIR, dir, first_image)
        copy_path = os.path.join(OUTPUT_DIR, dir.replace(".pdf", ".jpg"))
        shutil.copy(source_path, copy_path)


if __name__ == "__main__":
    main()