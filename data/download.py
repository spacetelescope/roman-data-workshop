import shutil
from pathlib import Path
import requests



from astropy.utils.data import download_file

REMOTE_URL = "https://data.science.stsci.edu/redirect/Roman/Roman_Data_Workshop/"
REMOTE_PATHS = [
    "ExampleData/Build14/r0000101001001001001_01101_0001_WFI01_uncal.asdf",
    "ExampleData/Build14/r0000101001001001001_01101_0001_WFI01_cal.asdf",
    "ExampleData/Build14/r0000101001001001001_01101_0001_WFI16_uncal.asdf",
    "ExampleData/Build14/r0000101001001001001_01101_0001_WFI16_cal.asdf",
    "ExampleData/Build14/r0000201001001001001_01101_0001_WFI01_cal.asdf",
    "ExampleData/Build14/r0099101001001001001_r274dp63x31y81_visit_F158_prompt_i2d.asdf",
    "ExampleData/Build14/r0099101001001001001_r274dp63x31y81_visit_F158_prompt_cat.asdf",
    "ExampleData/Build14/r0099101001001001001_r274dp63x31y81_visit_F158_prompt_segm.asdf",
    "ExampleData/jw01448013001_02105_00001_nis_rate.fits",
    "ExampleData/jw01448013001_02106_00001_nis_rate.fits",
    "ExampleData/jw01448013001_02106_00001_nis_cat.ecsv",
    "ExampleData/jwst_niriss_distortion_0013.asdf",
    "ExampleData/jwst_niriss_filteroffset_0002.asdf",
    "ExampleData/jwst_niriss_specwcs_0018.asdf",
    "ExampleData/jwst_niriss_wavelengthrange_0002.asdf",
]
LOCAL_DIRECTORY = Path(__file__).parent
WEBBPSF_DATA = Path('./data')/'Webbpsf-data-LATEST.tar.gz'


def download_data(overwrite: bool = False):
    for remote_path in REMOTE_PATHS:
        local_path = LOCAL_DIRECTORY / Path(remote_path).name
        if overwrite or not local_path.exists():
            print(f'downloading "{remote_path}"')
            filename = download_file(REMOTE_URL + remote_path)
            shutil.move(filename, local_path)

    response = requests.get('https://stsci.box.com/shared/static/qxpiaxsjwo15ml6m4pkhtk36c9jgj70k.gz')

    with open(WEBBPSF_DATA, 'wb') as f:
        f.write(response.content)

    print("Done downloading files")

if __name__ == "__main__":
    download_data()
    shutil.unpack_archive(WEBBPSF_DATA, Path('./data'))
