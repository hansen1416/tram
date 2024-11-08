#!/bin/bash

curl -O https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh

bash Anaconda3-2024.10-1-Linux-x86_64.sh -b -p $HOME/anaconda3

source ~/.bashrc

conda create -n tram python=3.10 -y
conda activate tram
bash install.sh