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

DATA_DIR = "data/raw"
IMAGES_DIR = "images/0"
COMMAND = [
    "kaggle",
    "competitions",
    "download",
    "-c",
    "h-and-m-personalized-fashion-recommendations",
    "-f",
    "FILE",
    "-p",
    "DIR",
]
meta_files = [
    "articles.csv",
    "customers.csv",
    "sample_submission.csv",
    "transactions_train.csv",
]
images_files_dir = list(range(10, 96))


def check_storage(project = os.getcwd()):
    """_summary_

    Parameters
    ----------
    directory_path : _type_
        _description_

    Returns
    -------
    _type_
        _description_

    Raises
    ------
    StorageFullError
        _description_
    """
    total, used, free = shutil.disk_usage(project)
    total_size_gb = round(total / (2**30), 2)
    used_size_gb = round(used / (2**30), 2)
    free_size_gb = round(free / (2**30), 2)
    if used_size_gb / total_size_gb >= 0.8:
        raise StorageFullError
    else:
        return free_size_gb


def download_dataset_(cmd, file, dire):
    """_summary_

    Parameters
    ----------
    cmd : _type_
        _description_
    file : _type_
        _description_
    dir : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """

    _ = subprocess.run(cmd, check=True, capture_output=True, text=True)
    unzipped_file_path = dire + "/" + file + ".zip"
    if (
        os.path.exists(unzipped_file_path)
        and os.path.splitext(unzipped_file_path)[1].lower() == ".zip"
    ):
        with ZipFile(unzipped_file_path, "r") as unzipped_file:
            unzipped_file.extract(dire)
        os.remove(unzipped_file_path)
    return True


def download_loop(file_array, main_dir, images_dw=False):
    """_summary_

    Parameters
    ----------
    file_array : _type_
        _description_
    main_dir : _type_
        _description_
    images_dw : bool, optional
        _description_, by default False

    Raises
    ------
    DownloadFailedError
        _description_
    """
    directory_path = main_dir
    for file_name in file_array:
        if images_dw:
            check_storage()
            file_name = IMAGES_DIR + file_name
            directory_path = main_dir + "/" + file_name
        logger.info(f"Downloading {file_name} in {directory_path}")
        COMMAND[6] = file_name
        COMMAND[-1] = directory_path
        re = download_dataset_(cmd=COMMAND, file=file_name, dire=directory_path)
        if not re:
            raise DownloadFailedError
        logger.info(f"{file_name} has been downloaded")


class StorageFullError(Exception):
    """Custom exception for when storage is full."""

    pass


class DownloadFailedError(Exception):
    """Custom exception for failed downloads."""

    pass


def main():
    """main function to run the script"""
    logger.info(f"Commencing downloading the dataset into {DATA_DIR}")
    try:
        if not os.path.isdir(DATA_DIR):
            os.makedirs(DATA_DIR)
        logger.info(f"{check_storage()}")
        download_loop(meta_files, DATA_DIR)
        logger.success(f"Downloaded metadata into {DATA_DIR}")
        logger.info(f"{check_storage()}")
        logger.info("Downloading images datasets")
        download_loop(images_files_dir, DATA_DIR, images_dw=True)
        logger.success(f"Dataset downloaded to {DATA_DIR} successfully.")
    except DownloadFailedError as error:
        logger.error(f"Dataset download failed due to: {error}")


if __name__ == "__main__":
    main()
