from unittest import TestCase
from bloom_filter import BloomFilter


class Test(TestCase):
    def test_bloom_filter(self):
        bloom_filter = BloomFilter(32)
        self.assertFalse(bloom_filter.is_value("0123456789"))
        self.assertIsNone(bloom_filter.put("0123456789"))
        self.assertTrue(bloom_filter.is_value("0123456789"))

        self.assertFalse(bloom_filter.is_value("1234567890"))
        self.assertIsNone(bloom_filter.put("1234567890"))
        self.assertTrue(bloom_filter.is_value("1234567890"))

        self.assertFalse(bloom_filter.is_value("2345678901"))
        self.assertIsNone(bloom_filter.put("2345678901"))
        self.assertTrue(bloom_filter.is_value("2345678901"))

        self.assertFalse(bloom_filter.is_value("3456789012"))
        self.assertIsNone(bloom_filter.put("3456789012"))
        self.assertTrue(bloom_filter.is_value("3456789012"))

        self.assertFalse(bloom_filter.is_value("4567890123"))
        self.assertIsNone(bloom_filter.put("4567890123"))
        self.assertTrue(bloom_filter.is_value("4567890123"))

        self.assertFalse(bloom_filter.is_value("5678901234"))
        self.assertIsNone(bloom_filter.put("5678901234"))
        self.assertTrue(bloom_filter.is_value("5678901234"))

        self.assertFalse(bloom_filter.is_value("6789012345"))
        self.assertIsNone(bloom_filter.put("6789012345"))
        self.assertTrue(bloom_filter.is_value("6789012345"))

        self.assertFalse(bloom_filter.is_value("7890123456"))
        self.assertIsNone(bloom_filter.put("7890123456"))
        self.assertTrue(bloom_filter.is_value("7890123456"))

        self.assertFalse(bloom_filter.is_value("8901234567"))
        self.assertIsNone(bloom_filter.put("8901234567"))
        self.assertTrue(bloom_filter.is_value("8901234567"))

        self.assertFalse(bloom_filter.is_value("9012345678"))
        self.assertIsNone(bloom_filter.put("9012345678"))
        self.assertTrue(bloom_filter.is_value("9012345678"))
