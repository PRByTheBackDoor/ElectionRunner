
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

"""Provides a model for a constituency."""


class Constituency(object):
    """
    Provides a model for a constituency.
    """

    def __init__(self, constituencyName):
        self.name = constituencyName
        self.parties = []
        self.candidates = []

#    def add_party(self, party):
#        """Add a party to the constituency.
#        """
#        assert party not in self.parties
#
#        self.parties.append(party)

    def add_candidate(self, candidate):
        """Add a candidate to the constituency.
        """
        assert candidate not in self.candidates
        assert candidate.party not in self.parties
        assert candidate.constituency is self

        self.parties.append(candidate.party)
        self.candidates.append(candidate)

    def __str__(self):
        out = self.name
        for can in self.candidates:
            out = out + "\n    %s" % (can)
        return out

    def __repr__(self):
        return "Constituency(%s)" % (self.name)
