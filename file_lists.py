import requests
import json
import os
import common as cmn
import logging

"""
A script to generate a list of GDC RNA-seq or miRNA-seq file manifests to be used 
later by the accompanying files.py to request and download the actual files
"""

# GDC API files endpoint URL
URL = cmn.BASE_URL+'files'


def gen_file_list(req_type, from_param=0):
    """
    Generate a list of GDC file manifests for RNA-seq or miRNA-seq in a JSON file using an HTTP
    POST request with parameters from the req.json files and provided 'from' param.

    :param req_type: String 'RNA' or 'miRNA'.
    :param from_param: Number start index for requested files
    """

    # open the manifest request query parameters JSON file as an object
    params = json.load(open(os.path.join(cmn.FILE_LIST_REQ_DIR, cmn.FILE_LIST_REQ_NAME % req_type), 'rb'))
    # set "pagination" parameters
    params["size"] = str(cmn.FILES_PER_LIST)
    params["from"] = str(from_param)

    logging.info("Requesting manifests for files %(start)s to %(end)s (index+1) ..." % {
        "start": from_param+1,
        "end": from_param+cmn.FILES_PER_LIST
    })

    # send HTTP POST request and print HTTP status code returned (200, 404, etc...)
    r = requests.post(URL, data=json.dumps(params), headers=cmn.HEADERS)
    logging.info(r)

    if r.status_code == requests.codes.ok:
        # set path for manifest list JSON file
        file_path = os.path.join(cmn.FILE_LIST_DIR, cmn.FILE_LIST_NAME % (req_type, from_param//cmn.FILES_PER_LIST))

        logging.info("Writing manifest list to %s ..." % file_path)
        # write JSON manifests from HTTP response to the file
        with open(file_path, 'w') as f:
            f.write(r.text)
        logging.info("List written to file.\n")
    else:
        logging.error("Request failed, skipping file.\n")


def gen_file_lists(req_type):
    """
    Generate the manifest-lists of GDC files for RNA-seq or miRNA-seq using
    the gen_file_list method iteratively.

    :param req_type: String 'RNA' or 'miRNA'.
    """
    '''
    Calls gen_file_list n times. n is based on the total number of manifests
    or files to be downloaded and the desired number of manifests per list file.
    '''
    n = 0
    if req_type == "RNA":
        n = cmn.TOTAL_RNA // cmn.FILES_PER_LIST
    elif req_type == "miRNA":
        n = cmn.TOTAL_MIRNA // cmn.FILES_PER_LIST
    else:
        return

    logging.info("Generating %s manifest lists to '%s' ... \n" % (req_type, cmn.FILE_LIST_DIR))

    '''
    Each call to the helper method passes the file index to start at when sending
    the request. This is calculated using the current index of the manifest list
    file and then umber of files/manifests per list.
    '''
    for i in range(n):
        logging.info("Generating manifest list %(i)s of %(n)s ..." % {"i": i + 1, "n": n})
        try:
            gen_file_list(req_type, i * cmn.FILES_PER_LIST)
        except TypeError:
            logging.error("genFileList - invalid parameter types\n")

    logging.info("%s manifest lists generated\n" % req_type)

    return n


def run():
    """
    Run the file manifest-list files generating stage
    """
    # create required directory
    cmn.make_dir(cmn.FILE_LIST_DIR)

    # generate RNA file lists
    n_rna = gen_file_lists("RNA")

    # generate miRNA file lists
    n_mirna = gen_file_lists("miRNA")

    logging.info("manifest list files generated in '%s' :" % cmn.FILE_LIST_DIR)
    logging.info("%s RNA-seq manifest lists generated, with %s manifests in each list." % (n_rna, cmn.FILES_PER_LIST))
    logging.info("%s miRNA-seq manifest lists generated, with %s manifests in each list.\n" % (n_mirna, cmn.FILES_PER_LIST))
