
# The MIT License (MIT)
#
# Copyright (c) 2014 PRByTheBackDoor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Provides a factory to produce systems."""

import inspect
import sys

# voting systems
from systems.fptp_system import FPTPSystem


class SystemFactory(object):
    """
    Provides a factory that produces simulations of voting systems.
    """

    factories = {}

    def add_factory(name, factory):
        """Add a subclassed factory to the system factory."""
        SystemFactory.factories[name] = factory
    add_factory = staticmethod(add_factory)

    def create_system(name, *args):
        """Create a new system using the correct factory."""
        if name not in SystemFactory.factories:
            classes = inspect.getmembers(sys.modules[__name__],
                                         lambda x: inspect.isclass(x) and
                                         x.__module__ !=
                                         SystemFactory. __module__)

            for cls in classes:
                if name == cls[0]:
                    SystemFactory.add_factory(cls[1].Factory())
                    break
            else:
                raise NameError("'%s' is not a supported voting system" % name)

        return SystemFactory.factories[name].create(*args)

    create_system = staticmethod(create_system)
