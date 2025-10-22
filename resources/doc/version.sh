LANG=$1

echo $VERSION
echo $LANG

echo $'\n**Version '$VERSION'**' >> docs/$LANG/about.md
echo $'\nDocumentation generated at '$(date -u +"%F %T")' UTC' >> docs/$LANG/about.md

cat docs/$LANG/about.md
