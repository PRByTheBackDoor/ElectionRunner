
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

"""First past the post voting system."""

from systems.system import System
from models.outcome import Outcome


class FPTPSystem(System):
    """
    Provides a simulation of a first past the post (FPTP) voting system.
    """

    def __init__(self, election):
        super(FPTPSystem, self).__init__(election)

    def run(self):
        """Run the simulation."""

        outcome = Outcome()

        for con in self.election.constituencies:
            max_vote = -1
            winner = []
            for can in con.candidates:
                if can.vote_count > max_vote:
                    winner = [can]
                    max_vote = can.vote_count
                elif can.vote_count == max_vote:
                    winner.append(can)

            if len(winner) > 1:
                raise ValueError("Tied vote")
            outcome.add_winner(winner[0])

        return outcome

    class Factory(object):
        """Factory to create the system."""
        def create(self, election):
            return FPTPSystem(election)
