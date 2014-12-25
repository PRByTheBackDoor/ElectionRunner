
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

"""Provides unit tests for the ``systems'' package."""

from unittest import TestCase, main

from inputs import election_from_csv

import os.path

from systems import SystemFactory


class SystemFactoryTests(TestCase):
    """Test the system factory class."""

    def setUp(self):
        pass

    def test_create_system(self):
        """Test the public ``create_system()'' function."""

        with self.assertRaises(NameError):
            SystemFactory.create_system("non-existant-system", None)

        SystemFactory.create_system("FPTPSystem", None)


class FPTPSystemTests(TestCase):
    """Test the "first past the post" voting system class."""

    def setUp(self):
        pass

    def test_run(self):
        """Test the public ``run()'' function."""

        path = os.path.dirname(__file__)
        filename = os.path.join(path, "election_test_data.csv")

        # import the data
        el = election_from_csv(filename)
        el_copy = election_from_csv(filename)

        system = SystemFactory.create_system("FPTPSystem", el)

        system.run()

        # check the election object was not modified
        el_candidate_names = map(lambda x: x.name,
                                 el.candidates)
        el_copy_candidate_names = map(lambda x: x.name,
                                      el_copy.candidates)

        el_candidate_votes = map(lambda x: (x.name,
                                            x.constituency.name,
                                            x.party.name,
                                            x.vote_count),
                                 el.candidates)
        el_copy_candidate_votes = map(lambda x: (x.name,
                                                 x.constituency.name,
                                                 x.party.name,
                                                 x.vote_count),
                                      el_copy.candidates)

        el_constituency_names = map(lambda x: x.name,
                                    el.constituencies)
        el_copy_constituency_names = map(lambda x: x.name,
                                         el_copy.constituencies)

        el_party_names = map(lambda x: x.name,
                             el.parties)
        el_copy_party_names = map(lambda x: x.name,
                                  el_copy.parties)

        self.assertEqual(set(el_candidate_names),
                         set(el_copy_candidate_names))
        self.assertEqual(len(el_candidate_names),
                         len(el_copy_candidate_names))

        self.assertEqual(set(el_candidate_votes),
                         set(el_copy_candidate_votes))
        self.assertEqual(len(el_candidate_votes),
                         len(el_copy_candidate_votes))

        self.assertEqual(set(el_constituency_names),
                         set(el_copy_constituency_names))
        self.assertEqual(len(el_constituency_names),
                         len(el_copy_constituency_names))

        self.assertEqual(set(el_party_names),
                         set(el_copy_party_names))


if __name__ == '__main__':
    main()
