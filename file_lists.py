import requests
import json
import common as cmn

"""
A script to generate a list of GDC RNA-seq or miRNA-seq files to be downloaded 
later using the accompanying Files.py
"""

# GDC API files endpoint URL
URL = cmn.BASE_URL+'files'


def make_dirs():
    """
    Create the directories needed by this script

    :return:
    """
    cmn.make_dir(cmn.FILE_LIST_DIR)


def gen_file_list(req_type, from_param=0):
    """
    Generate a list of GDC files for RNA-seq or miRNA-seq in a JSON file from an HTTP
    POST request with parameters from the req.json files and provided 'from' param.

    :param req_type: String 'RNA' or 'miRNA'.
    :param from_param: Number start index for requested files
    :return:
    """

    params = json.load(open("json/file-list_req/%s-seq.json" % req_type, 'rb'))
    params["size"] = str(cmn.FILES_PER_LIST)
    params["from"] = str(from_param)

    print("Requesting information for files %(start)s to %(end)s (index+1) ..." % {
        "start": from_param+1,
        "end": from_param+cmn.FILES_PER_LIST
    })

    r = requests.post(URL, data=json.dumps(params), headers=cmn.HEADERS)
    print(r)

    fpath = "%(dir)s%(req)s-seq_%(num)s.json" % {
        "dir": cmn.FILE_LIST_DIR,
        "req": req_type,
        "num": from_param//cmn.FILES_PER_LIST
    }

    print("Writing list to %s ..." % fpath)
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

    print("\nGenerating %s files lists to '%s' ... " % (req_type, cmn.FILE_LIST_DIR))

    for i in range(n):
        print("\nGenerating file list %(i)s of %(n)s ..." % {"i": i + 1, "n": n})
        try:
            gen_file_list(req_type, i * cmn.FILES_PER_LIST)
        except TypeError:
            print("ERROR: genFileList - invalid parameter types")

    print("\n%s file lists generated" % req_type)

    return n


def main():
    # generate required directories
    make_dirs()

    # generate RNA file lists
    n_rna = gen_file_lists("RNA")

    # generate miRNA file lists
    n_mirna = gen_file_lists("miRNA")

    print()
    print(n_rna, "RNA file lists generated, with information on", cmn.FILES_PER_LIST, "files in each list.\n")
    print(n_mirna, "miRNA file lists generated, with information on", cmn.FILES_PER_LIST, "files in each list.\n")


if __name__ == "__main__":
    main()
