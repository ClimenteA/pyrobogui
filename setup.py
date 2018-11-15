from setuptools import setup, find_packages

#python setup.py bdist_wheel sdist
#cd dist 
#twine upload *

setup (
	name="pyrobogui",
	version="0.0.1",
	description="Wrapper around pyautogui - plus some new functions ",
	url="https://github.com/ClimenteA/pyrobogui",
	author="Climente Alin",
	author_email="climente.alin@gmail.com",
	license='MIT',
	py_modules=["pyrobogui"],
	packages=find_packages(),
	package_dir={"":"src"}
)