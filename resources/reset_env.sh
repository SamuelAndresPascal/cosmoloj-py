conda activate base
if [ -z "$2" ] ; then PYTHON_VERSION=3.11 ; else PYTHON_VERSION=$2 ; fi
conda env remove -n $1 -y
conda create -n $1 -y python=$PYTHON_VERSION
conda activate $1
python --version
conda --version