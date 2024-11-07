PYTHON_VERSION=$1
. ../resources/reset_env.sh cosmoloj_py $PYTHON_VERSION
python --version
conda --version

conda install numpy -y
pip install .
bibliograpy process --output-dir src/coordop -s SHARED_SCOPE bibliograpy.bib
conda install pytest -y
pytest