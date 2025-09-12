#!/usr/bin/env python3

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("onekey")
except PackageNotFoundError:
    __version__ = "\"_\""


__title__ = "onekey"
__description__ = "Password meneger based on sha256 hash."
__url__ = "https://github.com/stpatriarch/onekey"

__author__ = "stpatriarch"
__author_email__ = "chinaryannarek@gmail.com"
__license__ = "MIT"

