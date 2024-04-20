from unittest import TestCase
from array_chunk import ArrayChunk


class Test(TestCase):
    def test_array_chunk(self):
        array = [7, 5, 6, 4, 3, 1, 2]
        self.assertEqual(3, ArrayChunk(array))
        self.assertEqual([2, 1, 3, 4, 6, 5, 7], array)

        array = [10]
        self.assertEqual(0, ArrayChunk(array))
        self.assertEqual([10], array)

        array = [10, 20]
        self.assertEqual(1, ArrayChunk(array))
        self.assertEqual([10, 20], array)

        array = [10, 20, 30]
        self.assertEqual(1, ArrayChunk(array))
        self.assertEqual([10, 20, 30], array)

        array = [10, 20, 30, 40]
        self.assertEqual(2, ArrayChunk(array))
        self.assertEqual([10, 20, 30, 40], array)

        array = [40, 30, 20, 10]
        self.assertEqual(2, ArrayChunk(array))
        self.assertEqual([10, 20, 30, 40], array)

        array = [30, 40, 20, 10]
        self.assertEqual(2, ArrayChunk(array))
        self.assertEqual([10, 20, 30, 40], array)

        array = [30, 40, 20, 10, 50]
        self.assertEqual(2, ArrayChunk(array))
        self.assertEqual([10, 20, 30, 40, 50], array)

        array = [30, 40, 20, 60, 50, 10]
        self.assertEqual(5, ArrayChunk(array))
        self.assertEqual([30, 40, 20, 10, 50, 60], array)

        array = [30, 40, 20, 50, 10, 60]
        self.assertEqual(0, ArrayChunk(array))
        self.assertEqual([10, 40, 20, 30, 50, 60], array)

        array = [30, 40, 10, 50, 20, 60]
        self.assertEqual(3, ArrayChunk(array))
        self.assertEqual([10, 20, 30, 40, 50, 60], array)

        array = [30, 40, 10, 50, 20, 60, 5]
        self.assertEqual(0, ArrayChunk(array))
        self.assertEqual([5, 40, 10, 30, 20, 50, 60], array)
