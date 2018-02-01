import os
import errno

"""
Common code (global variables, functions) that will be used by multiple modules of this program
for configuration or functionality
"""

# GDC API files endpoint URL
BASE_URL = 'https://api.gdc.cancer.gov/'

# basic HTTP request header
HEADERS = {
    'Content-Type': 'application/json'
}

# total RNA, miRNA files to request
TOTAL_RNA, TOTAL_MIRNA = 35000, 25000

# max files per json list
FILES_PER_LIST = 500

# file-list JSON files directory
FILE_LIST_DIR = 'json/file-list/'

# absolute directory path to download files to (recommended if project is stored in space-sensitive
# location such as a cloud drive directory (Dropbox, OneDrive, etc...)
ABS_DL_DIR = os.path.abspath(os.path.join(os.path.expanduser('~'), 'Downloads', 'GDC_Downloads'))

# relative directory path to download files to
REL_DL_DIR = 'GDC_Downloads/'

# chosen downloads directory
DL_DIR = ABS_DL_DIR


def make_dir(directory):
    if not os.path.exists(directory):
        print("Creating directory '%s' ..." % directory)
        try:
            os.makedirs(directory)
            print("Directory '%s' created \n" % directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                print("Failed to create directory '%s'! \n" % directory)
                raise
            else:
                print("Directory '%s' already exists \n" % directory)
    else:
        print("Directory '%s' already exists \n" % directory)
