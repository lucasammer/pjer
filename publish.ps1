./scrips/activate

pip install wheel
pip install twine

python setup/setup.py sdist bdist_wheel

twine upload dist/*
setup/setup.py sdist bdist_wheel