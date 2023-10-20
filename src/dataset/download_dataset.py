"""Dataset Download Module

This module provides functions to download datasets from a HMG dataset.

Functions:
- download_dataset(url: str, destination: str) -> bool:
  Downloads a dataset from the given URL to the specified destination directory.
- main - the main function to run the script
"""
# TODO clean up code

import os
import shutil
from zipfile import ZipFile
import subprocess
from loguru import logger


DATA_DIR = 'data/raw'
COMMAND = [
    "kaggle",
    "competitions",
    "download",
    "-c","h-and-m-personalized-fashion-recommendations","-f", "FILE", "-p", "DATA_DIR",]
meta_files = ["articles.csv","customers.csv","sample_submission.csv","transactions_train.csv"]
images_dir = list(range(10,96))


def check_storage(dir):
    total, used, free = shutil.disk_usage(dir)
    total_size_gb = round(total/(2**30), 2)
    used_size_gb = round(used/(2**30), 2)
    free_size_gb = round(free/(2**30), 2)

    return

def download_dataset_(cmd, file):
    """
    """
    result = subprocess.run(cmd, check= True, capture_output= True, text= True)
    unzipped_file_path = DATA_DIR + file + ".zip"
    if (
        os.path.exists(unzipped_file_path)
        and os.path.splitext(unzipped_file_path)[1].lower() == ".zip"
    ):
        with ZipFile(unzipped_file_path, 'r') as unzipped_file:
            unzipped_file.extract(DATA_DIR)
        os.remove(unzipped_file_path)
        return True

def main():
    """main function to run the script
    """
    logger.info(f"Commencing downloading the dataset into {DATA_DIR}")
    try:
        if not os.path.isdir(DATA_DIR):
            os.makedirs(DATA_DIR)
        # TODO check storage and plan for error
        loop(meta_files)
        # TODO check storage and plan for error
        for 
        logger.success(f"Dataset downloaded to {DATA_DIR} successfully.")
    except DownloadFailedError as error:
        logger.error(f"Dataset download failed due to: {error}")

def loop(file_array):
    for file_name in file_array:
        logger.info(f"Downloading {file_name} in {DATA_DIR}")
        COMMAND[6] = file_name
        re = download_dataset_(cmd= COMMAND, file = file_name)
        if not re:
            raise DownloadFailedError
        logger.info(f"{file_name} has been downloaded")

class StorageFullError(Exception):
    """Custom exception for when storage is full."""
    pass

class DownloadFailedError(Exception):
    """Custom exception for failed downloads."""
    pass
if __name__ == "__main__":
    main()
