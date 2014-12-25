
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

"""Provides a model for an election."""


class Election(object):
    """Provides a class to model an election.

    An election consists of constituencies, parties and candidates. Each
    candidate is associated with precisely one constituency and one party.
    """

    def __init__(self):
        self.constituencies = []
        self.parties = []
        self.candidates = []

    def add_candidate(self, candidate):
        """Add a candidate to the election."""
        assert candidate not in self.candidates

        if candidate.party not in self.parties:
            self.parties.append(candidate.party)

        if candidate.constituency not in self.constituencies:
            self.constituencies.append(candidate.constituency)

        self.candidates.append(candidate)

    def __str__(self):
        out = "Election()"
        for con in self.constituencies.itervalues():
            out = out + "\n%s" % (con)
        return out
