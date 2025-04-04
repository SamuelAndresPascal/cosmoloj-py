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
# with explicit import of the shared API scope
bibliograpy process cosmoloj.bib -o cosmoloj_bib.py -S
# only use implicitly imported shared API scope
bibliograpy process cosmoloj.bib -o alt_1_cosmoloj_bib.py -s SHARED_SCOPE -i 'dict()'
# define a local bibliograpy scope
bibliograpy process cosmoloj.bib -o alt_2_cosmoloj_bib.py -i '{}' -s _SCOPE

# use bibliography
echo
echo "bibliograpy usage"
echo "================="
echo
python script.py | tee