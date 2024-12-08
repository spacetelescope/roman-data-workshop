import shutil
from pathlib import Path
import requests



from astropy.utils.data import download_file

REMOTE_URL = "https://data.science.stsci.edu/redirect/Roman/Roman_Data_Workshop/"
REMOTE_PATHS = [
    "ExampleData/Build16/r0000101001001001001_0001_wfi01_uncal.asdf",
    "ExampleData/Build16/r0000101001001001001_0001_wfi01_cal.asdf",
    "ExampleData/Build16/r0000201001001001001_0003_wfi12_uncal.asdf",
    "ExampleData/Build16/r0000201001001001001_0003_wfi12_cal.asdf",
    "ExampleData/Build16/r0000301001001001001_0001_wfi14_uncal.asdf",
    "ExampleData/Build16/r0000301001001001001_0001_wfi14_cal.asdf",
    "ExampleData/Build16/r00001_p_v01001001001_r274dp63x31y80_f158_coadd_cat.asdf",
    "ExampleData/Build16/r00001_p_v01001001001_r274dp63x31y80_f158_coadd_segm.asdf",
    "ExampleData/Build16/r00001_p_v01001001001_r274dp63x31y80_f158_coadd_i2d.asdf",
    "ExampleData/Build16/new_distortion.asdf",
    "ExampleData/Build16/skycell_wcs.asdf",
    "ExampleData/Build16/r00001_p_v01001001001_r274dp63x31y80_f158_coadd_asn.json",
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
