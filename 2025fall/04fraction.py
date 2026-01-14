def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, fraction):
        new_num = self.num * fraction.den + self.den * fraction.num
        new_den = self.den * fraction.den
        da = gcd(new_num, new_den)
        new_num, new_den = int(new_num//da), int(new_den/da)

        return Fraction(new_num, new_den)

a, b, c, d = map(int, input().split())
f1 = Fraction(a, b)
f2 = Fraction(c, d)
print(f1 + f2)
