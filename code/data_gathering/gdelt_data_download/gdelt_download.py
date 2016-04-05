import datetime
from datetime import date
import os
import urllib

base_url = 'http://data.gdeltproject.org/events/'


def next_date(start_month=03, start_year=2016, start_date=25):
    next_day = datetime.timedelta(days=1)
    date = datetime.date(start_year, start_month, start_date)
    next_date = date + next_day
    return next_date


def build_url(date):
    yr = str(date.year)
    mon = date.strftime('%m')
    day = date.strftime('%d')
    file_name = yr + mon + day + ".export.CSV.zip"
    return (file_name, base_url + file_name)


##TODO 1. Make the code take parameters for start date and end date
##TODO 2. Create the folders locally if they do not exist.
##TODO 3. Can we run this on AWS and populate the zip files on S3
##TODO 4. Can we download the zip files, unzip them and upload them into our S3 buckets.
##TODO 5. Exception handling for connections errors, retries, and any other issues.
##TODO 6. Build a proper build and a package structure around this so that we can invoke this from command line with options and the script knows what to do.
##TODO 7. Write unit tests/integration tests.
##TODO 8. How to keep track of files that are already downloaded, database

if __name__ == '__main__':
    end_date = date.today()
    start_date = next_date(start_date=23)
    while (start_date <= end_date):
        filename_url = build_url(start_date)
        print filename_url[0]
        if (os.path.exists(filename_url[0]) == False):
            ## Need to handle exceptions where the file does not exist and log them appropriately
            urllib.urlretrieve(filename_url[1], filename_url[0])
            start_date = next_date(start_year=start_date.year, start_date=start_date.day, start_month=start_date.month)
