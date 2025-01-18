#!/usr/bin/python3
"""Send a request, and displays the value of the X-Request-Id variable."""

import sys
from urllib.request import Request, urlopen


if __name__ == "__main__":
    req = Request(sys.argv[1])
    with urlopen(req) as response:
        print(dict(response.headers).get('X-Request-Id'))
