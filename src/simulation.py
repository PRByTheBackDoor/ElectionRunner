
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

"""
Run an election simulation.
"""

import argparse
import re
import os

from elections import FPTPElection


class Simulation(object):
    """
    Class to run an election simulation.
    """

    def __init__(self):
        """
        Initialise the simulator.
        """

        parser = argparse.ArgumentParser("Simulate general elections")
        parser.add_argument("years", nargs="*",
                            help="election years to run the simulation for \
                                                        (can be a range)")
        parser.add_argument("-v", "--verbose", action="store_true",
                            help="increase output verbosity")
        args = parser.parse_args()

        years = []
        if not args.years:
            years = range(0, 9999)
        else:
            for y in args.years:
                # attempt to match a year
                match = re.match('^(\d{4})$', y.strip())
                if match is not None:
                    years.append(int(y))
                    continue

                # attempt to match a year range
                match = re.match('^(\d{4})-(\d{4})$', y.strip())
                if match is not None:
                    start = int(match.group(1))
                    end = int(match.group(2))

                    if start >= end:
                        raise ValueError("Invalid year range: %s"
                                         % (y.strip()))

                    years.extend(range(start, end+1))

        # uniquify and sort the list of years
        years = list(set(years))
        years.sort()

        # TODO: these should be generator functions
        election_types = ["FPTP"]

        self.elections = []

        for y in years:
            # attempt to find election data
            filename = "../data/election%d.csv" % (y)
            if os.path.exists(filename):

                # create the elections
                for t in election_types:
                    # XXX:
                    e = FPTPElection()
                    e.import_csv(filename)

                    self.elections.append(e)

        if len(self.elections) == 0:
            print "No election data found for the specified years"
            exit(2)

    def run(self):
        """
        Run all the elections.
        """

        for e in self.elections:
            e.run()

            for con in e.constituencies.values():
                print "%s\n    %s" % (con.name, con.winner)


if __name__ == "__main__":
    s = Simulation()

    s.run()
