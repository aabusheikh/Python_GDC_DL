# Python_GDC_DL

Created for CSI4900 - Honours Project

Python script that will request RNA-seq and miRNA-seq files from the GDC server

GDC search and retieval API documentation: https://docs.gdc.cancer.gov/API/Users_Guide/Search_and_Retrieval/

Also created a script to combine/integrate data files: https://github.com/bbpgrs/Python_GDC_Integration

___

##### Python 3 is required, Python 3.6 or higher strongly recommended (not tested with older versions).

https://www.python.org/downloads/release

Running this program through the command line is recommended as IDEs may need extra configuration.

#### Run program:

Windows (Python 3 installed)

> python main.py

Linux/MacOS

> python3 main.py

#### Commandline arguments:

Only generate file manifest lists (download files later)

> python main.py -man

Only download files (use previously generated manifest lists)

> python main.py -dlo

    If both arguments are provided '-man' will be used.

___

##### This program requires the 'requests' library: http://docs.python-requests.org/en/latest/user/install/

### To install the 'requests' library:


#### Windows: 


Check for pip updates

> python -m pip install --upgrade pip


Install pipenv

> python -m pip install pipenv


Install requests

> python -m pipenv install requests


#### Mac OS:

Same commands as above, but use 'python3' instead, 

OR (not tested):


    Install Python 3: http://docs.python-guide.org/en/latest/starting/install3/osx/ 

    Installing Python 3 using Homebrew as described in the guide will also install pip3.

    Then:

    > pip3 install pipenv

    > pipenv install requests


#### Linux:

Same commands as above (Windows), but use 'python3' instead, 

OR (not tested):


    Install pip for Python 3 (Debian Linux)

    > sudo apt-get install python3-pip

    Then:

    > pip3 install pipenv

    > pipenv install requests

___

#### Copyright (C) 2018 Ahmad A. A.
