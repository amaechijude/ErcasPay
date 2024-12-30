from setuptools import setup, find_packages

setup(
    name="ercas_pay",
    version='0.1',
    author='Amaechi Ugwu',
    author_email='amaechijude178@gmail.com',
    description='This package simplifies ercasng payment processing in python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://docs.ercaspay.com/',
    packages=find_packages,
    classifiers= [
        " Programming Language :: Python :: 3",
        "Licence :: OSI Approved :: MIT Licence"
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8"
)