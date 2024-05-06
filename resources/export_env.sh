if [ -z "$2" ] ; then SUFFIX="-3_11" ; else SUFFIX="" ; fi
echo "export environment $1"
conda env export -n $1 | grep -v "^prefix:" > "environment$SUFFIX.yml"
