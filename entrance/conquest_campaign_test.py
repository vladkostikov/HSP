import unittest
from conquest_campaign import ConquestCampaign

class MyTestCase(unittest.TestCase):
    def test_conquest_campaign(self):
        self.assertEqual(ConquestCampaign(1,1,1,[1,1]), 1)
        self.assertEqual(ConquestCampaign(1,2,1,[1,1]), 2)
        self.assertEqual(ConquestCampaign(2,2,1,[1,1]), 3)
        self.assertEqual(ConquestCampaign(3,4,1,[2,2]), 4)
        self.assertEqual(ConquestCampaign(3,4,2,[2,2, 3,4]), 3)
        self.assertEqual(ConquestCampaign(3,4,2,[2,2, 2,2]), 4)
        self.assertEqual(ConquestCampaign(5,5,1,[3,3]), 5)
        self.assertEqual(ConquestCampaign(4,4,2,[1,1, 4,4]), 4)
        self.assertEqual(ConquestCampaign(11,11,1,[6,6]), 11)
if __name__ == '__main__':
    unittest.main()
