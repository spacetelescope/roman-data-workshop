import shutil
from pathlib import Path

from astropy.utils.data import download_file

REMOTE_URL = "https://data.science.stsci.edu/redirect/Roman/Roman_Data_Workshop/"
REMOTE_PATHS = [
    "ExampleData/roman_wfi_dark_0549.asdf",
    "ExampleData/roman_wfi_linearity_0215.asdf",
    "ExampleData/roman_wfi_saturation_0229.asdf",
    "ExampleData/roman_wfi_flat_0227.asdf",
    "ExampleData/roman_wfi_readnoise_0440.asdf",
    "ExampleData/roman_wfi_gain_0205.asdf",
    "ExampleData/roman_wfi_mask_0074.asdf",
    "ExampleData/roman_wfi_photom_0056.asdf",
    "ExampleData/roman_wfi_distortion_0054.asdf",
    "ExampleData/r0000101001001001001_01101_0001_WFI01_uncal.asdf",
    "ExampleData/r0000101001001001001_01101_0001_WFI01_cal.asdf",
    "ExampleData/jw01448013001_02105_00001_nis_rate.fits",
    "ExampleData/jw01448013001_02106_00001_nis_rate.fits",
    "ExampleData/jw01448013001_02106_00001_nis_cat.ecsv",
    "ExampleData/jwst_niriss_distortion_0013.asdf",
    "ExampleData/jwst_niriss_filteroffset_0002.asdf",
    "ExampleData/jwst_niriss_specwcs_0018.asdf",
    "ExampleData/jwst_niriss_wavelengthrange_0002.asdf",
]
LOCAL_DIRECTORY = Path(__file__).parent


def download_data(overwrite: bool = False):
    for remote_path in REMOTE_PATHS:
        local_path = LOCAL_DIRECTORY / Path(remote_path).name
        if overwrite or not local_path.exists():
            print(f'downloading "{remote_path}"')
            filename = download_file(REMOTE_URL + remote_path)
            shutil.move(filename, local_path)

    print("Done downloading files")


if __name__ == "__main__":
    download_data()
