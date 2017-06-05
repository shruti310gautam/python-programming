#Given a list of rational numbers,find their product. 

def product(fracs):
    t = reduce(lambda frac1, frac2 : Fraction(frac1.numerator * frac2.numerator, frac1.denominator * frac2.denominator), fracs)# complete this line with a reduce statement
    return t.numerator, t.denominator
