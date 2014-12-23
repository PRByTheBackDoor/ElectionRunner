
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

"""Provides a model for an election candidate."""

class Candidate(object):
    """
    Provides a model for an election candidate.
    """

    def __init__(self, candidate_name, party_name,
                 constituency_name, vote_count=None):
        self.name = candidate_name
        self.party = party_name
        self.constituency = constituency_name
        self.vote_count = vote_count

    def set_vote_count(self, vote_count):
        """Set the vote count for the candidate.
        """
        self.vote_count = vote_count

    def __repr__(self):
        return "Candidate(%s, %s, %s, %d)" % (self.name,
                                              self.party,
                                              self.constituency,
                                              self.vote_count)

    def __str__(self):
        return "%s (%s): %d" % (self.name, self.party, self.vote_count)
