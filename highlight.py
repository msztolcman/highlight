#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" highlight - Highlight the found text.
    http://mysz.github.io/highlight
    Author: Marcin Sztolcman (marcin@urzenia.net)

    Get help with: highlight --help
    Information about version: highlight --version
"""

from __future__ import print_function, unicode_literals

__version__ = 0.1

import argparse
import os, os.path
import re
import sys
import unicodedata

def _parse_input_args__parse_pattern(args):  # pylint: disable-msg=invalid-name
    """ Compile pattern as defined by user in `parse_input_args`.
    """
    pattern = args.anon_pattern[0]
    pattern = pattern.decode('utf-8')
    pattern = unicodedata.normalize('NFC', pattern)
    if args.fuzzy:
        pattern = '(' + '.*'.join(re.escape(c) for c in pattern) + ')'
    elif args.regexp:
        pattern = '(' + pattern.replace('(', r'\(').replace(')', r'\)') + ')'
    else:
        pattern = '(' + re.escape(pattern) + ')'

    flags = re.UNICODE
    if args.ignorecase:
        flags |= re.IGNORECASE
    if args.regex_multiline:
        flags |= re.MULTILINE
    if args.regex_dotall:
        flags |= re.DOTALL
    pattern = re.compile(pattern, flags)

    return pattern

def parse_input_args(args):
    """ Parse user defined arguments.
    """
    p = argparse.ArgumentParser(description='')  # pylint: disable-msg=invalid-name

    p.add_argument('-i', '--ignorecase', '--ignore-case', action='store_true', default=False)
    p.add_argument('-g', '--regexp', action='store_true', default=False)
    p.add_argument('-f', '--fuzzy', action='store_true', default=False)
    p.add_argument('-l', '--regex-multiline', action='store_true', default=False)
    p.add_argument('-d', '--regex-dotall', action='store_true', default=False)
    p.add_argument('--version', action='version', version="%s %s" % (os.path.basename(sys.argv[0]), __version__))
    p.add_argument('anon_pattern', metavar='pattern', type=str, nargs=1)

    args = p.parse_args(args)

    args.pattern = _parse_input_args__parse_pattern(args)

    return args

def main():
    """ Run script.
    """
    args = parse_input_args(sys.argv[1:])

    data = sys.stdin.read()
    data = data.decode('utf-8')
    data = unicodedata.normalize('NFC', data)
    data = args.pattern.sub(r'\033[32m\1\033[0m', data)
    print(data)

if __name__ == '__main__':
    main()
