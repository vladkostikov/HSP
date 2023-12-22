from unittest import TestCase
from stack_from_linked_list import Stack
from stack_from_linked_list import check_balance_of_brackets


class TestStack(TestCase):
    def test_size(self):
        stack = Stack()
        self.assertEqual(0, stack.size())
        stack.push(10)
        self.assertEqual(1, stack.size())
        stack.push(20)
        stack.push(30)
        stack.push(40)
        stack.push(50)
        self.assertEqual(5, stack.size())

    def test_pop(self):
        stack = Stack()
        self.assertIsNone(stack.pop())
        stack.push(10)
        stack.push(20)
        stack.push(30)
        stack.push(40)
        stack.push(50)
        self.assertEqual(5, stack.size())
        self.assertEqual(50, stack.pop())
        self.assertEqual(4, stack.size())
        self.assertEqual(40, stack.peek())

    def test_push(self):
        stack = Stack()
        self.assertEqual(10, stack.push(10))
        self.assertEqual(20, stack.push(20))
        self.assertEqual(30, stack.push(30))
        self.assertEqual(40, stack.push(40))
        self.assertEqual(50, stack.push(50))
        self.assertEqual(5, stack.size())
        self.assertEqual(50, stack.data.tail.prev.value)
        self.assertEqual(10, stack.data.head.next.value)

    def test_peek(self):
        stack = Stack()
        self.assertIsNone(stack.peek())
        stack.push(10)
        self.assertEqual(10, stack.peek())
        stack.push(20)
        self.assertEqual(20, stack.peek())

    def test_stack_with_100_000_elements(self):
        stack = Stack()
        for element in range(100_000):
            self.assertEqual(element, stack.push(element))
            self.assertEqual(element + 1, stack.size())
            self.assertEqual(element, stack.peek())
        for element in range(100_000 - 1):
            self.assertEqual(100_000 - element - 1, stack.pop())
            self.assertEqual(100_000 - element - 1, stack.size())
            self.assertEqual(100_000 - element - 2, stack.peek())
        self.assertEqual(0, stack.pop())
        self.assertEqual(0, stack.size())
        self.assertIsNone(stack.peek())

    def test_check_balance_of_brackets(self):
        self.assertTrue(check_balance_of_brackets("()"))
        self.assertTrue(check_balance_of_brackets("(()((())()))"))
        self.assertTrue(check_balance_of_brackets("(()()())"))
        self.assertTrue(check_balance_of_brackets("((()(()))())"))
        self.assertTrue(check_balance_of_brackets(""))
        self.assertFalse(check_balance_of_brackets("("))
        self.assertFalse(check_balance_of_brackets(")"))
        self.assertFalse(check_balance_of_brackets(")())"))
        self.assertFalse(check_balance_of_brackets("())("))
        self.assertFalse(check_balance_of_brackets("(()()(()"))
        self.assertFalse(check_balance_of_brackets("())("))
        self.assertFalse(check_balance_of_brackets("))(("))
        self.assertFalse(check_balance_of_brackets("((())"))
