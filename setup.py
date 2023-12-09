#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Simon Hobbs",
    author_email='simon.hobbs@electrooptical.net',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    entry_points={
        'console_scripts': [
            'InteractiveHtmlBom=InteractiveHtmlBom.generate_interactive_bom:main',
        ],
    },
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='InteractiveHtmlBom',
    name='InteractiveHtmlBom',
    packages=find_packages(include=['InteractiveHtmlBom', 'InteractiveHtmlBom.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/snhobbs/InteractiveHtmlBom',
    version='0.1.0',
    zip_safe=False,
)
