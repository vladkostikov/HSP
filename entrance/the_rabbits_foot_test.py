import unittest
from the_rabbits_foot import TheRabbitsFoot


class MyTestCase(unittest.TestCase):
    def test_word_search(self):
        self.assertEqual(TheRabbitsFoot("отдай мою кроличью лапку", True), "омоюу толл дюиа акчп йрьк")
        self.assertEqual(TheRabbitsFoot("омоюу толл дюиа акчп йрьк", False), "отдаймоюкроличьюлапку")


if __name__ == '__main__':
    unittest.main()
