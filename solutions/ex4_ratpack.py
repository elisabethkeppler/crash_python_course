from math import floor, isclose, gcd
from ex3_5 import prime_factors

class Rational:
    """
    Class for handling Rational numbers using continued fraction approximation
    with precision control and simplified representation.
    """

    def __init__(self, value, precision=1e-5):
        if not (0 <= precision <= 1):
            raise ValueError("Precision must be between 0 and 1.")

        sign = -1 if value < 0 else 1
        value = abs(value)

        num, den = self._approximate(value, precision)
        num *= sign

        num, den = self._simplify(num, den)

        self.numerator = num
        self.denominator = den
        self.precision = precision

    # representation operators 

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        value = self.numerator / self.denominator
        return f"Rational({value}, precision={self.precision:.0e})"

    # basic dundler functions

    def __abs__(self):
        if self.numerator < 0:
            return Rational(-self.numerator / self.denominator, precision=self.precision)
        else:
            return Rational(self.numerator / self.denominator, precision=self.precision)


    def __float__(self):
        return self.numerator / self.denominator

    def __int__(self):
        return self.numerator // self.denominator

    # Arithmetic operators
    def __add__(self, other):
        if not isinstance(other, Rational): other = Rational(other)
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Rational(num / den, self.precision)

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return Rational(-self.numerator / self.denominator, self.precision)

    def __mul__(self, other):
        if not isinstance(other, Rational): other = Rational(other)
        return Rational((self.numerator * other.numerator) / (self.denominator * other.denominator), self.precision)

    def __truediv__(self, other):
        if not isinstance(other, Rational): other = Rational(other)
        if other.numerator == 0:
            raise ZeroDivisionError("division by zero")
        return Rational((self.numerator * other.denominator) / (self.denominator * other.numerator), self.precision)

    # Comparison operators
    def __eq__(self, other):
        if not isinstance(other, Rational): other = Rational(other)
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):
        return float(self) < float(other)

    def __le__(self, other):
        return float(self) <= float(other)

    def __gt__(self, other):
        return float(self) > float(other)

    def __ge__(self, other):
        return float(self) >= float(other)

    def to_integer_low(self):
        return self.numerator // self.denominator

    def to_integer_upp(self):
        return -(-self.numerator // self.denominator)  # ceil for int


    def _approximate(self, x, precision):
        original = x
        a = floor(x)
        num1, den1 = a, 1
        num2, den2 = 1, 0
        x -= a

        while True:
            approx = num1 / den1
            if x == 0 or isclose(approx, original, abs_tol=precision):
                return num1, den1
            x = 1 / x
            a = floor(x)
            x -= a
            num1, den1, num2, den2 = a * num1 + num2, a * den1 + den2, num1, den1

    def _simplify(self, num, den):
        gcd_num = gcd(num, den)
        return num // gcd_num, den // gcd_num


if __name__ == '__main__':
    # Some quick manual tests
    print(Rational(0.5))
    print(Rational(1.3333, precision=1e-4))
    print(Rational(22/7))
    print(Rational(-0.75))
    print(Rational(0.25) + Rational(0.25))
    print(abs(Rational(-3.14)))