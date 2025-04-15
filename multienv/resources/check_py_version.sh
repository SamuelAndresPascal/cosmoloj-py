PYTHON_VERSION_ID=$1

conda activate base
conda env remove -n test$PYTHON_VERSION_ID -y

conda env create --yes --file environment_test$PYTHON_VERSION_ID.yml
conda activate test$PYTHON_VERSION_ID

python --version
conda --version

pip install .
pytest