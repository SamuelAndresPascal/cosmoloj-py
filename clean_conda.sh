CONDA_ENV=$1
PYTHON_VERSION=$2

python --version
conda --version
which python
which conda
conda init bash
conda env list
conda list $CONDA_ENV
conda create -n $CONDA_ENV python=$PYTHON_VERSION -y
. ~/.bashrc
conda activate $CONDA_ENV
conda list
python --version
which python