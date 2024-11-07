PYTHON_VERSION=$1
. ../resources/reset_env.sh cosmoloj_py $PYTHON_VERSION
python --version
conda --version

conda install numpy -y
pip install .
conda install pytest -y
pytest