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
bibliograpy process cosmoloj.bib -o cosmoloj_bib.py -S 'from bibliograpy.api_bibtex import SHARED_SCOPE' -s SHARED_SCOPE
# only use implicitly imported shared API scope
bibliograpy process cosmoloj.bib -o alt_1_cosmoloj_bib.py -s SHARED_SCOPE
# define a local bibliograpy scope
bibliograpy process cosmoloj.bib -o alt_2_cosmoloj_bib.py -S 'SCOPE: dict[str, Reference] = {}' -s SCOPE

# use bibliography
echo
echo "bibliograpy usage"
echo "================="
echo
python script.py | tee