conda activate base
conda env remove -n cosmoloj_py -y
conda env create --yes --file environment_test312.yml -n cosmoloj_py -y python=3.12
conda activate cosmoloj_py
python --version
conda --version

pip install .
pytest