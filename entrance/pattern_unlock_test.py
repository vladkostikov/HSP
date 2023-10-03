import unittest
from pattern_unlock import PatternUnlock

class MyTestCase(unittest.TestCase):
    def test_pattern_unlock(self):
        self.assertEqual(PatternUnlock(10,[1, 2, 3, 4, 5, 6, 2, 7, 8, 9]), "982843")
        self.assertEqual(PatternUnlock(10,[1, 2, 3, 4, 5, 6, 1, 9, 8, 7]), "9")
        self.assertEqual(PatternUnlock(5,[1, 5, 3, 8, 1]), "565685")
        self.assertEqual(PatternUnlock(6,[1, 5, 3, 8, 1, 2]), "665685")
if __name__ == '__main__':
    unittest.main()
