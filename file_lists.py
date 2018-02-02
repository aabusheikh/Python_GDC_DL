import requests
import json
import os
import common as cmn

"""
A script to generate a list of GDC RNA-seq or miRNA-seq file manifests to be used 
later by the accompanying Files.py to download the actual files
"""

# GDC API files endpoint URL
URL = cmn.BASE_URL+'files'


def gen_file_list(req_type, from_param=0):
    """
    Generate a list of GDC files for RNA-seq or miRNA-seq in a JSON file from an HTTP
    POST request with parameters from the req.json files and provided 'from' param.

    :param req_type: String 'RNA' or 'miRNA'.
    :param from_param: Number start index for requested files
    :return:
    """

    params = json.load(open(os.path.join(cmn.FILE_LIST_REQ_DIR, cmn.FILE_LIST_REQ_NAME % req_type), 'rb'))
    params["size"] = str(cmn.FILES_PER_LIST)
    params["from"] = str(from_param)

    print("Requesting manifests for files %(start)s to %(end)s (index+1) ..." % {
        "start": from_param+1,
        "end": from_param+cmn.FILES_PER_LIST
    })

    r = requests.post(URL, data=json.dumps(params), headers=cmn.HEADERS)
    print(r)

    fpath = os.path.join(cmn.FILE_LIST_DIR, cmn.FILE_LIST_NAME % (req_type, from_param//cmn.FILES_PER_LIST))

    print("Writing manifest list to %s ..." % fpath)
    with open(fpath, 'w') as f:
        f.write(r.text)
    print("List written to file.")


def gen_file_lists(req_type):
    """
    Generate the lists of GDC files for RNA-seq or miRNA-seq using genFileList method

    :param req_type: String 'RNA' or 'miRNA'.
    :return:
    """

    n = 0
    if req_type == "RNA":
        n = cmn.TOTAL_RNA // cmn.FILES_PER_LIST
    elif req_type == "miRNA":
        n = cmn.TOTAL_MIRNA // cmn.FILES_PER_LIST

    print("\nGenerating %s manifest lists to '%s' ... " % (req_type, cmn.FILE_LIST_DIR))

    for i in range(n):
        print("\nGenerating manifest list %(i)s of %(n)s ..." % {"i": i + 1, "n": n})
        try:
            gen_file_list(req_type, i * cmn.FILES_PER_LIST)
        except TypeError:
            print("ERROR: genFileList - invalid parameter types")

    print("\n%s manifest lists generated" % req_type)

    return n


def run():
    # create required directory
    cmn.make_dir(cmn.FILE_LIST_DIR)

    # generate RNA file lists
    n_rna = gen_file_lists("RNA")

    # generate miRNA file lists
    n_mirna = gen_file_lists("miRNA")

    print("\nmanifest list files generated in '%s' :" % cmn.FILE_LIST_DIR)
    print(n_rna, "RNA-seq manifest lists generated, with", cmn.FILES_PER_LIST, "manifests in each list.")
    print(n_mirna, "miRNA-seq manifest lists generated, with ", cmn.FILES_PER_LIST, "manifests in each list.\n")
