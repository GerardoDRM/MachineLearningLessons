from vector import Vector
from unittest import TestCase, main

class TestVector(TestCase):

    def test_eq(self):
        # Testing vector class
        self.assertTrue(Vector([1,2,3])==Vector([1,2,3]))
        self.assertFalse(Vector([1,2,3])==Vector([-1,2,3]))

    def test_ops(self):
        # Operating vectors
        self.assertTrue(Vector([8.218, -9.341]) + Vector([-1.129,2.111]) == (7.089, -7.229999999999999))
        self.assertTrue(Vector([7.119, 8.215]) - Vector([-8.223,0.878]) == (15.342, 7.337))
        v_mult = Vector([1.671, -1.012, -0.318])
        self.assertTrue(v_mult.scalar_mult(7.41) == (12.38211, -7.49892, -2.35638))

if __name__ == "__main__":
    main()
