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

"""
firestarter

Author: Dishant B. (@dishb) code.dishb@gmail.com
License: MIT License
Source: https://github.com/dishb/firestarter
"""

from pathlib import Path
from os import mkdir

from ._files import BLANK_MAIN, DIST_REQS, INIT, SETUP_PY
from ._labels import _Labels

def _create_package(root_dir: Path, name: str) -> None:
    """
    Creates a Python package. Not meant for programming use.

    Args:
        root_dir (Path): The root or base directory for the project.
        name (str): The name of the project.
    """

    print(_Labels.INFO + f"Creating directory: {root_dir / name}")

    mkdir(root_dir / name)

    print(_Labels.INFO + "Creating file: requirements.txt")

    with open(root_dir / "requirements.txt", "x", encoding = "utf-8") as file:
        file.write("")
        file.close()

    print(_Labels.INFO + "Creating file: dist-requirements.txt")

    with open(root_dir / "dist-requirements.txt", "x", encoding = "utf-8") as file:
        file.write(DIST_REQS)
        file.close()

    print(_Labels.INFO + "Creating directory: tests")

    mkdir(root_dir / "tests")
    with open(root_dir / "tests" / "__init__.py", "x", encoding = "utf-8") as file:
        file.write(INIT)
        file.close()

    print(_Labels.INFO + "Creating file: setup.py")

    with open(root_dir / "setup.py", "x", encoding = "utf-8") as file:
        file.write(SETUP_PY)
        file.close()

def _create_blank(root_dir: Path) -> None:
    """
    Creates a blank project. Not meant for programming use.

    Args:
        root_dir (Path): The root or base directory for the project.
    """

    print(_Labels.INFO + "Creating file: main.py")

    with open(root_dir / "main.py", "x", encoding = "utf-8") as file:
        file.write(BLANK_MAIN)
        file.close()

    print(_Labels.INFO + "Creating file: requirements.txt")

    with open(root_dir / "requirements.txt", "x", encoding = "utf-8") as file:
        file.write("")
        file.close()
