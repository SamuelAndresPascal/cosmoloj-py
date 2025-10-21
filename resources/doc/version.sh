LANG=$1

if [ $CI_COMMIT_TAG ] ; then VERSION=$(echo $CI_COMMIT_TAG | cut -d'_' -f 2) ; else VERSION=$CI_COMMIT_BRANCH ; fi
echo $'\n**Version '$VERSION'**' >> docs/$LANG/about.md
echo $'\nDocumentation generated at '$(date -u +"%F %T")' UTC' >> docs/$LANG/about.md
