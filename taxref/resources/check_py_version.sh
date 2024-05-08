PYTHON_VERSION=$1
. ../resources/reset_env.sh cosmoloj_py $PYTHON_VERSION
python --version
conda --version

conda install pandas python-dotenv -y
pip install .
conda install pytest -y
pytest