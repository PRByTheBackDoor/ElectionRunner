
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

"""Provides unit tests for the ``models'' package."""

from unittest import TestCase, main

from models import Election, Constituency, Party, Candidate, Outcome


class ElectionTests(TestCase):
    """Test all public functions provided by the Election() class."""

    def setUp(self):
        pass

    def test_election(self):
        """Test the public ``add_candidate'' function provided by the
        Election() class.
        """

        el = Election()

        con1 = Constituency("test")
        con2 = Constituency("test2")

        party1 = Party("party1")
        party2 = Party("party2")

        candidate1 = Candidate("candidate1", party1, con1)
        candidate2 = Candidate("candidate2", party2, con1)
        candidate3 = Candidate("candidate3", party2, con2)

        el.add_candidate(candidate1)
        self.assertTrue(candidate1 in el.candidates)
        self.assertTrue(party1 in el.parties)
        self.assertTrue(con1 in el.constituencies)

        with self.assertRaises(AssertionError):
            el.add_candidate(candidate1)

        el.add_candidate(candidate2)
        self.assertTrue(candidate2 in el.candidates)
        self.assertTrue(party1 in el.parties)
        self.assertTrue(con1 in el.constituencies)
        self.assertEqual(len(el.candidates), 2)
        self.assertEqual(len(el.parties), 2)
        self.assertEqual(len(el.constituencies), 1)

        el.add_candidate(candidate3)
        self.assertTrue(candidate3 in el.candidates)
        self.assertTrue(party2 in el.parties)
        self.assertTrue(con2 in el.constituencies)
        self.assertEqual(len(el.candidates), 3)
        self.assertEqual(len(el.parties), 2)
        self.assertEqual(len(el.constituencies), 2)


class ConstituencyTests(TestCase):
    """Test all public functions provided by the Constituency() class."""

    def setUp(self):
        pass

    def test_add_candidate(self):
        """Test the public ``add_candidate'' function provided by the
        Constituency() class.
        """

        con = Constituency("test")
        con2 = Constituency("test2")

        party1 = Party("party1")
        party2 = Party("party2")
        party3 = Party("party3")

        candidate1 = Candidate("candidate1", party1, con)
        candidate2 = Candidate("candidate2", party2, con)
        candidate3 = Candidate("candidate3", party3, con2)
        candidate4 = Candidate("candidate4", party2, con)

        con.add_candidate(candidate1)
        self.assertTrue(candidate1 in con.candidates)
        self.assertEqual(len(con.candidates), 1)

        # attempt to add a candidate twice
        with self.assertRaises(AssertionError):
            con.add_candidate(candidate1)
        self.assertEqual(len(con.candidates), 1)
        self.assertEqual(len(con.parties), 1)

        con.add_candidate(candidate2)
        self.assertTrue(candidate1 in con.candidates)
        self.assertTrue(candidate2 in con.candidates)
        self.assertEqual(len(con.candidates), 2)
        self.assertEqual(len(con.parties), 2)

        # attempt to add a candidate with the wrong constituency
        with self.assertRaises(AssertionError):
            con.add_candidate(candidate3)
        self.assertEqual(len(con.candidates), 2)

        # attempt to add a candidate with the same party
        with self.assertRaises(AssertionError):
            con.add_candidate(candidate4)
        self.assertEqual(len(con.candidates), 2)


class OutcomeTests(TestCase):
    """Test all public functions provided by the Outcome() class."""

    def setUp(self):
        pass

    def test_add_winner(self):
        """Test the public ``add_winner'' function provided by the
        Outcome() class.
        """

        con = Constituency("test")
        con2 = Constituency("test2")

        party1 = Party("party1")
        party2 = Party("party2")

        candidate1 = Candidate("candidate1", party1, con)
        candidate2 = Candidate("candidate2", party2, con2)

        outcome = Outcome()

        outcome.add_winner(candidate1)

        self.assertEqual(len(outcome.winners), 1)
        self.assertTrue(candidate1 in outcome.winners)

        # attempt to add the same candidate
        with self.assertRaises(AssertionError):
            outcome.add_winner(candidate1)


if __name__ == '__main__':
    main()
