import zipfile
import os
from os.path import isfile, join
from os import listdir

input_zip_dir = 'event_files'
temp_unzip_dir = 'unzip_temp'
extension = '.zip'


print os.path.abspath(input_zip_dir)
for item in listdir(input_zip_dir):
    if item.endswith(extension):
        print 'Extracting file %s ' % item
        file_to_extract = os.path.abspath(item)
        print join(os.path.abspath(input_zip_dir), item)
        zipFile_to_extract = zipfile.ZipFile(join(os.path.abspath(input_zip_dir), item))
        if not os.path.exists(temp_unzip_dir):
            os.makedirs(temp_unzip_dir)
        zipFile_to_extract.extractall(temp_unzip_dir)
        zipFile_to_extract.close()
