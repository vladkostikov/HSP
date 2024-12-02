from unittest import TestCase
from bounded_stack import BoundedStack


class Test(TestCase):
    def test_default_bounded_stack(self):
        stack = BoundedStack()
        self.assertEqual(stack.PUSH_NIL, stack.get_push_status())
        self.assertEqual(stack.POP_NIL, stack.get_pop_status())
        self.assertEqual(stack.PEEK_NIL, stack.get_peek_status())

        self.assertEqual(0, stack.size())

        self.assertEqual(0, stack.peek())
        self.assertEqual(stack.PEEK_ERR, stack.get_peek_status())

        self.assertIsNone(stack.pop())
        self.assertEqual(stack.POP_ERR, stack.get_pop_status())

        for el in range(32):
            self.assertIsNone(stack.push(el))
            self.assertEqual(stack.PUSH_OK, stack.get_push_status())
            self.assertEqual(el, stack.peek())
            self.assertEqual(stack.PEEK_OK, stack.get_peek_status())

        self.assertEqual(31, stack.peek())
        self.assertEqual(stack.PEEK_OK, stack.get_peek_status())

        self.assertIsNone(stack.push(42))
        self.assertEqual(stack.PUSH_ERR, stack.get_push_status())
        self.assertEqual(31, stack.peek())
        self.assertEqual(stack.PEEK_OK, stack.get_peek_status())

        self.assertIsNone(stack.pop())
        self.assertEqual(stack.POP_OK, stack.get_pop_status())
        self.assertEqual(30, stack.peek())
        self.assertEqual(stack.PEEK_OK, stack.get_peek_status())

        self.assertEqual(31, stack.size())
        self.assertIsNone(stack.clear())
        self.assertEqual(0, stack.size())

    def test_non_default_bounded_stack(self):
        stack = BoundedStack(10)
        self.assertEqual(stack.PUSH_NIL, stack.get_push_status())
        self.assertEqual(stack.POP_NIL, stack.get_pop_status())
        self.assertEqual(stack.PEEK_NIL, stack.get_peek_status())

        self.assertEqual(0, stack.size())

        self.assertEqual(0, stack.peek())
        self.assertEqual(stack.PEEK_ERR, stack.get_peek_status())

        self.assertIsNone(stack.pop())
        self.assertEqual(stack.POP_ERR, stack.get_pop_status())

        for el in range(10):
            self.assertIsNone(stack.push(el))
            self.assertEqual(stack.PUSH_OK, stack.get_push_status())

        self.assertEqual(9, stack.peek())
        self.assertEqual(stack.PEEK_OK, stack.get_peek_status())

        self.assertIsNone(stack.push(42))
        self.assertEqual(stack.PUSH_ERR, stack.get_push_status())
        self.assertEqual(9, stack.peek())
        self.assertEqual(stack.PEEK_OK, stack.get_peek_status())

        self.assertIsNone(stack.pop())
        self.assertEqual(stack.POP_OK, stack.get_pop_status())
        self.assertEqual(8, stack.peek())
        self.assertEqual(stack.PEEK_OK, stack.get_peek_status())

        self.assertEqual(9, stack.size())
        self.assertIsNone(stack.clear())
        self.assertEqual(0, stack.size())
