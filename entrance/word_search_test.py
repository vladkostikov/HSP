import unittest
from word_search import WordSearch


class MyTestCase(unittest.TestCase):
    def test_word_search(self):
        self.assertEqual(WordSearch(12,"1) строка   разбивается на набор строк через выравнивание по заданной ширине.","строк"), [0, 0, 0, 1, 0, 0, 0])
        self.assertEqual(WordSearch(3,"стр ока с кор тки ми сло вами","ока"), [0, 1, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(WordSearch(5,"строка чуть длиннее","чуть"), [0, 0, 1, 0, 0])


if __name__ == '__main__':
    unittest.main()
