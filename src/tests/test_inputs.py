
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

"""Provides unit tests for the ``inputs'' package."""

from unittest import TestCase, main

from inputs import election_from_csv

import os.path


class ImportTests(TestCase):
    """Test all public functions provided by the inputs package."""

    def setUp(self):
        pass

    def test_election_from_csv(self):
        """Test the public ``election_from_csv'' function."""

        path = os.path.dirname(__file__)
        filename = os.path.join(path, "non_existant_file.csv")

        with self.assertRaises(IOError):
            election_from_csv(filename)

        filename = os.path.join(path, "election_test_data.csv")

        # import the data
        el = election_from_csv(filename)

        # check that only the expected constituencies were imported
        expected_constituency_names = ["Forthright South",
                                       "Stonecorner",
                                       "Blandbridge"]
        imported_constituency_names = map(lambda x: x.name,
                                          el.constituencies)

        self.assertEqual(set(expected_constituency_names),
                         set(imported_constituency_names))
        self.assertEqual(len(el.constituencies),
                         len(expected_constituency_names))

        # check that only the expected parties were imported
        expected_party_names = ["C", "Lab", "LD", "UKIP"]
        imported_party_names = map(lambda x: x.name, el.parties)

        self.assertEqual(set(expected_party_names), set(imported_party_names))
        self.assertEqual(len(el.parties), len(expected_party_names))

        # check that only the expected candidates were imported
        expected_candidates = [("Farmer, Joseph", 12390),
                               ("Woolsey, J.C.", 21208),
                               ("Clews, Louise", 7923),
                               ("Williams, Wendy", 25002),
                               ("Scoffing, Peter.", 15432),
                               ("Green, P.M.", 13450),
                               ("Piddling, Grant", 1923),
                               ("Dodge, John", 13398)]

        expected_candidate_names = map(lambda x: x[0], expected_candidates)
        imported_candidate_names = map(lambda x: x.name, el.candidates)

        self.assertEqual(set(expected_candidate_names),
                         set(imported_candidate_names))
        self.assertEqual(len(el.candidates), len(expected_candidate_names))

        # check that the correct vote counts were imported
        expected_candidate_votes = map(lambda x: x[1], expected_candidates)
        imported_candidate_votes = map(lambda x: x.vote_count, el.candidates)

        self.assertEqual(set(expected_candidate_names),
                         set(imported_candidate_names))
        self.assertEqual(len(el.candidates), len(expected_candidate_names))


if __name__ == '__main__':
    main()
