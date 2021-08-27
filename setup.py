#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
        "luma.core>=1.17.1",
        "pillow>=4.0.0"
        ]

test_requirements = [ ]

setup(
    author="Edward Harman",
    author_email='jaq@ethelred.org',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Treat 2 luma devices as if they are a single display.",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='luma_combine',
    name='luma_combine',
    packages=find_packages(include=['luma_combine', 'luma_combine.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/edward3h/luma_combine',
    version='0.0.1',
    zip_safe=False,
)
