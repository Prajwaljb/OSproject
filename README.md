# Automated Backup Script (Python)

This project is a simple Python-based automated backup utility that periodically creates timestamped backups of a source directory into a destination directory. It is useful for safeguarding important files, project folders, or datasets by maintaining regular backups with minimal manual intervention.

## Features

* Automatically creates backups at fixed time intervals
* Stores backups in timestamped folders for easy versioning
* Copies both files and directories
* Ignores unnecessary folders like .git and **pycache**
* Logs all backup activity and errors to a log file
* Runs continuously in the background once started

## Project Structure

```
.
├── backup.py
├── backup_log.txt
└── README.md
```

## Requirements

* Python 3.7 or higher
* Standard Python libraries only (no external dependencies)

## Configuration

Open the script and modify the following variables as needed:

```python
SOURCE_DIR = r'D:\Code\images'
DEST_DIR = r'D:\Dest'
BACKUP_INTERVAL = 86400
```

* SOURCE_DIR – Directory to be backed up
* DEST_DIR – Location where backups will be stored
* BACKUP_INTERVAL – Time interval in seconds between backups (86400 seconds = 24 hours)

## How It Works

* A new backup folder is created using the current timestamp
* All files and directories from the source folder are copied
* Each backup is stored separately to preserve previous versions
* Activity and errors are written to backup_log.txt
* The script waits for the specified interval and repeats the process

## Running the Script

```bash
python backup.py
```

The script will continue running until it is manually stopped.

## Logs

All operations are logged to:

```
D:\Code\webproj\backup_log.txt
```

Logs include:

* Backup completion timestamps
* Waiting intervals
* Errors during file operations

## Use Cases

* Daily backups of project folders
* Personal file safety
* Dataset version preservation
* Lightweight alternative to full backup tools

## Notes

* Ensure both source and destination directories exist before running
* The script is designed for Windows paths but can be adapted for other operating systems
* Run the script using Task Scheduler or a background process for automation

## License

This project is open-source and free to use for personal or educational purposes.
