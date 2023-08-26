<!--
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
SOFTWARE.
-->

# Contributing

This is the documentation for contributing to `firestarter`.

## Getting started:

You can get started by following the commands below. 
They'll help you clone the repository and install all the dependencies.

1. Clone the repository:

    | OS Independent |
    | --- |
    | `git clone https://github.com/dishb/firestarter.git` |

    Change to the directory:

    | macOS/Linux | Windows |
    | --- | --- |
    | `cd ./firestarter/` | `cd .\firestarter\` |

2. Create a virtual environment (optional, but recommended):

    | macOS/Linux | Windows |
    | --- | --- |
    | `python3 -m venv ./.venv/` | `python -m venv .\.venv\` |
    | `source ./.venv/bin/activate` | `.\.venv\Scripts\activate.bat` |

3. Install the dependencies:

    | macOS/Linux | Windows |
    | --- | --- |
    | `pip3 install -r requirements.txt` | `pip install -r requirements.txt` |
    | `pip3 install -r dev-requirements.txt` | `pip install -r dev-requirements.txt` |

4. Install `firestarter` in edit mode:

    | macOS/Linux | Windows |
    | --- | --- |
    | `pip3 install -e .` | `pip install -e .` |

## Commits:

When making commits to your clone, we ask that you follow this simple guide.

For the sake of readability, we ask that commit messages be no longer than 50 characters.

Here are titles for each commit. They should prefix the short message and be followed by a colon (:).

An example commit: `title: short message`.

- new feature - feat
- small edit - edit
- a bug/general fix - fix
- a chore (dependecies, code redability) - chore
- initializing commits (adding project files) - init
- documentation related changes - docs
- new tests added, general testing - test
- deletions - delete
- formatting or fixing Pylint issues - format
- organizing file structure, changing directory/file names - org
- bumping versions up - bump

If you have any questions, please ask in the Q&A section of Discussions tab.

## Linting

To make sure our code is maintainable, we use Pylint.

When running Pylint, make sure to use the `./.pylintrc` file for configuration.
