echo "dependencies with default I/O"
echo
pyenvs dependencies
ls pip_*.yml
rm pip_*.yml

echo
echo "dependencies with custom I/O"
echo
mkdir out
pyenvs dependencies --output out multienv_pip.yml
ls out/pip_*.yml
rm -rf out

echo "deps with default I/O"
echo
pyenvs deps
ls pip_*.yml
rm pip_*.yml

echo
echo "deps with custom I/O"
echo
mkdir out
pyenvs deps --output out multienv_pip.yml
ls out/pip_*.yml
rm -rf out

echo
echo "display general help"
echo
pyenvs --help

echo
echo "display config specific help"
echo
pyenvs dependencies --help