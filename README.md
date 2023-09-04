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

<div align = 'center'>
    <img alt = 'banner image' src = './assets/banner.png' width = 300/>
</div>

# firestarter
A cross-platform CLI to help you jump right into developing projects with Python.

## Features:
- Create boilerplate files + code for a Python package
- Create boilerplate files + code for a blank project
- Configure a testing framework
- Configure a linter
- Initialize a `git` repository
- Reusable template files (written in a custom langauge!)

## Documentation:
To get more information on how to use `firestarter`, you can read the documentation in the [`./docs`](https://github.com/dishb/firestarter/tree/main/docs) directory.

## Installation:
`firestarter` requires Python 3.9 or higher.

You can install the package with `pip`.

| macOS/Linux | Windows |
| --- | --- |
| `pip3 install firestarter` | `pip install firestarter` |

## Usage:
You can use `firestarter` by running the command below.

| macOS/Linux | Windows |
| --- | --- |
| `python3 -m firestarter` | `python -m firestarter` |

You can also just call `firestarter` directly.

## Contributing:
To get started with contributing to `firestarter`, follow this guide.
It is recommended to read the [`./CONTRIBUTING.md`](https://github.com/dishb/firestarter/blob/main/CONTRIBUTING.md) file.

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

## Code of Conduct
This project is goverened by the Contributor Covenant Code of Conduct.
We ask that you read the full Code of Conduct in the [`./CODE_OF_CONDUCT.md`](https://github.com/dishb/firestarter/blob/main/CODE_OF_CONDUCT.md) file.

## License:
This project is licensed under the `MIT License`. The full copyright can be found in the [`./LICENSE.md`](https://github.com/dishb/firestarter/blob/main/LICENSE.md) file.

## Attribution
`firestarter`'s logo is an edited version of the FontAwesome [fire icon](https://fontawesome.com/icons/fire?f=classic&s=solid).
