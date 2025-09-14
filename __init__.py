__version__ = "0.1.0"
__author__ = "Jay Kuroor"

from .beam import *
from .data import *
from .nn import *
from .optim import *
from .utils import *

def version():
    return __version__

def info():
    return f"Version: {__version__}, Author: {__author__}"