import unittest
from ufo import UFO


class MyTestCase(unittest.TestCase):
    def test_word_search(self):
        self.assertEqual(UFO(2, [1234, 1777], False), [4660, 6007])
        self.assertEqual(UFO(2, [1234, 1777], True), [668, 1023])


if __name__ == '__main__':
    unittest.main()
