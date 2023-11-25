from unittest import TestCase
from artificial_muscle_fibers import artificial_muscle_fibers


class Test(TestCase):
    def test_artificial_muscle_fibers(self):
        self.assertEqual(0, artificial_muscle_fibers([1, 2, 3, 4, 5]))
        self.assertEqual(2, artificial_muscle_fibers([1, 2, 3, 2, 1]))
        self.assertEqual(2, artificial_muscle_fibers([1, 2, 3, 2, 1, 2, 4, 2, 1]))
        self.assertEqual(0, artificial_muscle_fibers([]))
        arr = [num for num in range(2000)] + [num for num in range(250, 500)] + [num for num in range(400, 500)]
        self.assertEqual(250, artificial_muscle_fibers(arr))
