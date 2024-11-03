echo "bibliograpy demo"
echo "################"
echo


# print help
echo
echo "bibliograpy help"
echo "================"
echo
bibliograpy --help
bibliograpy process --help

# preprocess bibliography
echo
echo "bibliograpy proprocessing"
echo "========================="
echo
bibliograpy process cosmoloj.bib -o cosmoloj_bib.py -S 'from bibliograpy.api import SHARED_SCOPE' -s SHARED_SCOPE

# use bibliography
echo
echo "bibliograpy usage"
echo "================="
echo
python script.py | tee