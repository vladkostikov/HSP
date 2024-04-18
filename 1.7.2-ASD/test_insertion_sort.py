from unittest import TestCase
from insertion_sort import InsertionSort, InsertionSortStep, KnuthSequence, ShellSort


class Test(TestCase):
    def test_insertion_sort(self):
        array = [7, 6, 5, 4, 3, 2, 1]
        self.assertEqual([1, 3, 2, 4, 6, 5, 7], InsertionSort(array, 3))

        array = [7, 6, 5, 4, 3, 2, 1]
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], InsertionSort(array, 1))

    def test_insertion_sort_step(self):
        array = [7, 6, 5, 4, 3, 2, 1]
        self.assertEqual([1, 6, 5, 4, 3, 2, 7], InsertionSortStep(array, 3, 0))

        array = [1, 6, 5, 4, 3, 2, 7]
        self.assertEqual([1, 3, 5, 4, 6, 2, 7], InsertionSortStep(array, 3, 1))

    def test_knuth_sequence(self):
        self.assertEqual([1], KnuthSequence(0))
        self.assertEqual([1], KnuthSequence(1))
        self.assertEqual([1], KnuthSequence(3))
        self.assertEqual([1], KnuthSequence(4))
        self.assertEqual([4, 1], KnuthSequence(5))
        self.assertEqual([13, 4, 1], KnuthSequence(15))
        self.assertEqual([13, 4, 1], KnuthSequence(15))
        self.assertEqual([13, 4, 1], KnuthSequence(15))
        self.assertEqual([13, 4, 1], KnuthSequence(39))
        self.assertEqual([13, 4, 1], KnuthSequence(40))
        self.assertEqual([40, 13, 4, 1], KnuthSequence(41))


    def test_shell_sort(self):
        array = []
        self.assertEqual([], ShellSort(array))

        array = [7, 6, 5, 4, 3, 2, 1]
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], ShellSort(array))

        array = list(reversed([num for num in range(15)]))
        self.assertEqual(list(sorted(array)), ShellSort(array))

        array = list(reversed([num for num in range(42)]))
        self.assertEqual(list(sorted(array)), ShellSort(array))

        array = list(reversed([num for num in range(123)]))
        self.assertEqual(list(sorted(array)), ShellSort(array))

        array = list(reversed([num for num in range(366)]))
        self.assertEqual(list(sorted(array)), ShellSort(array))
