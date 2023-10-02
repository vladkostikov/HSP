import unittest
from synchronizing_tables import SynchronizingTables

class MyTestCase(unittest.TestCase):
    def test_synchronizing_tablesx(self):
        self.assertEqual(SynchronizingTables(3,[50, 1, 1024], [20000, 100000, 90000]), [90000, 20000, 100000])
        self.assertEqual(SynchronizingTables(5,[3, 1, 4, 2, 5], [10, 40, 50, 20, 30]), [30, 10, 40, 20, 50])
        self.assertEqual(SynchronizingTables(1,[10], [1000]), [1000])
        self.assertEqual(SynchronizingTables(2,[50, 10], [1200, 3300]), [3300, 1200])
        self.assertEqual(SynchronizingTables(0,[], []), [])
if __name__ == '__main__':
    unittest.main()
