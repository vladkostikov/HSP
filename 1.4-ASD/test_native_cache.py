from unittest import TestCase
from native_cache import NativeCache


class TestNativeCache(TestCase):
    def test_hash_fun(self):
        native_cache = NativeCache(100)
        self.assertEqual(0, native_cache.hash_fun(''))
        self.assertEqual(86, native_cache.hash_fun('ab'))
        self.assertEqual(97, native_cache.hash_fun('ba'))

    def test_is_key(self):
        native_cache = NativeCache(100)
        self.assertFalse(native_cache.is_key(''))
        self.assertFalse(native_cache.is_key('key'))
        self.assertEqual('value', native_cache.values[native_cache.put('key', 'value')])
        self.assertEqual('value2', native_cache.values[native_cache.put('key2', 'value2')])
        self.assertEqual('value3', native_cache.values[native_cache.put('key3', 'value3')])
        self.assertTrue(native_cache.is_key('key'))
        self.assertTrue(native_cache.is_key('key2'))
        self.assertTrue(native_cache.is_key('key3'))
        self.assertFalse(native_cache.is_key('key4'))

    def test_put(self):
        native_cache = NativeCache(100)
        self.assertIsNone(native_cache.get('key'))
        self.assertEqual('value', native_cache.values[native_cache.put('key', 'value')])
        self.assertEqual('value2', native_cache.values[native_cache.put('key2', 'value2')])
        self.assertEqual('value3', native_cache.values[native_cache.put('key3', 'value3')])
        self.assertEqual('value', native_cache.get('key'))
        self.assertEqual('value2', native_cache.get('key2'))
        self.assertEqual('value3', native_cache.get('key3'))

        self.assertEqual('value20', native_cache.values[native_cache.put('key2', 'value20')])
        self.assertEqual('value20', native_cache.get('key2'))
        self.assertEqual('value20', native_cache.values[native_cache.put('key3', 'value20')])
        self.assertEqual('value20', native_cache.get('key3'))

        for i in range(50):
            self.assertEqual((i ** 2), native_cache.values[native_cache.put(str(i), (i ** 2))])
            self.assertEqual(str(i), native_cache.slots[native_cache.find(str(i))])
            self.assertEqual((i ** 2), native_cache.values[native_cache.find(str(i))])

        native_cache = NativeCache(100)
        for i in range(50):
            self.assertIsNotNone(native_cache.put(str(i), i))
            self.assertIsNotNone(native_cache.get(str(i)))
            self.assertIsNotNone(native_cache.get(str(i)))
        for i in range(50, 100):
            self.assertIsNotNone(native_cache.put(str(i), i))
        for i in range(100, 120):
            self.assertIsNotNone(native_cache.put(str(i), i))
            self.assertIsNotNone(native_cache.is_key(str(i)))

        for i in range(1000, 5000):
            self.assertIsNotNone(native_cache.put(str(i), i))

        # В кэше должны остаться значения от 0 до 50, и от 100 до 120, т.к. к ним были обращения.
        for i in range(50):
            self.assertTrue(native_cache.is_key(str(i)))
        for i in range(100, 120):
            self.assertTrue(native_cache.is_key(str(i)))

    def test_get(self):
        native_cache = NativeCache(100)
        self.assertIsNone(native_cache.get('key'))
        self.assertEqual('value', native_cache.values[native_cache.put('key', 'value')])
        self.assertEqual('value2', native_cache.values[native_cache.put('key2', 'value2')])
        self.assertEqual('value3', native_cache.values[native_cache.put('key3', 'value3')])
        self.assertEqual('value', native_cache.get('key'))
        self.assertEqual('value2', native_cache.get('key2'))
        self.assertEqual('value3', native_cache.get('key3'))
        self.assertIsNone(native_cache.get('key4'))

    def test_record_request(self):
        native_cache = NativeCache(100)
        self.assertEqual('value', native_cache.values[native_cache.put('key', 'value')])
        self.assertEqual('value2', native_cache.values[native_cache.put('key2', 'value2')])
        self.assertEqual('value3', native_cache.values[native_cache.put('key3', 'value3')])

        self.assertEqual(1, native_cache.hits[native_cache.find('key')])
        self.assertEqual(1, native_cache.hits[native_cache.find('key2')])
        self.assertEqual(1, native_cache.hits[native_cache.find('key3')])

        self.assertEqual(2, native_cache.hits[native_cache.find('key')])
        self.assertEqual('value', native_cache.get('key'))
        self.assertEqual(4, native_cache.hits[native_cache.find('key')])

    def test_find_slot_with_minimum_queries(self):
        native_cache = NativeCache(100)
        for i in range(100):
            self.assertEqual((i ** 2), native_cache.values[native_cache.put(str(i), (i ** 2))])

        self.assertEqual(15, native_cache.hash_fun('abc'))
        self.assertEqual(15, native_cache.find_slot_to_insert('abc'))

        for i in range(15):
            self.assertIsNotNone(native_cache.get(native_cache.slots[i]))
            self.assertEqual(15, native_cache.find_slot_to_insert('abc'))
        self.assertIsNotNone(native_cache.get(native_cache.slots[15]))
        self.assertEqual(22, native_cache.find_slot_to_insert('abc'))

        for i in range(16, 22):
            self.assertIsNotNone(native_cache.is_key(native_cache.slots[i]))
            self.assertEqual(22, native_cache.find_slot_to_insert('abc'))
        self.assertIsNotNone(native_cache.get(native_cache.slots[22]))
        self.assertEqual(29, native_cache.find_slot_to_insert('abc'))
