PYTHON_VERSION=$1

. ../resources/reset_env.sh cosmoloj_py $PYTHON_VERSION

conda install pandas python-dotenv -y
pip install .
conda install pytest -y
pytest