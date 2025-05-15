PYTHON_VERSION=$1
. ../resources/reset_env.sh cosmoloj_py $PYTHON_VERSION
python --version
conda --version

pip install .
conda install pytest -y
pytest
python demo/group_preprocessor.py
python demo/merge_preprocessor.py