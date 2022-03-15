from math import pi


class MyMath():
    @classmethod
    def circle_len(cls, radius : int) -> float:
        return 2 * pi * radius

    @classmethod
    def circle_sq(cls, radius : int) -> float:
        return pi * radius**2

    @classmethod
    def sphere_sq(cls, radius : int) -> float:
        return 4 * pi * radius**2

    @classmethod
    def cube_volume(cls, length : int) -> int:
        return length**3


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_volume(length=4)

print(res_1)
print(res_2)
print(res_3)
