
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

import csv

from constituency import Constituency
from party import Party
from candidate import Candidate


class Election(object):
    """
    Provides a model for an election.
    """

    def __init__(self):
        self.constituencies = {}
        self.parties = {}
        self.candidates = {}

    def import_csv(self, filename):
        with open(filename, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')

            for row in reader:
                # extract the fields from the CSV data
                constituencyName = row[0]
                candidateName = row[1]
                partyName = row[2]
                voteCount = int(row[3])

                # reconcile the constituency
                if constituencyName not in self.constituencies:
                    con = Constituency(constituencyName)
                    self.constituencies[constituencyName] = con
                else:
                    con = self.constituencies[constituencyName]

                # reconcile the party
                if partyName not in self.parties:
                    par = Party(partyName)
                    self.parties[partyName] = par
                else:
                    par = self.parties[partyName]

                # reconcile the candidate
                if (candidateName, partyName, constituencyName) \
                        not in self.candidates:
                    can = Candidate(candidateName,
                                    partyName,
                                    constituencyName,
                                    voteCount)
                    self.candidates[(candidateName,
                                     partyName,
                                     constituencyName)] = can
                else:
                    raise ValueError(
                        """A candidate with the same details already exists""")

                # add the candidate to the constituency
                con.add_candidate(can)

                # add the candidate to the party
                par.add_candidate(can)

                # add the party to the constituency
                con.add_party(par)

    def __str__(self):
        out = "Election()"
        for c in self.constituencies.values():
            out = out + "\n%s" % (c)
        return out
