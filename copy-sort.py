import os
import shutil
import sys


def copy_and_sort(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)

        if os.path.isdir(item_path):
            copy_and_sort(item_path, destination_dir)
        elif os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1]
            target_subdir = os.path.join(destination_dir, file_extension)

            if not os.path.exists(target_subdir):
                os.makedirs(target_subdir)

            shutil.copy(item_path, target_subdir)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <source_directory> <destination_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    copy_and_sort(source_directory, destination_directory)
    print("Files copied and sorted successfully!")
