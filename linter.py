#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Ruke
#
# License: MIT
#

"""This module exports the Vrjasslint plugin class."""

from SublimeLinter.lint import Linter, util
import os

class Vrjasslint(Linter):
    """Provides an interface to vrjasslint."""

    syntax = 'jass'
    regex = r'(?P<line>\d+):(?P<col>\d+) (?P<message>.+)'
    cmd = 'java -jar * -c'