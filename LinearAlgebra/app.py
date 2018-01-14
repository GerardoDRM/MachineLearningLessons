from vector import Vector
from unittest import TestCase

def test_vector(TestCase):

    def test_eq(self):
        # Testing vector class
        self.assertTrue(Vector([1,2,3]), Vector([1,2,3]))
        self.assertFalse(Vector([1,2,3]), Vector([-1,2,3]))

if __name__ == "__main__":
    unittest.main()
