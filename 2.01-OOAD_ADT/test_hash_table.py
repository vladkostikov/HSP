from unittest import TestCase
from hash_table import HashTable


class Test(TestCase):
    def test_init(self):
        hash_table = HashTable(42)

        self.assertEqual(hash_table.PUT_ERR, hash_table.get_put_status())
        self.assertEqual(hash_table.SEEK_SLOT_ERR, hash_table.get_seek_slot_status())

    def test_hash_func(self):
        hash_table = HashTable(100)

        self.assertEqual(0, hash_table.hash_fun(""))
        self.assertEqual(66, hash_table.hash_fun("A"))
        self.assertEqual(67, hash_table.hash_fun("B"))
        self.assertEqual(2, hash_table.hash_fun("AB"))
        self.assertEqual(12, hash_table.hash_fun("ABC"))

    def test_seek_slot(self):
        hash_table = HashTable(100)

        self.assertEqual(0, hash_table.seek_slot(""))
        self.assertEqual(hash_table.SEEK_SLOT_OK, hash_table.get_seek_slot_status())
        self.assertEqual(66, hash_table.seek_slot("A"))
        self.assertEqual(hash_table.SEEK_SLOT_OK, hash_table.get_seek_slot_status())
        self.assertEqual(2, hash_table.seek_slot("AB"))
        self.assertEqual(hash_table.SEEK_SLOT_OK, hash_table.get_seek_slot_status())
        self.assertEqual(12, hash_table.seek_slot("ABC"))
        self.assertEqual(hash_table.SEEK_SLOT_OK, hash_table.get_seek_slot_status())

        self.assertIsNone(hash_table.put("A"))
        self.assertEqual(hash_table.PUT_OK, hash_table.get_put_status())
        self.assertEqual(66, hash_table.seek_slot("A"))
        self.assertEqual(hash_table.SEEK_SLOT_EXIST, hash_table.get_seek_slot_status())

    def test_put(self):
        hash_table = HashTable(5)

        self.assertIsNone(hash_table.put(""))
        self.assertEqual(hash_table.PUT_OK, hash_table.get_put_status())
        self.assertIsNone(hash_table.put("a"))
        self.assertEqual(hash_table.PUT_OK, hash_table.get_put_status())
        self.assertIsNone(hash_table.put("b"))
        self.assertEqual(hash_table.PUT_OK, hash_table.get_put_status())
        self.assertIsNone(hash_table.put("c"))
        self.assertEqual(hash_table.PUT_OK, hash_table.get_put_status())
        self.assertIsNone(hash_table.put("d"))
        self.assertEqual(hash_table.PUT_OK, hash_table.get_put_status())
        self.assertIsNone(hash_table.put("b"))
        self.assertEqual(hash_table.PUT_EXIST, hash_table.get_put_status())
        self.assertIsNone(hash_table.put("c"))
        self.assertEqual(hash_table.PUT_EXIST, hash_table.get_put_status())
        self.assertIsNone(hash_table.put("e"))
        self.assertEqual(hash_table.PUT_ERR, hash_table.get_put_status())

    def test_find(self):
        hash_table = HashTable(5)

        self.assertFalse(hash_table.find("a"))
        self.assertIsNone(hash_table.put("a"))
        self.assertEqual(hash_table.PUT_OK, hash_table.get_put_status())
        self.assertTrue(hash_table.find("a"))

        self.assertFalse(hash_table.find("b"))
        self.assertIsNone(hash_table.put("b"))
        self.assertEqual(hash_table.PUT_OK, hash_table.get_put_status())
        self.assertTrue(hash_table.find("b"))

        self.assertFalse(hash_table.find("c"))
        self.assertIsNone(hash_table.put("c"))
        self.assertEqual(hash_table.PUT_OK, hash_table.get_put_status())
        self.assertTrue(hash_table.find("c"))
