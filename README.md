# gig

[![PyPI Latest Version](https://badgen.net/pypi/v/gig)](https://pypi.org/project/gig/)
[![Travis CI Status](https://badgen.net/travis/sloria/gig)](https://travis-ci.org/sloria/gig)

A CLI to create .gitignore files, to keep your source control so fresh and clean.

![Andre](https://upload.wikimedia.org/wikipedia/commons/d/d8/Andr%C3%A93000.jpg)

## Install/Upgrade

```
$ pip install -U gig
```

Or, run it with [pipx](https://github.com/pipxproject/pipx):

```
$ pipx run gig --help
```

## Usage

In the shell. . .

```
$ gig Python Ruby > .gitignore
```

Or, programmatically, in Python. . .

```python
>>> import gig
>>> gig.generate_gitignore(["Clojure"])
u'\n### Clojure ###\nLeiningen.gitignore'
```

You can also generate global `.gitignore_global` files. For more info, see [here](https://help.github.com/en/articles/ignoring-files#create-a-global-gitignore).

```
$ gig macOS VisualStudioCode --global > ~/.gitignore_global
```

To get a list of available templates. . .

```
$ gig list
$ gig list --global
```

For more help, run `gig --help`.

## Requirements

- Python >= 3.6
- Internet connection

## License

MIT Licensed.

## Changelog

### 1.0.0 (2019-06-27)

- Write to `stdout`.
- Only Python>=3.6 is supported.

### 0.2.0 (2013-09-09)

- Add support for global gitignore files.

### 0.1.0 (2013-09-07)

- First release.
