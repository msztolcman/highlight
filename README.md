highlight
=========

Highlight the found text.

Current stable version
----------------------

0.1

Installation
------------

`highlight` should work on any platform where [Python](http://python.org) is available, it means Linux, Windows, MacOS X etc. There is no dependencies, plain Python power :) 

To install, go to [GitHub releases](https://github.com/mysz/highlight/releases), download newest release, unpack and put somewhere in `PATH` (ie. `~/bin` or `/usr/local/bin`).

If You want to install newest unstable version, then just copy file to your PATH, for example:

    curl https://raw.github.com/mysz/highlight/master/highlight.py > /usr/local/bin/highlight

or:

    wget https://raw.github.com/mysz/highlight/master/highlight.py -O /usr/local/bin/highlight

Voila!

Usage
-----

    usage: highlight.py [-h] [-i] [-g] [-f] [-l] [-d] pattern

    positional arguments:
    pattern

    optional arguments:
    -h, --help            show this help message and exit
    -i, --ignorecase, --ignore-case
    -g, --regexp
    -f, --fuzzy
    -l, --regex-multiline
    -d, --regex-dotall

Contact
-------

If you like or dislike this software, please do not hesitate to tell me about this me via email (marcin@urzenia.net).

If you find bug or have an idea to enhance this tool, please use GitHub's [issues](https://github.com/mysz/highlight/issues).

License
-------

The MIT License (MIT)

Copyright (c) 2013 Marcin Sztolcman

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

