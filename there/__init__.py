"""
Print current file and line number

   import there
   print(there)
"""

__version__ = '0.0.8'

import sys
import inspect
import types
from builtins import print as _print

import os.path

import syslog

HOME = os.path.expanduser('~')
LEN_HOME = len(HOME)

def compress(path):
    if path.startswith(HOME):
        return '~'+path[LEN_HOME:]
    return path

class There(types.ModuleType):
    """
    Simply a global object that act as undefined.
    """

    __version__ = __version__


    @property
    def Undefined(self):
        return self

    def __str__(self):
        cf = inspect.currentframe().f_back
        return '{}:{}'.format(compress(cf.f_code.co_filename), cf.f_lineno)

    def __repr__(self):
        return str(self)
        cf = inspect.currentframe().f_back
        return '<there {}:{}>'.format(compress(cf.f_code.co_filename), cf.f_lineno)

    def print(self, *args, **kwargs):
        cf = inspect.currentframe().f_back
        _print('{}:{}'.format(compress(cf.f_code.co_filename), cf.f_lineno), '|',*args, **kwargs)

    def syslogprint(self, *args):
        cf = inspect.currentframe().f_back
        syslog.syslog(syslog.LOG_NOTICE, '{}:{}'.format(compress(cf.f_code.co_filename), cf.f_lineno) + '|' + ' '.join([str(x) for x in args]).replace('\n','\\n'))

    def FILE(self):
        cf = inspect.currentframe().f_back
        return compress(cf.f_code.co_filename)


    def LINE(self):
        cf = inspect.currentframe().f_back
        return cf.f_lineno



There.__name__ = 'There'
There = There('there', """
    Simply a global object that act as undefined.
    """
    )

There.__version__ = __version__


if sys.modules[__name__] is There:
    print('doing nothing')
    pass
else:
    There.__file__ = sys.modules[__name__].__file__
    sys.modules[__name__] = There
