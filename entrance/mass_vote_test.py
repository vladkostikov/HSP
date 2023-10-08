import unittest
from mass_vote import MassVote


class MyTestCase(unittest.TestCase):
    def test_mad_max(self):
        self.assertEqual(MassVote(5, [60, 10, 10, 15, 5]), "majority winner 1")
        self.assertEqual(MassVote(3, [10, 15, 10]), "minority winner 2")
        self.assertEqual(MassVote(4, [111, 111, 110, 110]), "no winner")
        self.assertEqual(MassVote(1, [5]), "majority winner 1")
        self.assertEqual(MassVote(1, [0]), "no winner")
        self.assertEqual(MassVote(2, [0, 3]), "majority winner 2")
        self.assertEqual(MassVote(2, [0, 2, 3, 2]), "minority winner 3")


if __name__ == '__main__':
    unittest.main()
