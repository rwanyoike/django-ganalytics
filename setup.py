#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='django-ganalytics',
    version='1.0.0',
    description='Simple integration of the Google Analytics tracking code in Django projects.',
    author='Raymond Wanyoike',
    author_email='raymond.wanyoike@gmail.com',
    long_description=open('README.rst').read(),
    url='http://bitbucket.org/raymondwanyoike/django-ganalytics/',
    packages=find_packages(),
    include_package_data=True,
    keywords='django ganalytics',
    install_requires=[
        'Django>=1.4,<1.6',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    zip_safe=False,
)
