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

    def test_magnitude_direction(self):
        self.assertTrue(Vector([-0.221, 7.437]).magnitude() == 7.440282924728065)
        self.assertTrue(Vector([5.581, -2.136]).direction() == (0.9339352140866403, -0.35744232526233))

    def test_dotproduct_angles(self):
        self.assertTrue(Vector([7.887, 4.138]).dot_product(Vector([-8.802, 6.776])) == -41.382286)
        self.assertTrue(Vector([3.183, -7.627]).angle(Vector([-2.668, 5.319])) == (3.0720263098372476, 176.01414210682285))


if __name__ == "__main__":
    main()
