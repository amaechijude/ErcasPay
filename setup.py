from setuptools import setup, find_packages

setup(
    name="ercaspay",
    version='0.1',
    author='Amaechi Ugwu',
    author_email='amaechijude178@gmail.com',
    description='This package simplifies ercasng payment processing in python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/amaechijude/ErcasPay',
    packages=find_packages(),
    classifiers= [
        " Programming Language :: Python :: 3",
        "Licence :: OSI Approved :: MIT Licence",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8"
)