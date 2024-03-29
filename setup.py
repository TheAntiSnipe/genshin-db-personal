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
    
    # Comment this line if you're snapping
    # a colorless installation.
    
    install_requires=['colorama'],
    
    # Uncomment this line if you're snapping a colorless 
    # installation:
    
    # entry_points = {
    #     'console_scripts': [
    #         'genshin-resource-calc=src.colorless_main:main']
    #         },
    
    entry_points = {
        'console_scripts': [
            'genshin-resource-calc=src.main:main']
            },
    
    classifiers = ['Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.6',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
)