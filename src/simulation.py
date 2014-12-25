
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

from inputs import election_from_csv
from systems import SystemFactory


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
            for year in args.years:
                # attempt to match a year
                match = re.match(r'^(\d{4})$', year.strip())
                if match is not None:
                    years.append(int(year))
                    continue

                # attempt to match a year range
                match = re.match(r'^(\d{4})-(\d{4})$', year.strip())
                if match is not None:
                    start = int(match.group(1))
                    end = int(match.group(2))

                    if start >= end:
                        raise ValueError("Invalid year range: %s"
                                         % (year.strip()))

                    years.extend(range(start, end+1))

        # uniquify and sort the list of years
        self.years = list(set(years))
        self.years.sort()

        self.voting_systems = ["FPTPSystem"]

        self.systems = []

    def initialise(self):
        """
        Load data for all the elections.
        """

        for year in self.years:
            # attempt to find election data
            path = os.path.dirname(__file__)
            filename = os.path.join(path, "../data/election%d.csv" % (year))
            if os.path.exists(filename):

                # create the elections
                for system_name in self.voting_systems:
                    election = election_from_csv(filename)

                    try:
                        sys = SystemFactory.create_system(system_name,
                                                          election)
                    except NameError, error:
                        print error
                        exit(2)

                    self.systems.append(sys)

        if len(self.systems) == 0:
            print "No election data found for the specified years"
            exit(2)

    def run(self):
        """
        Run all the elections.
        """

        for sys in self.systems:
            sys.run()

    def output(self):
        """
        Produce the required output.
        """

        for sys in self.systems:
            con_max = None
            len_max = 0
            for con in sys.election.constituencies:
                if len(con.parties) > len_max:
                    len_max = len(con.parties)
                    con_max = [con.name]
                elif len(con.parties) == len_max:
                    con_max.append(con.name)

                print "%s\n    %s" % (con.name, con.winner)

            print "%d" % (len_max)
            for con in con_max:
                print "%s" % (con)


if __name__ == "__main__":
    SIM = Simulation()

    SIM.initialise()

    SIM.run()

    SIM.output()
