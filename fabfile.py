import configparser
import os
import sys
from importlib import util

from provision import (  # noqa
    project,
)

# let's load custom commands defined in
# ~/.fabric/my.py

sys.path.append(os.path.expanduser('~/.fabric'))

spec = util.find_spec('my')

# load custom fabric commands in the case such
# file exists
if spec:
    zzz = util.module_from_spec(spec)
    spec.loader.exec_module(zzz)
