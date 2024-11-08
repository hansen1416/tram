#!/bin/bash

source ~/.bashrc

conda create -n tram python=3.10 -y
conda activate tram
bash install.sh