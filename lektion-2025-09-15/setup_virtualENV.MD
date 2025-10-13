## HERE is the step to setup venv in Linux

## setup virtual enveironment venv
 sudo  apt install python3.10-venv

## Created venv called testenv
 python3 -m venv testenv
 
## Activated testenv
 source testenv/bin/activate
 
## install pytest
 pip install pytest-cov
 
## Deactivate venv
 deactivate
 
## remove venv
 rm -rf testenv

 