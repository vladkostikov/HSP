from unittest import TestCase
from binary_search import BinarySearch


class TestBinarySearch(TestCase):
    def test_step(self):
        array = [num for num in range(100)]
        b_search = BinarySearch(array)
        self.assertEqual(0, b_search.Left)
        self.assertEqual(len(array) - 1, b_search.Right)
        self.assertEqual(0, b_search.Status)

        b_search.Step(29)
        self.assertEqual(0, b_search.Left)
        self.assertEqual(48, b_search.Right)
        self.assertEqual(0, b_search.Status)

        b_search.Step(29)
        self.assertEqual(25, b_search.Left)
        self.assertEqual(48, b_search.Right)
        self.assertEqual(0, b_search.Status)

        b_search.Step(29)
        self.assertEqual(25, b_search.Left)
        self.assertEqual(35, b_search.Right)
        self.assertEqual(0, b_search.Status)

        b_search.Step(29)
        self.assertEqual(25, b_search.Left)
        self.assertEqual(29, b_search.Right)
        self.assertEqual(0, b_search.Status)

        b_search.Step(29)
        self.assertEqual(28, b_search.Left)
        self.assertEqual(29, b_search.Right)
        self.assertEqual(0, b_search.Status)

        b_search.Step(29)
        self.assertEqual(29, b_search.Left)
        self.assertEqual(29, b_search.Right)
        self.assertEqual(0, b_search.Status)

        b_search.Step(29)
        self.assertEqual(29, b_search.Left)
        self.assertEqual(29, b_search.Right)
        self.assertEqual(1, b_search.Status)

        b_search.Step(29)
        self.assertEqual(29, b_search.Left)
        self.assertEqual(29, b_search.Right)
        self.assertEqual(1, b_search.Status)

    def test_get_result(self):
        array = [num for num in range(100)]
        b_search = BinarySearch(array)
        self.assertEqual(0, b_search.GetResult())

        b_search.Step(29)
        self.assertEqual(0, b_search.GetResult())

        b_search.Step(29)
        self.assertEqual(0, b_search.GetResult())

        b_search.Step(29)
        self.assertEqual(0, b_search.GetResult())

        b_search.Step(29)
        self.assertEqual(0, b_search.GetResult())

        b_search.Step(29)
        self.assertEqual(0, b_search.GetResult())

        b_search.Step(29)
        self.assertEqual(0, b_search.GetResult())

        b_search.Step(29)
        self.assertEqual(1, b_search.GetResult())

        b_search.Step(29)
        self.assertEqual(1, b_search.GetResult())

        array = [num for num in range(100_000)]
        b_search = BinarySearch(array)
        self.assertEqual(0, b_search.GetResult())
        while b_search.GetResult() == 0:
            b_search.Step(8000)
        self.assertEqual(1, b_search.GetResult())

        array = [num for num in range(100_000)]
        b_search = BinarySearch(array)
        self.assertEqual(0, b_search.GetResult())
        while b_search.GetResult() == 0:
            b_search.Step(120_000)
        self.assertEqual(-1, b_search.GetResult())
