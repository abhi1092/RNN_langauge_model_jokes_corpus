#!/usr/bin/env bash
python3 Language_Model/train.py & python3 Language_Model/utils.py & python3 Language_Model/sample.py > /dev/null & 
nosetests --with-coverage
