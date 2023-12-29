from unittest import TestCase
from native_dictionary import NativeDictionary


class TestNativeDictionary(TestCase):
    def test_hash_fun(self):
        native_dictionary = NativeDictionary(100)
        self.assertEqual(0, native_dictionary.hash_fun(''))
        self.assertEqual(86, native_dictionary.hash_fun('ab'))
        self.assertEqual(97, native_dictionary.hash_fun('ba'))

    def test_is_key(self):
        native_dictionary = NativeDictionary(100)
        self.assertFalse(native_dictionary.is_key(''))
        self.assertFalse(native_dictionary.is_key('key'))
        self.assertEqual('value', native_dictionary.values[native_dictionary.put('key', 'value')])
        self.assertEqual('value2', native_dictionary.values[native_dictionary.put('key2', 'value2')])
        self.assertEqual('value3', native_dictionary.values[native_dictionary.put('key3', 'value3')])
        self.assertTrue(native_dictionary.is_key('key'))
        self.assertTrue(native_dictionary.is_key('key2'))
        self.assertTrue(native_dictionary.is_key('key3'))
        self.assertFalse(native_dictionary.is_key('key4'))

    def test_put(self):
        native_dictionary = NativeDictionary(100)
        self.assertIsNone(native_dictionary.get('key'))
        self.assertEqual('value', native_dictionary.values[native_dictionary.put('key', 'value')])
        self.assertEqual('value2', native_dictionary.values[native_dictionary.put('key2', 'value2')])
        self.assertEqual('value3', native_dictionary.values[native_dictionary.put('key3', 'value3')])
        self.assertEqual('value', native_dictionary.get('key'))
        self.assertEqual('value2', native_dictionary.get('key2'))
        self.assertEqual('value3', native_dictionary.get('key3'))

        self.assertEqual('value20', native_dictionary.values[native_dictionary.put('key2', 'value20')])
        self.assertEqual('value20', native_dictionary.get('key2'))
        self.assertEqual('value20', native_dictionary.values[native_dictionary.put('key3', 'value20')])
        self.assertEqual('value20', native_dictionary.get('key3'))

        for i in range(50):
            self.assertEqual(str(i ** 2), native_dictionary.values[native_dictionary.put(str(i), str(i ** 2))])
            self.assertEqual(str(i), native_dictionary.slots[native_dictionary.find(str(i))])
            self.assertEqual(str(i ** 2), native_dictionary.values[native_dictionary.find(str(i))])

    def test_get(self):
        native_dictionary = NativeDictionary(100)
        self.assertIsNone(native_dictionary.get('key'))
        self.assertEqual('value', native_dictionary.values[native_dictionary.put('key', 'value')])
        self.assertEqual('value2', native_dictionary.values[native_dictionary.put('key2', 'value2')])
        self.assertEqual('value3', native_dictionary.values[native_dictionary.put('key3', 'value3')])
        self.assertEqual('value', native_dictionary.get('key'))
        self.assertEqual('value2', native_dictionary.get('key2'))
        self.assertEqual('value3', native_dictionary.get('key3'))
        self.assertIsNone(native_dictionary.get('key4'))
