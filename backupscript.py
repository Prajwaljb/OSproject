import shutil
import os
from datetime import datetime
import logging
import sys
import time

# Configure logging
logging.basicConfig(filename=r'D:\Code\webproj\backup_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def backup_files(source_dir, dest_dir):
    try:
        # Create a timestamp for the backup
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_dir = os.path.join(dest_dir, f'backup_{timestamp}')
        os.makedirs(backup_dir)

        # Copy files and directories
        for item in os.listdir(source_dir):
            s = os.path.join(source_dir, item)
            d = os.path.join(backup_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, False, shutil.ignore_patterns('.git', '__pycache__'))
            else:
                shutil.copy2(s, d)

        logging.info(f'Backup completed successfully at {timestamp}')
    except Exception as e:
        logging.error(f'Error occurred during backup: {e}')

def run_backup_periodically(source_dir, dest_dir, interval):
    while True:
        backup_files(source_dir, dest_dir)
        logging.info(f'Waiting for {interval} seconds before the next backup...')
        time.sleep(interval)

if __name__ == "__main__":
    # Configuration
    SOURCE_DIR = r'D:\Code\images'
    DEST_DIR = r'D:\Dest'
    BACKUP_INTERVAL = 86400  # Interval in seconds (e.g., 86400 seconds = 24 hours)

    if not os.path.exists(SOURCE_DIR):
        logging.error(f'Source directory does not exist: {SOURCE_DIR}')
        sys.exit(1)

    if not os.path.exists(DEST_DIR):
        logging.error(f'Destination directory does not exist: {DEST_DIR}')
        sys.exit(1)

    logging.info('Backup script started')
    run_backup_periodically(SOURCE_DIR, DEST_DIR, BACKUP_INTERVAL)
