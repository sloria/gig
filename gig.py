#!/usr/bin/env python3
"""gig

A .gitignore template generator.

Usage:
  gig list [--global]
  gig <language> ... [--verbose --global]
  gig Python Ruby Clojure ...


To write to a file:
  gig Python Node > .gitignore
  gig macOS VisualStudioCode --global > ~/.global_gitignore


Options:
  -h --help             Show this screen.
  --version             Show version.
  list                  List available languages. NOTE: Languages are case-sensitive.
  -g --global           Generate a global gitignore.
  -v --verbose          Toggle verbose output.
"""
from pkg_resources import DistributionNotFound, get_distribution
import typing
import sys
import logging

from docopt import docopt
import requests

try:
    __version__ = get_distribution("gig").version
except DistributionNotFound:  # not installed
    pass

API_URL = "https://api.github.com/gitignore/templates"
GLOBAL_URL = "https://api.github.com/repos/github/gitignore/contents/Global/"
TEMPLATE_URL = "https://raw.github.com/github/gitignore/master"
HEADER = "########## Generated by gig ###########\n"


def generate_gitignore(
    languages: typing.List[str], global_: bool = False
) -> typing.Tuple[str, int]:
    """Return a .gitignore given a list of languages."""
    output = ""
    exit_code = 0
    session = requests.Session()
    for language in languages:
        base_url = f"{TEMPLATE_URL}/Global" if global_ else TEMPLATE_URL
        url = f"{base_url}/{language}.gitignore"
        res = session.get(url)
        if res.status_code == requests.codes.ok:
            content = res.text  # The gitignore template
            output += f"\n### {language} ###\n\n{content}"
        else:
            command = "gig list --global" if global_ else "gig list"
            message = (
                f'Couldn not get .gitignore for "{language}". '
                f"Use `{command}` for a list of available languages/platforms. "
                "Languages are case-sensitive."
            )
            logging.error(message)
            exit_code = 1
            continue
    return output, exit_code


def list_languages(global_: bool = False) -> typing.Tuple[str, int]:
    """Output the list of available languages."""
    request_url = GLOBAL_URL if global_ else API_URL
    res = requests.get(request_url)
    ok = res.status_code == requests.codes.ok
    output = ""
    if ok:
        resp_data = res.json()
        if global_:
            languages = [
                d["name"].split(".")[0] for d in resp_data if d["name"] != "README.md"
            ]
        else:
            languages = resp_data
        output = "\n".join(languages)
    else:
        logging.debug(res.status_code)
        logging.error("Could not get language list. Please try again later.")
    exit_code = int(not ok)
    return output, exit_code


def main():
    args = docopt(__doc__, version=__version__)
    log_level = logging.INFO if args["--verbose"] else logging.ERROR
    logging.basicConfig(format="%(levelname)s: %(message)s", level=log_level)
    if args["list"]:
        output, code = list_languages(global_=args["--global"])
    else:
        gitignore, code = generate_gitignore(
            languages=args["<language>"], global_=args["--global"]
        )
        output = f"{HEADER}{gitignore}"
    if code:
        sys.exit(code)
    print(output, end="")


if __name__ == "__main__":
    main()
