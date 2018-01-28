import requests
import json

"""
A script to generate a list of GDC RNA-seq or miRNA-seq files to be downloaded 
later using the accompanying Files.py
"""

# GDC API files endpoint URL
URL = 'https://api.gdc.cancer.gov/files'

# basic HTTP request header
HEADERS = {
    'Content-Type': 'application/json'
}

# total RNA, miRNA files to request
TOTAL_RNA, TOTAL_MIRNA = 35000, 25000

# max files per json list
FILES_PER_LIST = 500

# file list directory
FILE_LIST_DIR = 'json/file-list/'


def genFileList(reqType, fromParam=0):
    """
    Generate a list of GDC files for RNA-seq or miRNA-seq in a JSON file from an HTTP
    POST request with parameters from the req.json files and provided 'from' param.

    :param reqType: String 'RNA' or 'miRNA'.
    :param fromParam: Number start index for requested files
    :return:
    """
    if reqType != "RNA" and reqType != "miRNA":
        print("genFileList: reqType has to be 'RNA' or 'miRNA', terminating...")
        return

    params = json.load(open("json/file-list_req/%s-seq.json" % reqType, 'rb'))
    params["size"] = str(FILES_PER_LIST)
    params["from"] = str(fromParam)

    print("Requesting information for files %(start)s to %(end)s (index+1) ..." % {
        "start": int(fromParam)+1,
        "end": int(fromParam)+FILES_PER_LIST
    })
    r = requests.post(URL, data=json.dumps(params), headers=HEADERS)
    print(r)

    fpath = "%(dir)s%(req)s-seq_%(num)s.json" % {
        "dir": FILE_LIST_DIR,
        "req": reqType,
        "num": int(fromParam)//FILES_PER_LIST
    }
    print("Writing list to %s ..." % fpath)
    f = open(fpath, 'w')
    f.write(r.text)
    print("List written to file.")


# generate RNA file lists
n = TOTAL_RNA // FILES_PER_LIST
print("\nGenerating RNA files lists to '%s' ... " % FILE_LIST_DIR)
for i in range(n):
    print("\nGenerating file list %(i)s of %(n)s ..." % {
        "i": i+1,
        "n": n
    })
    genFileList("RNA", i*FILES_PER_LIST)
print("\nRNA file lists generated")

# generate miRNA file lists
m = TOTAL_MIRNA // FILES_PER_LIST
print("\nGenerating miRNA files lists to '%s' ... " % FILE_LIST_DIR)
for i in range(m):
    print("\nGenerating file list %(i)s of %(n)s ..." % {
        "i": i+1,
        "n": m
    })
    genFileList("miRNA", i * FILES_PER_LIST)
print("\nmiRNA file lists generated")

print()
print(n, "RNA file lists generated, with information on", FILES_PER_LIST, "files in each list.\n")
print(m, "miRNA file lists generated, with information on", FILES_PER_LIST, "files in each list.\n")
