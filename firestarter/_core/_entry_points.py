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

import os
from argparse import ArgumentParser
from pathlib import Path
from platform import system

from .._fuel import _ignite
from ._labels import _Labels

def _console() -> int:
    """
    firestarter's main entry point. Not meant for programming use.

    Returns:
        int: The exit code.
    """

    description = """description: a cross-platform CLI to help you jump right into developing
projects with Python."""

    parser = ArgumentParser(prog = "firestarter",
                            description = description,
                            )
    parser.add_argument("-v", "--version",
                        action = "store_true",
                        help = "print the version of firestarter.",
                        required = False,
                        dest = "version"
                        )
    parser.add_argument("-c", "--copyright",
                        action = "store_true",
                        help = "print the license/full copyright of firestarter.",
                        required = False,
                        dest = "license"
                        )
    parser.add_argument("-f", "--fuel",
                        nargs = 1,
                        action = "store",
                        help = "use a fuel template to create a project.",
                        required = False,
                        dest = "fuel",
                        metavar = "PATH TO TEMPLATE"
                        )

    args = parser.parse_args()

    if args.version:
        print("\nfirestarter: v0.0.2\n")
        return 0

    if args.license:
        print("""
firestarter is licensed under the MIT License:

MIT License

Copyright (c) 2023 Dishant B. (@dishb) <code.dishb@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE
"""
             )
        return 0

    if args.fuel:
        fuel_template = Path(args.fuel[0])

        return _ignite(fuel_template)

    if system().lower() not in ["darwin", "linux", "windows"]:
        print(_Labels.ERROR +
              f"\n{system()} is not supported. Please use Linux, Windows, or macOS.\n"
              )
        return 1

    name = input(_Labels.INIT + "Name of project: ")

    path = input(_Labels.INIT + "Path to project (blank defaults to current directory): ")
    if path is None or path == "":
        path = "."

    root_dir = Path(path) / name
    if os.path.exists(root_dir):
        print(_Labels.ERROR + f"{root_dir} already exists.")
        return 1

    git = ""
    while git.lower() not in ["y", "n", "yes", "no"]:
        git = input(_Labels.INIT + "Do you want to initialize a git repository? (y/n) ")

    project = ""
    while project not in ["package", "blank"]:
        project = input(_Labels.INIT + "Type of project (package, blank): ")

    test_framework = ""
    while test_framework.lower() not in ["pytest", "unittest", "none"]:
        test_framework = input(_Labels.INIT + "Testing framework (pytest, unittest, none): ")

    linter = ""
    while linter.lower() not in ["pylint", "flake8", "black", "bandit", "none"]:
        linter = input(_Labels.INIT + "Linter (pylint, flake8, black, bandit, none): ")

    temp_dir = Path("./.firestarter/")
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)

    template_file = temp_dir / ".firestarter_temp.fuel"
    if os.path.exists(template_file):
        mode = "w"
    else:
        mode = "x"

    with open(template_file, mode, encoding = "utf-8") as file:
        file.write(f"""[name] :: {name}
[path] :: {path}
[git] :: {git}
[project-type] :: {project}
[test-framework] :: {test_framework}
[linter] :: {linter}
"""
                  )

    return _ignite(template_file)
