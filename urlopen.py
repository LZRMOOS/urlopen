#!/usr/bin/env python3

import webbrowser
import sys
import os


def usage() -> None:
    print('Usage:')
    print('  python3 urlopen.py <url> <x>')
    print('  python3 urlopen.py <filename>')
    print('  python3 urlopen.py')
    sys.exit(1)


def normalize_url(url) -> str:
    if not url.startswith('https://') and not url.startswith('http://'):
        url = 'https://' + url
    return url

def open_url_x_times(url, x) -> None:
    for i in range(x):
        normalized_url = normalize_url(url)
        webbrowser.open(normalized_url)


def open_file_and_read_urls(filename) -> list:
    with open(filename) as f:
        for line in f:
            yield line.strip()


def open_urls(urls) -> None:
    for url in urls:
        normalized_url = normalize_url(url)
        print(normalized_url)
        webbrowser.open(normalized_url)


def main() -> None:
    if len(sys.argv) == 3:
        url = sys.argv[1]
        x = int(sys.argv[2])
        open_url_x_times(url, x)
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        urls = open_file_and_read_urls(filename)
        open_urls(urls)
    else:
        usage()


if __name__ == '__main__':
    main()
    sys.exit(0)
