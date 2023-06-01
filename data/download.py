import shutil
from pathlib import Path

from astropy.utils.data import download_file

REMOTE_URL = "https://data.science.stsci.edu/redirect/Roman/Roman_Data_Workshop/"
REMOTE_PATHS = [
    "OldData/roman_wfi_dark_0427.asdf",
    "OldData/roman_wfi_linearity_0179.asdf",
    "OldData/roman_wfi_saturation_0193.asdf",
    "OldData/roman_wfi_flat_0227.asdf",
    "OldData/roman_wfi_readnoise_0368.asdf",
    "OldData/roman_wfi_gain_0169.asdf",
    "OldData/roman_wfi_mask_0074.asdf",
    "OldData/roman_wfi_photom_0056.asdf",
    "OldData/roman_wfi_distortion_0008.asdf",
    "OldData/r0000101001001001001_01101_0001_WFI01_uncal.asdf",
    "OldData/r0000101001001001001_01101_0001_WFI01_cal.asdf",
    "OldData/jw01448013001_02105_00001_nis_rate.fits",
    "OldData/jw01448013001_02106_00001_nis_rate.fits",
    "OldData/jw01448013001_02106_00001_nis_cat.ecsv",
    "OldData/jwst_niriss_distortion_0013.asdf",
    "OldData/jwst_niriss_filteroffset_0002.asdf",
    "OldData/jwst_niriss_specwcs_0018.asdf",
    "OldData/jwst_niriss_wavelengthrange_0002.asdf",
]
LOCAL_DIRECTORY = Path(__file__).parent


def download_data(overwrite: bool = False):
    for remote_path in REMOTE_PATHS:
        local_path = LOCAL_DIRECTORY / Path(remote_path).name
        if overwrite or not local_path.exists():
            url = REMOTE_URL + remote_path
            print(f'downloading "{url}"')
            filename = download_file(url)
            shutil.move(filename, local_path)

    print("Done downloading files")


if __name__ == "__main__":
    download_data()
