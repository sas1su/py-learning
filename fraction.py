def gcd(m, n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n
        
class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    
    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)
    #check both the num and den are eq using __eq__ override
    def __eq__(self, otherfraction):
        first = self.num * otherfraction.den
        second = self.den * otherfraction.num
        return first == second
    #subtraction
    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    #multiplication
    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)   

    def __lt__(self, otherfraction):
        first = self.num * otherfraction.den
        second = self.den * otherfraction.num
        return first < second

myf = Fraction(3,5)
myf.show()
print(myf)
print(myf.__str__())

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)

x = Fraction(2, 4)
y = Fraction(3, 5)
print(x == y)

print("sub:", x - y)
print("mul:", x*y)
print("lt:", x<y)
print("lt:", y<x)