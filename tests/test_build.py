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

from subprocess import run

from pytest import main

def test_build() -> None:
    """
    Tests the command: python3 -m build --sdist --wheel

    Only meant to be run by Dishant B. in his environment.
    """

    command = run(["python3", "-m", "build", "--sdist", "--wheel"],
                  check = False
                  )
    return_code = command.returncode

    assert return_code == 0

if __name__ == "__main__":
    main()
