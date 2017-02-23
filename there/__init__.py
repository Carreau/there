"""
Print current file and line number

   import there
   print(there)
"""

__version__ = '0.0.5'

import sys
import inspect
import types
from builtins import print as _print

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
        return '{}:{}'.format(cf.f_code.co_filename, cf.f_lineno)

    def __repr__(self):
        return str(self)
        cf = inspect.currentframe().f_back
        return '<there {}:{}>'.format(cf.f_code.co_filename, cf.f_lineno)

    def print(self, *args, **kwargs):
        cf = inspect.currentframe().f_back
        _print('{}:{}'.format(cf.f_code.co_filename, cf.f_lineno), '|',*args, **kwargs)

    @property
    def LINE(self):
        cf = inspect.currentframe().f_back
        return cf.f_code.co_filename


    @property
    def FILE(self):
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
    sys.modules[__name__] = There
