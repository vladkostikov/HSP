from unittest import TestCase
from stack import Stack


class TestStack(TestCase):
    def test_size(self):
        stack = Stack()
        stack.push(10)
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
        self.assertEqual(50, stack.stack[0])
        self.assertEqual(10, stack.stack[-1])

    def test_peek(self):
        stack = Stack()
        self.assertIsNone(stack.peek())
        stack.push(10)
        self.assertEqual(10, stack.peek())
        stack.push(20)
        self.assertEqual(20, stack.peek())

    def test_check_balance_of_brackets(self):
        self.assertTrue(Stack().check_balance_of_brackets("()"))
        self.assertTrue(Stack().check_balance_of_brackets("(()((())()))"))
        self.assertTrue(Stack().check_balance_of_brackets("(()()())"))
        self.assertTrue(Stack().check_balance_of_brackets("((()(()))())"))
        self.assertTrue(Stack().check_balance_of_brackets(""))
        self.assertFalse(Stack().check_balance_of_brackets("("))
        self.assertFalse(Stack().check_balance_of_brackets(")"))
        self.assertFalse(Stack().check_balance_of_brackets(")())"))
        self.assertFalse(Stack().check_balance_of_brackets("())("))
        self.assertFalse(Stack().check_balance_of_brackets("(()()(()"))
        self.assertFalse(Stack().check_balance_of_brackets("())("))
        self.assertFalse(Stack().check_balance_of_brackets("))(("))
        self.assertFalse(Stack().check_balance_of_brackets("((())"))
