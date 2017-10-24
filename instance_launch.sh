#!/bin/bash
## Script that downloads
## some source data and iPython notebooks
## into a Jupyter image for Python and Machine Learning course

cd /home/jovyan/work
# git reflog requires a name and email if user is not in passwd
# even if you're only cloning
export GIT_COMMITTER_NAME=anonymous
export GIT_COMMITTER_EMAIL=anon@localhost
# diego's repo
git clone https://github.com/daliagachc/NeGI-hyytiala.git
#richards' repo
git clone https://github.com/richard-olav/ebas-data-retrieval-session.git
#bokeh's
git clone https://github.com/bokeh/bokeh-notebooks.git

pip install --upgrade pip
pip install netCDF4
pip install pydap
conda install bokeh
conda install basemap
