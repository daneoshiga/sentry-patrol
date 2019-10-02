# !/usr/bin/env python


import io
import os
import re
import sys
from shutil import rmtree

from setuptools import Command, find_packages, setup

NAME = "sentry-patrol"
DESCRIPTION = "Command Line program to interact with sentry API"
URL = "https://github.com/daneoshiga/sentry-patrol"
EMAIL = "daniloshiga@gmail.com"
AUTHOR = "Danilo Shiga"

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = "\n" + f.read()


class VersionCommand(Command):
    description = "Print current version."
    user_options = []

    _version = "0.0.0"

    @staticmethod
    def read_version():
        with open(os.path.join(here, "CHANGES.rst")) as changes:
            for line in changes:
                VersionCommand._version = line.strip()
                if re.search(r"^[0-9]+\.[0-9]+(\.[0-9]+)?$", VersionCommand._version):
                    break

        return VersionCommand._version

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print(self.read_version())


# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine
class UploadCommand(Command):
    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPi via Twine…")
        os.system("twine upload dist/*")

        sys.exit()


setup(
    name=NAME,
    version=VersionCommand.read_version(),
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    long_description=long_description,
    packages=find_packages(exclude=["docs", "tests", "tests.*", "Pipfile*"]),
    entry_points={"console_scripts": ["patrol=patrol.cli:cli"]},
    zip_safe=False,
    include_package_data=True,
    license="MIT",
    keywords="sentry cli patrol",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: System :: Distributed Computing",
    ],
    cmdclass={"upload": UploadCommand, "version": VersionCommand},
    setup_requires=["pytest-runner"],
    install_requires=["click>=6.7,<6.8", "prettyconf", "simple-rest-client>=1.0.0"],
    tests_require=["pytest", "pytest-cov"],
)
