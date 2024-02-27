class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def check_simplicity(self):
        return self.numerator < self.denominator

fraction = Fraction(3, 5)
if fraction.check_simplicity():
    print("Дріб правильний.")
else:
    print("Дріб не правильний.")
