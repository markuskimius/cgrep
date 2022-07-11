#!/usr/bin/env python3

from setuptools import setup, find_packages
from os import path

SCRIPTDIR = path.abspath(path.dirname(__file__))

with open(path.join(SCRIPTDIR, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
                             name = "cgrep",
                      description = "A command line utility to grep for blocks of text",
                          version = "1.0.0",
                          license = "Apache 2.0",
                           author = "Mark Kim",
                     author_email = "markuskimius+py@gmail.com",
                              url = "https://github.com/markuskimius/cgrep",
                         keywords = [ "grep", "text" ],
                 long_description = long_description,
    long_description_content_type = "text/markdown",
                          scripts = [
                                        "bin/cgrep",
                                    ],
                       data_files = [
                                        ("man/man1", [
                                            "man/man1/cgrep.1"
                                        ])
                                    ],
)
