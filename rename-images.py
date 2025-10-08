import os

"""
Image files originally had '@bylilygaray-' at the start of the filenames. This program strips
that prefix for web display safety.
"""

DIR_NAME = r"C:\Users\jtomi\Documents\UVA\concertina-project\tomiak-chemnitzer.github.io\assets\images\lily-images"

def main():

    renamed_count = 0

    for filename in os.listdir(DIR_NAME):
        old_path = os.path.join(DIR_NAME, filename)
        new_filename = filename[13:]
        new_path = os.path.join(DIR_NAME, new_filename)

        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} -> {new_filename}")
        renamed_count += 1

    print(f"\nDone. {renamed_count} file(s) renamed.")


if __name__ == "__main__":
    main()
