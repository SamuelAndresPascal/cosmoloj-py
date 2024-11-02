echo "bibliograpy demo"
echo

# print help
bibliograpy --help
bibliograpy process --help

# preprocess bibliography
bibliograpy process cosmoloj.bib -o cosmoloj_bib.py

# use bibliography
python script.py