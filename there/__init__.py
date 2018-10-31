"""
Print current file and line number

   import there
   print(there)
"""

__version__ = '0.0.9'

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
    def __init__(self, *args, **kwargs):
        self.level = 0
        super().__init__(*args, **kwargs)

    @property
    def Undefined(self):
        return self

    def __str__(self):
        cf = sys._getframe( self.level+ 1 )
        return '{}:{} in {}'.format(compress(cf.f_code.co_filename), cf.f_lineno, cf.f_code.co_name)

    def __repr__(self):
        return str(self)
        cf = sys._getframe( self.level+ 1 )
        return '<there {}:{}>'.format(compress(cf.f_code.co_filename), cf.f_lineno)

    def print(self, *args, **kwargs):
        cf = sys._getframe( self.level+ 1 )
        _print('{}:{} in '.format(compress(cf.f_code.co_filename), cf.f_lineno, cf.f_code.co_name), '|',*args, **kwargs)

    def syslogprint(self, *args):
        cf = inspect.currentframe().f_back
        syslog.syslog(syslog.LOG_NOTICE, '{}:{}'.format(compress(cf.f_code.co_filename), cf.f_lineno) + '|' + ' '.join([str(x) for x in args]).replace('\n','\\n'))

    def FUNC( back = 0):
        return sys._getframe( self.level+ 1 ).f_code.co_name

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
