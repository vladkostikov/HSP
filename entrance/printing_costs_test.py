import unittest
from printing_costs import PrintingCosts


class MyTestCase(unittest.TestCase):
    def test_printing_costs(self):
        self.assertEqual(PrintingCosts('   '), 0)
        self.assertEqual(PrintingCosts('/ \\'), 10 + 10)
        self.assertEqual(PrintingCosts('✌.✌'), 50)
        self.assertEqual(PrintingCosts(' !"#$%'), 0 + 9 + 6 + 24 + 29 + 22)
        self.assertEqual(PrintingCosts('&,-.w~'), 24 + 7 + 7 + 4 + 19 + 9)
        self.assertEqual(PrintingCosts('x"Y'), 13 + 6 + 14)


if __name__ == '__main__':
    unittest.main()
