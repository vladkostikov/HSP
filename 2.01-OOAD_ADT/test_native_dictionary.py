from unittest import TestCase
from native_dictionary import NativeDictionary


class Test(TestCase):
    def test_init(self):
        dictionary = NativeDictionary(42)

        self.assertEqual(dictionary.PUT_ERR, dictionary.get_put_status())
        self.assertEqual(dictionary.GET_ERR, dictionary.get_get_status())
        self.assertEqual(dictionary.REMOVE_ERR, dictionary.get_remove_status())

    def test_put(self):
        dictionary = NativeDictionary(5)

        self.assertIsNone(dictionary.put("", "1"))
        self.assertEqual(dictionary.PUT_OK, dictionary.get_put_status())
        self.assertEqual("1", dictionary.get(""))

        self.assertIsNone(dictionary.put("a", "2"))
        self.assertEqual(dictionary.PUT_OK, dictionary.get_put_status())
        self.assertEqual("2", dictionary.get("a"))

        self.assertIsNone(dictionary.put("b", "3"))
        self.assertEqual(dictionary.PUT_OK, dictionary.get_put_status())
        self.assertEqual("3", dictionary.get("b"))

        self.assertIsNone(dictionary.put("c", "4"))
        self.assertEqual(dictionary.PUT_OK, dictionary.get_put_status())
        self.assertEqual("4", dictionary.get("c"))

        self.assertIsNone(dictionary.put("d", "5"))
        self.assertEqual(dictionary.PUT_OK, dictionary.get_put_status())
        self.assertEqual("5", dictionary.get("d"))

        self.assertIsNone(dictionary.put("b", "66"))
        self.assertEqual(dictionary.PUT_OK, dictionary.get_put_status())
        self.assertEqual("66", dictionary.get("b"))

        self.assertIsNone(dictionary.put("c", "77"))
        self.assertEqual(dictionary.PUT_OK, dictionary.get_put_status())
        self.assertEqual("77", dictionary.get("c"))

        self.assertIsNone(dictionary.put("e", "6"))
        self.assertEqual(dictionary.PUT_ERR, dictionary.get_put_status())
        self.assertIsNone(dictionary.get("e"))

    def test_remove(self):
        dictionary = NativeDictionary(5)

        self.assertIsNone(dictionary.remove("a"))
        self.assertEqual(dictionary.REMOVE_ERR, dictionary.get_remove_status())
        self.assertIsNone(dictionary.get("a"))

        self.assertIsNone(dictionary.put("b", "2"))
        self.assertEqual(dictionary.PUT_OK, dictionary.get_put_status())
        self.assertTrue(dictionary.is_key("b"))
        self.assertEqual("2", dictionary.get("b"))

        self.assertIsNone(dictionary.remove("b"))
        self.assertEqual(dictionary.REMOVE_OK, dictionary.get_remove_status())
        self.assertFalse(dictionary.is_key("b"))
        self.assertIsNone(dictionary.get("b"))

    def test_is_key(self):
        dictionary = NativeDictionary(5)

        self.assertFalse(dictionary.get("a"))
        self.assertIsNone(dictionary.put("a", "1"))
        self.assertEqual(dictionary.PUT_OK, dictionary.get_put_status())
        self.assertTrue(dictionary.is_key("a"))

        self.assertFalse(dictionary.get("b"))
        self.assertIsNone(dictionary.put("b", "2"))
        self.assertEqual(dictionary.PUT_OK, dictionary.get_put_status())
        self.assertTrue(dictionary.is_key("b"))

        self.assertFalse(dictionary.get("c"))
        self.assertIsNone(dictionary.put("c", "3"))
        self.assertEqual(dictionary.PUT_OK, dictionary.get_put_status())
        self.assertTrue(dictionary.is_key("c"))

    def test_get(self):
        dictionary = NativeDictionary(5)

        self.assertIsNone(dictionary.get("a"))
        self.assertEqual(dictionary.GET_ERR, dictionary.get_get_status())
        self.assertIsNone(dictionary.put("a", "1"))
        self.assertEqual(dictionary.PUT_OK, dictionary.get_put_status())
        self.assertEqual("1", dictionary.get("a"))
        self.assertEqual(dictionary.GET_OK, dictionary.get_get_status())

        self.assertIsNone(dictionary.get("b"))
        self.assertEqual(dictionary.GET_ERR, dictionary.get_get_status())
        self.assertIsNone(dictionary.put("b", "2"))
        self.assertEqual(dictionary.PUT_OK, dictionary.get_put_status())
        self.assertEqual("2", dictionary.get("b"))
        self.assertEqual(dictionary.GET_OK, dictionary.get_get_status())

        self.assertIsNone(dictionary.get("c"))
        self.assertEqual(dictionary.GET_ERR, dictionary.get_get_status())
        self.assertIsNone(dictionary.put("c", "3"))
        self.assertEqual(dictionary.PUT_OK, dictionary.get_put_status())
        self.assertEqual("3", dictionary.get("c"))
        self.assertEqual(dictionary.GET_OK, dictionary.get_get_status())
