import re
import sys

PYTHON_VERSION = sys.version_info[0]
if (3 == PYTHON_VERSION):
    xrange = range
    unicode = str

class Word(object):
    """docstring for Word"""
    def __init__(self, arg):
        super(Word, self).__init__()
        self.arg = arg
        