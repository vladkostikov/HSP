from unittest import TestCase
from deque import Deque
from deque import is_palindrome


class TestDeque(TestCase):
    def test_add_front(self):
        deque = Deque()
        self.assertEqual(0, deque.size())
        self.assertEqual(10, deque.addFront(10))
        self.assertEqual(10, deque.storage.head.next.value)
        self.assertEqual(1, deque.size())
        self.assertEqual(20, deque.addFront(20))
        self.assertEqual(20, deque.storage.head.next.value)
        self.assertEqual(2, deque.size())

    def test_add_tail(self):
        deque = Deque()
        self.assertEqual(0, deque.size())
        self.assertEqual(10, deque.addTail(10))
        self.assertEqual(10, deque.storage.tail.prev.value)
        self.assertEqual(1, deque.size())
        self.assertEqual(20, deque.addTail(20))
        self.assertEqual(20, deque.storage.tail.prev.value)
        self.assertEqual(2, deque.size())

    def test_remove_front(self):
        deque = Deque()
        self.assertEqual(0, deque.size())
        self.assertEqual(10, deque.addFront(10))
        self.assertEqual(20, deque.addFront(20))
        self.assertEqual(20, deque.storage.head.next.value)
        self.assertEqual(30, deque.addTail(30))
        self.assertEqual(40, deque.addTail(40))
        self.assertEqual(40, deque.storage.tail.prev.value)
        self.assertEqual(4, deque.size())

        self.assertEqual(20, deque.removeFront())
        self.assertEqual(10, deque.storage.head.next.value)
        self.assertEqual(3, deque.size())
        self.assertEqual(10, deque.removeFront())
        self.assertEqual(30, deque.storage.head.next.value)
        self.assertEqual(40, deque.storage.tail.prev.value)
        self.assertEqual(2, deque.size())

        self.assertEqual(30, deque.removeFront())
        self.assertEqual(40, deque.removeFront())
        self.assertEqual(0, deque.size())
        self.assertIsNone(deque.removeFront())
        self.assertEqual(0, deque.size())

    def test_remove_tail(self):
        deque = Deque()
        self.assertEqual(0, deque.size())
        self.assertEqual(10, deque.addFront(10))
        self.assertEqual(20, deque.addFront(20))
        self.assertEqual(20, deque.storage.head.next.value)
        self.assertEqual(30, deque.addTail(30))
        self.assertEqual(40, deque.addTail(40))
        self.assertEqual(40, deque.storage.tail.prev.value)
        self.assertEqual(4, deque.size())

        self.assertEqual(40, deque.removeTail())
        self.assertEqual(30, deque.storage.tail.prev.value)
        self.assertEqual(20, deque.storage.head.next.value)
        self.assertEqual(3, deque.size())
        self.assertEqual(30, deque.removeTail())
        self.assertEqual(20, deque.storage.head.next.value)
        self.assertEqual(10, deque.storage.tail.prev.value)
        self.assertEqual(2, deque.size())

        self.assertEqual(10, deque.removeTail())
        self.assertEqual(20, deque.removeTail())
        self.assertEqual(0, deque.size())
        self.assertIsNone(deque.removeTail())
        self.assertEqual(0, deque.size())

    def test_size(self):
        deque = Deque()
        self.assertEqual(0, deque.size())
        for number in range(100_000):
            self.assertEqual(number, deque.addTail(number))
            self.assertEqual(number + 1, deque.size())
        for number in range(100_000):
            self.assertEqual(number, deque.addFront(number))
            self.assertEqual(number + 1 + 100_000, deque.size())
        for number in range(100_000):
            deque.removeFront()
            deque.removeTail()
            self.assertEqual(200_000 - (number + 1) * 2, deque.size())
        self.assertIsNone(deque.removeTail())
        self.assertIsNone(deque.removeFront())
        self.assertEqual(0, deque.size())


class Test(TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("а"))
        self.assertTrue(is_palindrome("аа"))
        self.assertTrue(is_palindrome("аб а"))
        self.assertTrue(is_palindrome("аОбоА"))
        self.assertTrue(is_palindrome("Ш аб аш"))
        self.assertTrue(is_palindrome("20 02 2002"))
        self.assertTrue(is_palindrome("собакА кабос"))
        self.assertTrue(is_palindrome("кабан абак!"))
        self.assertTrue(is_palindrome("Искать такси"))
        self.assertTrue(is_palindrome("Лидер бредил"))
        self.assertTrue(is_palindrome("Муха! О, муха! Велика аки лев! Ах, ум! О ах, ум!"))
        self.assertTrue(is_palindrome("Madam, I’m Adam"))
        self.assertTrue(is_palindrome("Sum summus mus "))
        self.assertFalse(is_palindrome("аб"))
        self.assertFalse(is_palindrome("абв"))
        self.assertFalse(is_palindrome("к ош ка"))
