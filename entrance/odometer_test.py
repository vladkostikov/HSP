import unittest
from odometer import odometer

class MyTestCase(unittest.TestCase):
    def test_squirrel(self):
        self.assertEqual(odometer([0,0]), 0)
        self.assertEqual(odometer([10,1]), 10)
        self.assertEqual(odometer([10,1,20,2]), 30)
        self.assertEqual(odometer([10,1,20,2,30,3]), 60)
        self.assertEqual(odometer([10,1,20,2,30,3,40,5]), 140)
        self.assertEqual(odometer([10,1,20,2,30,3,40,5,10,10]), 190)

if __name__ == '__main__':
    unittest.main()
