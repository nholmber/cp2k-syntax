#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Holmberg Nico
# Copyright (c) 2016 Holmberg Nico
#
# License: MIT
#

"""This module exports the CP2KLint plugin class."""

from SublimeLinter.lint import Linter, util
import os

class CP2KLint(Linter):
    """Provides an interface to the cp2klint executable."""
    path = os.path.dirname(os.path.abspath(__file__))
    executable_absolute = os.path.join(path,"linter/cp2klint")
    default_manual = os.path.join(path,"sample-xml/cp2k_input.xml")
    syntax = 'cp2k-input'
    cmd = ('%s' %(executable_absolute), '@', '*')
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0'
    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+): '
        r'(?:(?P<error>[EF])|(?P<warning>[WCN]))\d+ '
        r'(?P<message>.+)'
    )
    tempfile_suffix = "inp.tmp"
    check_version = True
    defaults = {
        '@manualfile=': '%s' %(default_manual)
    }

