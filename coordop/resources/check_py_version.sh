PYTHON_VERSION=$1

. ../resources/reset_env.sh cosmoloj_py $PYTHON_VERSION

conda install numpy -y
pip install .
bibliograpy process --output-dir src/coordop -s SHARED_SCOPE bibliograpy.bib
pip install .

conda install pytest -y
pytest