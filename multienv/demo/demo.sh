echo "config with default I/O"
echo
pyenvs config
ls pip_*.yml
rm pip_*.yml

echo
echo "config with custom I/O"
echo
mkdir out
pyenvs config --output out multienv_pip.yml
ls out/pip_*.yml
rm -rf out

echo
echo "display general help"
echo
pyenvs --help

echo
echo "display config specific help"
echo
pyenvs config --help