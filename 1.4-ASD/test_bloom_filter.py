from unittest import TestCase
from bloom_filter import BloomFilter


class TestBloomFilter(TestCase):
    def test_hash1(self):
        bloom_filter = BloomFilter(32)
        self.assertEqual(13, bloom_filter.hash1("0123456789"))
        self.assertEqual(29, bloom_filter.hash1("1234567890"))

        self.assertEqual(13, bloom_filter.hash1("2345678901"))
        self.assertEqual(29, bloom_filter.hash1("3456789012"))
        self.assertEqual(13, bloom_filter.hash1("4567890123"))
        self.assertEqual(29, bloom_filter.hash1("5678901234"))
        self.assertEqual(13, bloom_filter.hash1("6789012345"))
        self.assertEqual(29, bloom_filter.hash1("7890123456"))
        self.assertEqual(13, bloom_filter.hash1("8901234567"))
        self.assertEqual(29, bloom_filter.hash1("9012345678"))

    def test_hash2(self):
        bloom_filter = BloomFilter(32)
        self.assertEqual(5, bloom_filter.hash2("0123456789"))
        self.assertEqual(27, bloom_filter.hash2("1234567890"))

        self.assertEqual(5, bloom_filter.hash2("2345678901"))
        self.assertEqual(27, bloom_filter.hash2("3456789012"))
        self.assertEqual(5, bloom_filter.hash2("4567890123"))
        self.assertEqual(27, bloom_filter.hash2("5678901234"))
        self.assertEqual(5, bloom_filter.hash2("6789012345"))
        self.assertEqual(27, bloom_filter.hash2("7890123456"))
        self.assertEqual(5, bloom_filter.hash2("8901234567"))
        self.assertEqual(27, bloom_filter.hash2("9012345678"))

    def test_add(self):
        bloom_filter = BloomFilter(32)
        self.assertEqual(0, bloom_filter.filter)

        self.assertEqual("0123456789", bloom_filter.add("0123456789"))
        self.assertEqual(8224, bloom_filter.filter)
        self.assertEqual("0b10000000100000", bin(bloom_filter.filter))

        self.assertEqual("1234567890", bloom_filter.add("1234567890"))
        self.assertEqual(671096864, bloom_filter.filter)
        self.assertEqual("0b101000000000000010000000100000", bin(bloom_filter.filter))


    def test_is_value(self):
        bloom_filter = BloomFilter(32)
        self.assertFalse(bloom_filter.is_value("0123456789"))
        self.assertFalse(bloom_filter.is_value("1234567890"))
        bloom_filter.add("0123456789")
        self.assertTrue(bloom_filter.is_value("0123456789"))
        bloom_filter.add("1234567890")
        self.assertTrue(bloom_filter.is_value("1234567890"))

        # Ложноположительные.
        self.assertTrue(bloom_filter.is_value("2345678901"))
        self.assertTrue(bloom_filter.is_value("3456789012"))
        self.assertTrue(bloom_filter.is_value("4567890123"))
        self.assertTrue(bloom_filter.is_value("5678901234"))
        self.assertTrue(bloom_filter.is_value("6789012345"))
        self.assertTrue(bloom_filter.is_value("7890123456"))
        self.assertTrue(bloom_filter.is_value("8901234567"))
        self.assertTrue(bloom_filter.is_value("9012345678"))
