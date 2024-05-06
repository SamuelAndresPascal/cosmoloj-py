PYTHON_VERSION=$1

. ../resources/reset_env.sh cosmoloj_py $PYTHON_VERSION
pip install -e .
conda install pytest -y
pytest
python demo.py