# conda remove -n tram --all -y
# conda create -n tram python=3.10 -y
# conda activate tram

# conda install nvidia/label/cuda-11.8.0::cuda-toolkit -y # you can disable this if you already have cuda-11.8
# conda install pytorch torchvision torchaudio pytorch-cuda -c pytorch -c nvidia -y
# sudo apt-get install libgl1
# becareful with the driver version (eg. 535, 565) and the cuda version (eg. 11.8, 11.1), the cuda version could require a specific driver version
# https://gist.github.com/MihailCosmin/affa6b1b71b43787e9228c25fe15aeba
conda install -y pytorch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 pytorch-cuda=12.4 -c pytorch -c nvidia
pip install 'git+https://github.com/hansen1416/detectron2.git@a59f05630a8f205756064244bf5beb8661f96180'
pip install "git+https://github.com/hansen1416/pytorch3d.git@75ebeeaea0908c5527e7b1e305fbc7681382db47"

conda install pytorch-scatter -c pyg
conda install -c conda-forge suitesparse

pip install pulp
pip install supervision

pip install open3d
pip install opencv-python
pip install loguru
pip install chumpy
pip install einops
pip install plyfile
pip install pyrender
pip install segment_anything
pip install scikit-image
pip install smplx
pip install timm==0.6.7
pip install evo
pip install pytorch-minimize
pip install imageio[ffmpeg]
pip install numpy==1.26
pip install gdown

# "https://download.pytorch.org/models/resnet50-19c8e357.pth" to /home/hlz/.cache/torch/hub/checkpoints/resnet50-19c8e357.pth
# "https://download.pytorch.org/models/resnet18-5c106cde.pth" to /home/hlz/.cache/torch/hub/checkpoints/resnet18-5c106cde.pth
# vim /home/ubuntu/anaconda3/envs/tram/lib/python3.10/site-packages/chumpy/__init__.py