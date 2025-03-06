# VerionBot

This script copies files from a source directory to a destination directory, optionally using a list of files to copy. It also logs the copy operation and can save additional content to a `.txt` file in the destination folder.

## Requirements

- Python 3.10.0
- `Typer` library

## Installation

1. Clone the repository or download the script.
2. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

You can run the script from the command line with the following options:

```bash
python save.py --files-list-path <FILES_LIST_PATH> --src-folder <SRC_FOLDER> --dest-folder <DEST_FOLDER> --txt-content <TXT_CONTENT>
```

### Options
- `--files-list-path`: Path to the file containing the list of files to copy. Each line in the file should contain a file name. (Optional)  
- `--src-folder`: Path to the source directory. (Required)  
- `--dest-folder`: Path to the destination directory. (Required)  
- `--txt-content`: Content to be saved in a .txt file in the destination folder. (Optional)  