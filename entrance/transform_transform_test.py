from unittest import TestCase
from transform_transform import TransformTransform


class Test(TestCase):
    def test_transform_transform(self):
        self.assertEqual(TransformTransform([1], 1), False)
        self.assertEqual(TransformTransform([1, 2], 2), False)
        self.assertEqual(TransformTransform([1, 2, 3], 3), True)
        self.assertEqual(TransformTransform([1, 2, 3, 4], 4), False)
