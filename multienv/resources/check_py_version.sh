PYTHON_VERSION=$1
. ../resources/reset_env.sh cosmoloj_py $PYTHON_VERSION
python --version
conda --version

conda install pyyaml -y
pip install .
conda install pytest -y
pytest