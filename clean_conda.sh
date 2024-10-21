CONDA_ENV=$1

python --version
conda --version
which python
conda init bash
. ~/.bashrc
conda remove -n $CONDA_ENV --all -y