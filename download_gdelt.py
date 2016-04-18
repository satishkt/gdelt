import urllib
import os
from os import listdir
from os.path import isfile, join

event_files_url = 'http://data.gdeltproject.org/events/index.html'

skip_file = 'GDELT.MASTERREDUCEDV2.1979-2013.zip'

"""
GDelt object just stores
    url=http://data.gdeltproject.org/events/index.html
    base_url=http://data.gdeltproject.org/events
    base_dir=directory where the script is stored
    download_dir=basedir + "event_files"

    two lists:
    downloaded_files = extract the list of files existing in download_dir
    new_files = filenames extracted from url and not in downloaded_files

gdelt object on created will store urls and dirs
gdelt object should call get_downloaded_files first and then get_new_files
finally should call download_new_files
TODO: to verify the sizes before ignoring to add to newfiles list

"""


class gdelt(object):
    def __init__(self, event_files_url):
        self.event_files_url = event_files_url
        self.base_url, self.event_file = os.path.split(event_files_url)
        self.base_dir = os.path.dirname(os.path.realpath(__file__))
        self.download_dir = join(self.base_dir, "event_files")
        self.downloaded_files = []
        self.new_files = []

    def show_downloaded_files(self):
        for file in self.downloaded_files:
            print file

    def show_new_files(self):
        for file in self.new_files:
            print file

    def get_downloaded_files_list(self):
        self.downloaded_files = [file for file in listdir(self.download_dir) if isfile(join(self.download_dir, file))]

    def get_new_files_list(self):
        urllib.urlretrieve(self.event_files_url, self.event_file)
        infile = open(self.event_file, 'r')
        line = infile.readline()
        while line:
            split_list = line.split('"')
            for word in line.split('"'):
                # TODO to change the condition to check the size of downloaded file and remote file
                if split_list.index(word) == 1 and ".zip" in word and word not in self.downloaded_files:
                    self.new_files.append(word)
            line = infile.readline()

    def download_new_files(self):
        for file in self.new_files:
            if file == skip_file:
                print file
                urllib.urlretrieve(join(self.base_url, file), join(self.download_dir, file))


# gdeltobj = gdelt(event_files_url).get_event_page()
gdeltobj = gdelt(event_files_url)
print "=======   Created gdeltobj   =============="
gdeltobj.get_downloaded_files_list()
print "=======   Downloaded Files list ==========="
# gdeltobj.show_downloaded_files()
print "=======   Get Fresh Page    ==============="
gdeltobj.get_new_files_list()
print "=======   New Files list   ================"
# gdeltobj.show_new_files()
print "=======   Download New Files   ================"
gdeltobj.download_new_files()
