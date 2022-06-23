import os.path
import shutil
import data
from astropy.utils.data import download_file


data_dir = data.__path__[0]

def download_data():
    box_path = 'https://data.science.stsci.edu/redirect/Roman/Roman_Data_Workshop/'
    l1_file = download_file(box_path + "ExampleData/r0000101001001001001_01101_0001_WFI01_uncal.asdf")

    l2_file = download_file(box_path + "ExampleData/r0000101001001001001_01101_0001_WFI01_cal.asdf")

    shutil.copyfile(l1_file, os.path.join(data_dir, "r0000101001001001001_01101_0001_WFI01_uncal.asdf"))
    shutil.copyfile(l2_file, os.path.join(data_dir, "r0000101001001001001_01101_0001_WFI01_cal.asdf"))
    print("Done downloading files")

