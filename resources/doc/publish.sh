# expects the language argument
LANG=$1

# assumes the documentation archive is available, named "site.<lang>.zip" and contains a "site.lang" folder to extract.

PUBLIC_DOC_DIR=$PUBLIC_SITE_SERVER_PATH/mkdocs/$CI_PROJECT_NAME/$LANG

ssh $PUBLIC_SITE_USER@$PUBLIC_SITE_SERVER "mkdir -p $PUBLIC_DOC_DIR"
scp site.$LANG.zip $PUBLIC_SITE_USER@$PUBLIC_SITE_SERVER:$PUBLIC_DOC_DIR
ssh $PUBLIC_SITE_USER@$PUBLIC_SITE_SERVER "cd $PUBLIC_DOC_DIR ; rm -rf $VERSION ; unzip site.$LANG.zip ; mv site.$LANG $VERSION ; rm site.$LANG.zip"
if [ $CI_COMMIT_TAG ] ; then ssh $PUBLIC_SITE_USER@$PUBLIC_SITE_SERVER "cd $PUBLIC_DOC_DIR ; rm latest ; ln -s $VERSION latest" ; fi
