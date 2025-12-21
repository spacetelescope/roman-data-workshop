import shutil
from pathlib import Path
import requests



from astropy.utils.data import download_file

REMOTE_URL = "https://data.science.stsci.edu/redirect/Roman/Roman_Data_Workshop/"
REMOTE_PATHS = [
    "ExampleData/Build20/r0000101001001001001_0001_wfi01_f158_uncal.asdf",
    "ExampleData/Build20/r0000101001001001001_0001_wfi01_f158_cal.asdf",
    "ExampleData/Build20/r0000101001001001001_0001_wfi01_f158_cat.parquet",
    "ExampleData/Build20/r0000101001001001001_0001_wfi01_f158_wcs.asdf",
    "ExampleData/Build20/r0000101001001001001_0001_wfi01_f158_segm.asdf",
    
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x69y48_f158_asn.json",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x69y49_f158_asn.json",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x69y50_f158_asn.json",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x70y48_f158_asn.json",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x70y49_f158_asn.json",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x70y50_f158_asn.json",
    
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x69y48_f158_coadd.asdf",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x69y49_f158_coadd.asdf",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x69y50_f158_coadd.asdf",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x70y48_f158_coadd.asdf",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x70y49_f158_coadd.asdf",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x70y50_f158_coadd.asdf",
    
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x69y48_f158_cat.parquet",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x69y49_f158_cat.parquet",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x69y50_f158_cat.parquet",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x70y48_f158_cat.parquet",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x70y49_f158_cat.parquet",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x70y50_f158_cat.parquet",
    
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x69y48_f158_segm.asdf",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x69y49_f158_segm.asdf",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x69y50_f158_segm.asdf",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x70y48_f158_segm.asdf",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x70y49_f158_segm.asdf",
    "ExampleData/Build20/r00001_p_v01001001001001_270p65x70y50_f158_segm.asdf",
    
    "ExampleData/Build20/r0000201001001001001_0001_wfi01_grism_uncal.asdf",
    "ExampleData/Build20/r0000201001001001001_0001_wfi01_grism_cal.asdf",
    "ExampleData/Build20/r0000201001001001001_0001_wfi01_grism_wcs.asdf",
    
    "ExampleData/Build20/r0000301001001001001_0001_wfi01_prism_uncal.asdf",
    "ExampleData/Build20/r0000301001001001001_0001_wfi01_prism_cal.asdf",
    "ExampleData/Build20/r0000301001001001001_0001_wfi01_prism_wcs.asdf",
    
    "ExampleData/Build16/new_distortion.asdf",
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
