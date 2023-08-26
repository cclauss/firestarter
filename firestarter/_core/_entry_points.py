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
from subprocess import run, PIPE
from platform import system

from colorama import init, deinit

from ._labels import _Labels
from ._files import GITIGNORE, INIT
from ._projects import _create_blank, _create_package

def _console() -> int:
    """
    firestarter's main entry point. Not meant for programming use.

    Returns:
        int: The exit code.
    """

    init(autoreset = True)

    description = ""

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

    args = parser.parse_args()

    if args.version:
        print("\nfirestarter: v0.0.1\n")
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

    if system().lower() in ["darwin", "linux"]:
        python_cmd = "python3"
        pip_cmd = "pip3"
    elif system().lower() == "windows":
        python_cmd = "python"
        pip_cmd = "pip"
    else:
        print(f"\n{system()} is not supported. Please use Linux, Windows, or macOS.\n")
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

    print(_Labels.INFO + "Creating project directory.")

    os.mkdir(root_dir)
    os.chdir(root_dir)

    print(_Labels.INFO + "Creating virtual environment.")

    venv_path = root_dir / ".venv"
    run([python_cmd, "-m", "venv", venv_path], check = True, stdout = PIPE)

    if git.lower() in ["y", "yes"]:
        print(_Labels.INFO + "Initializing a git repository.")

        run(["git", "init", root_dir], stdout = PIPE, text = True, check = True)

        print(_Labels.INFO + "Creating file: .gitignore")

        with open(root_dir / ".gitignore", "x", encoding = "utf-8") as file:
            file.write(GITIGNORE)
            file.close()

    if project == "blank":
        _create_blank(root_dir)
    elif project == "package":
        _create_package(root_dir, name)

    core_dir = root_dir / "core"
    print(_Labels.INFO + f"Creating directory: {core_dir}")

    os.mkdir(core_dir)
    with open(core_dir / "__init__.py", "x", encoding = "utf-8") as file:
        file.write(INIT)
        file.close()

    print(_Labels.INFO + "Creating file: dev-requirements.txt")

    with open(root_dir / "dev-requirements.txt", "x", encoding = "utf-8") as file:
        if linter != "none":
            file.write(linter)
        if test_framework not in ["unittest", "none"]:
            file.write(test_framework)
        file.close()

    if linter == "pylint":
        print(_Labels.INFO + "Creating file: .pylintrc")
        with open(root_dir / ".pylintrc", "x", encoding = "utf-8") as file:
            file.write("")
            file.close()

    print(_Labels.ACTION + f"Change to the project directory: cd {root_dir}")

    if system().lower() in ["darwin", "linux"]:
        print(_Labels.ACTION + "Activate the virtual environment: source ./.venv/bin/activate")
    else:
        print(_Labels.ACTION +
              "Activate the virtual environment: .\\.venv\\Scripts\\activate.bat"
              )

    req_file = root_dir / "requirements.txt"
    dev_req_file = root_dir / "dev-requirements.txt"
    print(_Labels.ACTION + "Install the dependencies:" +
          f"\n{pip_cmd} install {req_file}" +
          f"\n{pip_cmd} install {dev_req_file}"
          )

    if project == "package":
        dist_req_file = root_dir / "dist-requirements.txt"
        print(f"{pip_cmd} install {dist_req_file}")

        print(_Labels.ACTION + f"Install the package in editable mode: {pip_cmd} install -e .")

    print("")

    deinit()
    return 0
