import common as cmn
import files
import file_lists
import os
import logging
import time
import sys

"""
main module, program will be run through this module
"""


def main():
    """
    Run program
    """
    cmn.make_dir(cmn.LOG_DIR)
    logging.basicConfig(
        # filename=os.path.join(cmn.LOG_DIR, cmn.LOG_FILE_NAME % time.strftime(cmn.LOG_FILE_NAME_TIME)),
        handlers=[
            logging.FileHandler(os.path.join(cmn.LOG_DIR, cmn.LOG_FILE_NAME % time.strftime(cmn.LOG_FILE_NAME_TIME))),
            logging.StreamHandler()
        ],
        level=cmn.LOG_LEVEL,
        format=cmn.LOG_MSG_FORMAT,
        datefmt=cmn.LOG_TIME_FORMAT
    )
    logging
    logging.info("\nStarting program ...\n")

    if "-man" in sys.argv:
        logging.info("Detected 'manifest only' command line argument, program will only generate file manifests.")
        file_lists.run()
    elif "-dlo" in sys.argv:
        logging.info("Detected 'download only' command line argument, program will use existing manifest lists.")
        files.run()
    else:
        logging.warning("No valid command line arguments, program will ignore arguments.")
        file_lists.run()
        files.run()

    logging.info("\nFinished running program.\n")


if __name__ == "__main__":
    main()
