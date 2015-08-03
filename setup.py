"""Setup script."""

import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(*rnames)).read()


setup (
    name='geomodel',
    version='0.3.0',
    author="Roman Nurik",
    author_email="api dot roman dot public at gmail dot com (Roman Nurik)",
    description="Indexing and querying geospatial data in App Engine.",
    long_description=(
        read('README.txt')
        + '\n\n' +
        read('CHANGES.txt')
        + '\n\n' +
        read('geo', 'tests', 'geomodel.txt')
        ),
    license="Apache License 2.0",
    keywords="appengine gae geomodel google maps",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        ],
    url='https://github.com/ghelobytes/geomodel',
    packages=['geo'],
    include_package_data=True,
    install_requires=['setuptools'],
    zip_safe=False,
    )
