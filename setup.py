#
# MIT License
#
# Copyright (c) 2023 Dishant B. (@dishb) <code.dishb@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from setuptools import setup

VERSION = "0.0.2"
DESCRIPTION = "A cross-platform CLI to help you jump right into developing projects with Python."

with open("README.md", "r", encoding = "utf-8") as file:
    LONG_DESCRIPTION = file.read()
    file.close()

with open("requirements.txt", "r", encoding = "utf-8") as file:
    REQUIREMENTS = file.read()
    REQUIREMENTS = REQUIREMENTS.split()
    file.close()

setup(name = "firestarter",
      version = VERSION,
      author = "Dishant B. (@dishb)",
      author_email = "code.dishb@gmail.com",
      description = DESCRIPTION,
      long_description = LONG_DESCRIPTION,
      long_description_content_type = "text/markdown",
      packages = ["firestarter",
                  "firestarter._core"
                  ],
      entry_points = {"console_scripts": ["firestarter = firestarter._core._entry_points:_console"]},
      install_requires = REQUIREMENTS,
      python_requires = ">=3.9",
      keywords = ["firestarter",
                  "quickstart"
                  "build tool",
                  "project quickstart",
                  "cli",
                  "tool",
                  "developers",
                  "developing",
                  "firestarter tool",
                  "project maker",
                  "boilerplate",
                  "base files",
                  "python",
                  "cross-platform",
                  "python3"
                  ],
      license = "MIT",
      project_urls = {"Documentation": "https://github.com/dishb/firestarter/tree/main/docs",
                      "Source": "https://github.com/dishb/firestarter/",
                      "Issue Tracker": "https://github.com/dishb/firestarter/issues"
                      },
      url = "https://github.com/dishb/firestarter",
      classifiers = ["Programming Language :: Python :: 3.9",
                     "Programming Language :: Python :: 3.10",
                     "Programming Language :: Python :: 3.11",
                     "Operating System :: OS Independent",
                     "License :: OSI Approved :: MIT License",
                     "Environment :: Console",
                     "Intended Audience :: Developers",
                     "Natural Language :: English",
                     "Topic :: Software Development",
                     "Topic :: Software Development :: Build Tools",
                     "Topic :: Software Development :: Libraries :: Python Modules",
                     "Topic :: Utilities"
                     ]
     )
