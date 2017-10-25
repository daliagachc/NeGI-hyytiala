# ebas-data-retrieval-session
Notebooks used for demonstrating retrieval of data in EBAS using OPeNDAP

**In order to successfully run the notebooks, you need to install the following python modules:**

pydap.handlers.cdms==0.2.0.1

bokeh==0.12.10

numpy==1.13.3

pandas==0.20.1

matplotlib==1.5.1

netCDF4==1.3.0

pydap==3.2.2

# How to get started using notebooks on csc

**When you open the Notebook GUI, you will in the right corner of the screen see a dropdown with the title "New".
> Press this, and then select "Terminal"

**Set Git Name and Email**
>export GIT_COMMITTER_NAME=anonymous

>export GIT_COMMITTER_EMAIL=anon@localhost

**clone the repository**
> git clone https://github.com/richard-olav/ebas-data-retrieval-session.git

**First install requirements.txt (must be done locally for user)**
> pip install --upgrade pip

> pip install -U -r requirements.txt

or

> pip install --upgrade pip

> pip install -U netCDF4

> pip install -U Pydap

**Go to the python3 directory, and you should be able to play around**
