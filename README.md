# CSI4900_Python_Request
Python script that will request RNA-seq and miRNA-seq files from the GDC server

GDC search and retieval API documentation: https://docs.gdc.cancer.gov/API/Users_Guide/Search_and_Retrieval/

___

This program requires the 'requests' library: http://docs.python-requests.org/en/latest/user/install/

### To install the 'requests' library:


#### Windows: 


Check for pip updates

> python -m  pip install --upgrade pip


Install pipenv

> python -m pip install pipenv


Install requests

> python -m pipenv install requests


#### Linux/MacOS:

Same commands as above, but use 'python3' instead.

___

Python 3 is required, created and tested with Python 3.6.

Running this program through the CMD/PowerShell/Terminal is recommended as IDEs may need extra configuration,
and running through the CLI is very simple:

to run:

> python main.py

Or python3 on Linux
