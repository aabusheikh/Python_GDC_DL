import os
import errno

"""
Common code (global variables, functions) that will be used by multiple modules of this program
for configuration or functionality
"""

# GDC API base URL
BASE_URL = 'https://api.gdc.cancer.gov/'

# basic HTTP request header
HEADERS = {
    'Content-Type': 'application/json'
}

# total RNA, miRNA files to request
TOTAL_RNA, TOTAL_MIRNA = 12000, 12000

# max files per json list
FILES_PER_LIST = 500

# manifest file request query files directory
FILE_LIST_REQ_DIR = os.path.join('json','file-list_req')

# manifest request query file name template
FILE_LIST_REQ_NAME = '%s-seq.json'

# file-list JSON files directory
FILE_LIST_DIR = os.path.join('json','file-list')

# file manifest list file name template
FILE_LIST_NAME = '%s-seq_%s.json'

# absolute directory path to download files to (recommended if project is stored in space-sensitive
# location such as a cloud drive directory (Dropbox, OneDrive, etc...)
ABS_DL_DIR = os.path.abspath(os.path.join(os.path.expanduser('~'), 'Downloads', 'GDC_Downloads'))

# relative directory path to download files to
REL_DL_DIR = 'GDC_Downloads'

# chosen downloads directory
DL_DIR = ABS_DL_DIR


def make_dir(directory):
    """

    :param directory:
    :return:
    """
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
