from math import acos, degrees

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        return tuple([val + self.coordinates[idx] for idx, val in enumerate(v.coordinates)])

    def __sub__(self, v):
        return tuple([self.coordinates[idx] - val for idx, val in enumerate(v.coordinates)])

    def scalar_mult(self, v):
        return tuple([val * v  for val in self.coordinates])

    def magnitude(self):
        return sum(val**2 for val in self.coordinates) ** (0.5)

    def direction(self):
        # Get magnitude
        mag = self.magnitude()
        return tuple([val * 1/mag  for val in self.coordinates])

    def dot_product(self, v):
        return sum([val * self.coordinates[idx] for idx, val in enumerate(v.coordinates)])

    def angle(self, v):
        dot = self.dot_product(v)
        radians = acos(dot / (self.magnitude() * v.magnitude()))
        d = degrees(radians)
        return (radians, d)

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v):
        return (self.is_zero() or
                v.is_zero() or self.angle()[0] == 0 or
                self.angle_with(v) == pi)

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance
