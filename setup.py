from setuptools import setup
import sys,os

setup(
    name = 'resource-calc',
    version = '0.1.0',
    description = 'Genshin resource calculator',
    license='GPL v3',
    author = 'my name',
    packages = ['src'],
    package_data={'src': ['description.txt']
                 },
    # install_requires=['future'],
    entry_points = {
        'console_scripts': [
            'genshin-resource-calc=src.colorless_main:main']
            },
    classifiers = ['Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.6',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
)