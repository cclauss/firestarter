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

# Fuel Documentation

This is the documentation for `firestarter`'s template language, `fuel`.

## Syntax:
`fuel` has a very simple and minimal syntax.

#### Comments:
Comments are written using the `$` (dollar-sign). `fuel` only has single-line comments (no multi-line comments).

Example:
```
$ this is a comment
$ comments are ignored by fuel's parser completely

this is not a comment (and raises an error)

$
this is not a multi-line comment, it will raise an error
$
```

#### Headers:
Headers are used to define the values for different options. They are written using the `[]` (square-brackets).

The basic formula is `[option] :: value`

Example:
```
[name] :: name_of_my_project
```

#### Seperators:
`fuel` uses seperators to, well, seperate a header and it's corresponding value.

Seperators are written with `::` (2 colons).

You can look at the example provided in [Headers](#headers).

#### Values:
Values are the actual input you provide for each option. This is the configuration that `firestarter` will use when creating the project.

You can look at the example provided in [Headers](#headers).

## Options:
These are all the options for `firestarter` and their descriptions. The order that you put these options in the template does not matter.

| Option | Description |
| -- | -- |
| `name` | The name of your project. The value cannot have spaces. Instead of spaces, use underscores (_) or dashes (-). |
| `project-type` | The type of the project, must be one of the following: blank, package. |
| `path` | The path to the parent directory where the project will be created. Unlike the CLI, this option cannot be left blank in the template. |
| `git` | Whether or not you want to intialize a Git repository. Must be on of the following (case does not matter): yes, y, no, n. |
| `test-framework` | The framework (a Python package) that will be used for testing. Must be one of the following: pytest, unittest, none. |
| `linter` | The linter used in the project. Must be one of the following: pylint, flake8, bandit, black, none. |

