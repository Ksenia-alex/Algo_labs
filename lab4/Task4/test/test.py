import unittest
from lab4.Task4.src.task4 import checking_bracket_sequence


class BracketSequenceTestCase(unittest.TestCase):

    def test_an_example_from_the_text(self):
        self.assertEqual(checking_bracket_sequence("[]"), "Success")
        self.assertEqual(checking_bracket_sequence("{}[]"), "Success")
        self.assertEqual(checking_bracket_sequence("[()]"), "Success")
        self.assertEqual(checking_bracket_sequence("(())"), "Success")
        self.assertEqual(checking_bracket_sequence("{"), "1")
        self.assertEqual(checking_bracket_sequence("{[}"), "2")
        self.assertEqual(checking_bracket_sequence("foo(bar);"), "Success")
        self.assertEqual(checking_bracket_sequence("foo(bar[i);"), "8")


    def test_with_other_data(self):
        self.assertEqual(checking_bracket_sequence("[((({{}})))]"), "Success")
        self.assertEqual(checking_bracket_sequence("{()[]{{}}}[{({}{})}]"), "Success")
        self.assertEqual(checking_bracket_sequence("[(()([{}])({})({}))]"), "Success")
        self.assertEqual(checking_bracket_sequence("w(i(t{h{(w)o}r{d{[p]u}p}u}p)u)[]"), "Success")
        self.assertEqual(checking_bracket_sequence("{}{([)}"), "5")
        self.assertEqual(checking_bracket_sequence("{[][[[[()({})]]]]}{"), "19")
        self.assertEqual(checking_bracket_sequence("foo(bar[i[i]]);"), "Success")
        self.assertEqual(checking_bracket_sequence("foo(bar{[i[i][i]i]);"), "8")