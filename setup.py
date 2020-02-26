#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""
import sys

from setuptools import find_packages, setup


def get_version(filename):
    """Extract the package version"""
    with open(filename, encoding="utf8") as in_fh:
        for line in in_fh:
            if line.startswith("__version__"):
                return line.split("=")[1].strip()[1:-1]
    raise ValueError("Cannot extract version from %s" % filename)


with open("README.rst", encoding="utf8") as readme_file:
    readme = readme_file.read()

try:
    with open("HISTORY.rst", encoding="utf8") as history_file:
        history = history_file.read()
except OSError:
    history = ""

# requirements for use
requirements = [
    "numpy",
]

# requirements for development (testing, generating docs)
dev_requirements = [
    "coverage<5.0",  # 5.0 breaks a lot of other packages:
    # https://github.com/computationalmodelling/nbval/issues/129
    # https://github.com/codecov/codecov-python/issues/224
    "coveralls",
    "flake8",
    "gitpython",
    "isort",
    "ipython",
    "pre-commit",
    "pdbpp",
    "pylint",
    "pytest",
    "pytest-cov",
    "pytest-xdist",
    "sphinx",
    "sphinx-autobuild",
    "sphinx-autodoc-typehints",
    "sphinx_rtd_theme",
    "travis-encrypt",
    "twine",
    "wheel",
    "jupyter",
    "nbval",
    "nbsphinx",
    "watermark",
]

if sys.version_info >= (3, 6):
    dev_requirements.append("black")

version = get_version("./src/mu_diff/__init__.py")

setup(
    author="Tejas Shetty",
    author_email="tejas.shetty@iitb.ac.in",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Natural Language :: English",
    ],
    description=(
        "Takes two complex valued ndarrays and returns the sum of the absolute values of their differences"
    ),
    python_requires=">=3.6<3.8",
    install_requires=requirements,
    extras_require={"dev": dev_requirements},
    license="GNU General Public License v3",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="mu_diff",
    name="mu_diff",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url="https://github.com/TejasAvinashShetty/mu_diff",
    version=version,
    zip_safe=False,
)
