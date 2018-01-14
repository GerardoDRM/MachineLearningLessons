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
