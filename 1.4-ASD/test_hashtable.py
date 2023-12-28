from unittest import TestCase
from hashtable import HashTable


class TestHashTable(TestCase):
    def test_hash_fun(self):
        hashtable = HashTable(17, 3)
        self.assertEqual(0, hashtable.hash_fun(''))
        self.assertEqual(10, hashtable.hash_fun('a'))

        letter_r = chr(ord('a') + hashtable.size)
        self.assertEqual(10, hashtable.hash_fun(letter_r))
        self.assertEqual(14, hashtable.hash_fun('abc'))
        self.assertEqual(14, hashtable.hash_fun('abc'))

    def test_seek_slot(self):
        hashtable = HashTable(17, 3)
        self.assertEqual(14, hashtable.seek_slot('abc'))
        self.assertEqual(14, hashtable.seek_slot('abcc'))
        self.assertEqual(14, hashtable.put('abc'))
        self.assertEqual(0, hashtable.seek_slot('abcc'))

        for i in range(100, 116):
            self.assertIsNotNone(hashtable.put(chr(i)))
        self.assertEqual(17, hashtable.size)
        self.assertIsNone(hashtable.seek_slot('any'))

    def test_put(self):
        hashtable = HashTable(17, 3)
        self.assertEqual(14, hashtable.seek_slot('abc'))
        self.assertEqual(14, hashtable.put('abc'))
        self.assertEqual('abc', hashtable.slots[14])

        self.assertEqual(14, hashtable.hash_fun('abcc'))
        self.assertEqual(0, hashtable.seek_slot('abcc'))
        self.assertEqual(0, hashtable.put('abcc'))
        self.assertEqual('abcc', hashtable.slots[0])

        for i in range(100, 115):
            self.assertIsNotNone(hashtable.put(chr(i)))
        self.assertEqual(17, hashtable.size)
        self.assertIsNone(hashtable.put('any'))

    def test_find(self):
        hashtable = HashTable(17, 3)
        self.assertIsNone(hashtable.find('abc'))
        self.assertEqual(14, hashtable.put('abc'))
        self.assertEqual(0, hashtable.put('abcc'))
        self.assertEqual(14, hashtable.find('abc'))
        self.assertEqual(0, hashtable.find('abcc'))
        self.assertIsNone(hashtable.find('abcd'))
