import shutil
from pathlib import Path

from astropy.utils.data import download_file

REMOTE_URL = 'https://data.science.stsci.edu/redirect/Roman/Roman_Data_Workshop/'
REMOTE_PATHS = [
    'ExampleData/r0000101001001001001_01101_0001_WFI01_uncal.asdf',
    'ExampleData/r0000101001001001001_01101_0001_WFI01_cal.asdf',
]

LOCAL_DIRECTORY = Path(__file__).parent


def download_data():
    for remote_path in REMOTE_PATHS:
        print(f'downloading "{remote_path}"')
        filename = download_file(REMOTE_URL + remote_path)
        shutil.move(filename, LOCAL_DIRECTORY / Path(remote_path).name)

    print("Done downloading files")


if __name__ == '__main__':
    download_data()
