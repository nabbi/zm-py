"""Setuptools for zm-py"""
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding="utf-8")

setup(
    name='zm-py',
    version='0.5.2',
    license='Apache Software License',
    url='https://github.com/rohankapoorcom/zm-py',
    author='Rohan Kapoor',
    author_email='rohan@rohankapoor.com',
    description='A loose python wrapper around the ZoneMinder REST API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=("tests",)),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    #install_requires=list(val.strip() for val in (here / 'requirements.txt').read_text(encoding="utf-8")),
    install_requires=["requests"],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
