class Complex:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __iadd__(self, other):
        self.left += other.left
        self.right += other.right
        return Complex(self.left, self.right)

    def __isub__(self, other):
        self.left -= other.left
        self.right -= other.right
        return Complex(self.left, self.right)

    def __repr__(self):
        return f'{self.left}j {"+" if self.right > 0 else "-"} {abs(self.right)}i'


a1 = Complex(5, 4)
a2 = Complex(4, 3)
a1 += a2
print(a1)
a1 -= a2
print(a1)
a1 -= a2
print(a1)