from unittest import TestCase
from generate_bbst_array import GenerateBBSTArray


class Test(TestCase):
    def test_generate_bbst_array(self):
        self.assertEqual([100, 50, 200], GenerateBBSTArray([50, 100, 200]))
        self.assertEqual([100, 50, 200, 25, 75, 150, 250], GenerateBBSTArray([25, 150, 50, 100, 200, 75, 250]))
        self.assertEqual([100, 50, 200, 25, 75, 150, 250, 20, 30, 70, 80, 140, 160, 240, 260],
                         GenerateBBSTArray([20, 30, 70, 80, 140, 160, 240, 260, 25, 150, 50, 100, 200, 75, 250]))
