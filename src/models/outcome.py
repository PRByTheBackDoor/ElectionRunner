
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

"""The ourcome of an election."""


class Outcome(object):
    """
    Provides a model for an election outcome.
    """

    def __init__(self):
        self.winners = []

    def add_winner(self, candidate):
        """Add a winning candidate to the election outcome."""
        assert candidate not in self.winners

        self.winners.append(candidate)

    def __repr__(self):
        return "Outcome(%s)" % (self.winners)

    def __str__(self):
        out = "Outcome()"
        for can in self.winners:
            out = out + "\n%s" % (can)
        return out
