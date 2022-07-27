#!/usr/bin/env python3

import webbrowser
import sys
import os

def usage() -> None:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)


def open_file_and_read_urls(filename) -> list:
    with open(filename) as f:
        for line in f:
            yield line.strip()


def open_urls(urls) -> None:
    for url in urls:
        if not url.startswith('https://') and not url.startswith('http://'):
            url = 'https://' + url

        print(url)
        webbrowser.open(url)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print("File " + filename + " does not exist")
        sys.exit(1)

    urls = open_file_and_read_urls(filename)
    open_urls(urls)
    sys.exit(0)
