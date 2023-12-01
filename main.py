import os


os.system('pip install wheel')
os.system('pip install twine')
os.system('python setup.py sdist bdist_wheel')
os.system('python -m twine upload dist/*')