PYTHON_VERSION=$1

. ../resources/reset_env.sh cosmoloj_py $PYTHON_VERSION

pip install .
conda install pytest -y
pytest
python demo/demo.py