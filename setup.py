#!/usr/bin/env python
from distutils.core import setup


VERSION = '3.2.5git' 

README_FILE = open('README')
try:
    long_description = README_FILE.read()
finally:
    README_FILE.close()

 
setup(
    name='sorl-thumbnail',
    version=VERSION,
    url='https://github.com/sorl/sorl-thumbnail',
    description='Thumbnails for Django',
    long_description=long_description,
    author='Mikko Hellsing, Chris Beaven',
    platforms=['any'],
    packages=[
        'sorl',
        'sorl.thumbnail',
        'sorl.thumbnail.templatetags',
        'sorl.thumbnail.tests',
        'sorl.thumbnail.management',
        'sorl.thumbnail.management.commands',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
