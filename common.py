import os
import errno

"""
Common code that will be used by multiple modules of this program
"""


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
