#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import argparse
import os, os.path
import re
import sys

p = argparse.ArgumentParser(description='')
p.add_argument('-i', '--ignorecase', '--ignore-case', action='store_true', default=False)
p.add_argument('-g', '--regexp', action='store_true', default=False)
p.add_argument('-f', '--fuzzy', action='store_true', default=False)
p.add_argument('-l', '--regex-multiline', action='store_true', default=False)
p.add_argument('-d', '--regex-dotall', action='store_true', default=False)
p.add_argument('anon_pattern', metavar='pattern', type=str, nargs=1)
args = p.parse_args()

pattern = args.anon_pattern[0]
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

data = sys.stdin.read()
data = pattern.sub(r'\033[32m\1\033[0m', data)
print(data)

