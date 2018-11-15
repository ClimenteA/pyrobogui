from setuptools import setup, find_packages

#python setup.py bdist_wheel sdist
#cd dist 
#twine upload *


with open("README.md", "r") as fh:
    long_description = fh.read()


setup (
	name="pyrobogui",
	version="0.0.2",
	description="Wrapper around pyautogui for automating mouse and keyboard - plus some new functions",
	url="https://github.com/ClimenteA/pyrobogui",
	author="Climente Alin",
	author_email="climente.alin@gmail.com",
	license='MIT',
	py_modules=["pyrobogui"],
	packages=find_packages(),
	long_description=long_description,
    long_description_content_type="text/markdown",
	package_dir={"":"src"}
)