# -*- coding: utf-8 -*-

# Third
from setuptools import find_packages, setup

__version__ = '0.0.1'
__description__ = 'Api Python Flask'
__long_description__ = 'Api for app Anamnese'

__author__ = 'Matheus Leite'
__author_email__ = 'matheusjoselfm@gmail.com'

# Modulos para testes na aplicacao
testing_extras = [
    'pytest',
    'pytest-cov',
]

setup(
    name='api',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    license='MIT',
    description=__description__,
    long_description=__long_description__,
    url='https://github.com/itzmatheus/api-user-flask',
    keywords='API, MongoDB',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'testing': testing_extras,
    },
)
