import os
import shutil
import typer
from datetime import datetime

app = typer.Typer()

def read_files_list(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def copy_files(src_folder, dest_folder, files_to_copy=None, txt_content=None):
    # Get the current date and time
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")

    # Create the destination folder with the timestamp
    dest_path = os.path.join(dest_folder, timestamp)
    os.makedirs(dest_path, exist_ok=True)

    # Create a log file in the destination folder
    log_file_path = os.path.join(dest_path, "copy_log.txt")
    with open(log_file_path, 'w') as log_file:
        log_file.write(f"Copy operation started at {now}\n")
        log_file.write(f"Source folder: {src_folder}\n")
        log_file.write(f"Destination folder: {dest_path}\n")
        log_file.write("Files copied:\n")

        # Copy specified files or all files if none specified
        if files_to_copy:
            for filename in files_to_copy:
                src_path = os.path.join(src_folder, filename)
                dest_path_full = os.path.join(dest_path, filename)
                dest_dir = os.path.dirname(dest_path_full)
                os.makedirs(dest_dir, exist_ok=True)
                if os.path.isfile(src_path):
                    shutil.copy(src_path, dest_path_full)
                    log_file.write(f"Copied file: {filename}\n")
                elif os.path.isdir(src_path):
                    shutil.copytree(src_path, dest_path_full, dirs_exist_ok=True)
                    log_file.write(f"Copied directory: {filename}\n")
                else:
                    log_file.write(f"{filename} does not exist in the source folder.\n")
        else:
            for filename in os.listdir(src_folder):
                src_path = os.path.join(src_folder, filename)
                dest_path_full = os.path.join(dest_path, filename)
                dest_dir = os.path.dirname(dest_path_full)
                os.makedirs(dest_dir, exist_ok=True)
                if os.path.isfile(src_path):
                    shutil.copy(src_path, dest_path_full)
                    log_file.write(f"Copied file: {filename}\n")
                elif os.path.isdir(src_path):
                    shutil.copytree(src_path, dest_path_full, dirs_exist_ok=True)
                    log_file.write(f"Copied directory: {filename}\n")

        log_file.write("Copy operation completed.\n")

    # Save the .txt content to a file in the destination folder
    if txt_content:
        txt_file_path = os.path.join(dest_path, "logs.txt")
        with open(txt_file_path, 'w') as txt_file:
            txt_file.write(txt_content)

    print(f"Files copied to {dest_path}")

@app.command()
def main(
    files_list_path: str = typer.Option(None, help="Path to the file containing the list of files to copy."),
    src_folder: str = typer.Option(..., help="Path to the source directory."),
    dest_folder: str = typer.Option(..., help="Path to the destination directory."),
    txt_content: str = typer.Option("", help="Content to be saved in a .txt file in the destination folder."),
):
    files_to_copy = read_files_list(files_list_path) if files_list_path else None
    copy_files(src_folder, dest_folder, files_to_copy, txt_content)

    print("\nfiles_to_copy: ", files_to_copy)
    print("\nsrc_folder: ", src_folder)
    print("\ndest_folder: ", dest_folder)

if __name__ == "__main__":
    app()
