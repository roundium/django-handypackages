# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os

from setuptools import find_packages, setup

version = __import__('handypackages').__version__

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='django-handypackages',
    version=version,
    python_requires='>=3.6',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "test_project"]),
    platforms=['OS Independent'],
    include_package_data=True,
    description='A Handy Tools For Your Django Project, provided tools: models, utils, context processors, templates, template tags',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Chatr-e Nili',
    author_email='info@cnili.com',
    url='https://gitlab.com/cnili/django-handypackages',
    license='MIT',
    zip_safe=False,
    install_requires=[
        'Django>=1.11,<2.3',
        "django-ckeditor>=5.4.0",
        "django-filer>=1.3.2",
        "django-mathfilters>=0.4.0",
        "phonenumbers>=8.10.10",
        "django-easy-select2>=1.5.2",
        "django-phonenumber-field>=2.3.1"
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT license',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
