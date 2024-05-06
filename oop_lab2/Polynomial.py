"""The module is designed for work with polynomials.
"""
from RationalNumber import RationalNumber

class Polynomial:
    """Polynomial in one variable <x> with rational coefficients.

    Attributes:
        coef (dict): A dictionary, where every key-value pair represents a degree-coefficient pair,
                      thus a monomial coefficient*x^degree. Keys (degrees) are non-negative integers, 
                      values (coefficients) are objects of class <RationalNumber>.
        deg (int): A degree of a polynomial. In this class, a zero-polynomial's degree is equal to 0.
                      
    """

    def __init__(self, coefficients: str):
        """Initializes the instance based on string with coefficients,
        which are separated by comma and considered to have the appropriate 
        form (e.g. "m / n", minuses and spaces are allowed).
        """
        self.coef = {}
        coef = coefficients.split(",")[-1::-1]
        for i in range(len(coef)):
            coef[i] = RationalNumber.from_string(coef[i])
            self.coef[i] = coef[i]
        for number in coef[-1::-1]:
            if number.num == 0:
                coef.pop()
            else:
                value = len(coef) - 1
                break
        try:
            self.deg = value
        except UnboundLocalError:
            self.deg = 0

    
    def __repr__(self):
        """Makes an object to be represented in the standart basis 
        of the polynomial vector space.
        """
        string = ""
        for deg, coef in self.coef.items():
            string += f"({coef})*x^{deg} + "
        return string[:-2:]
    
    def __call__(self, x):
        """Makes an object a functor.

        Args:
            x: coordinate of a point in one-dimensional real vector space.
        
        Returns:
            res (RationalNumber): polynomial value at a point <x>.
        """
        res = RationalNumber._wrapper(0)
        x = RationalNumber._wrapper(x)
        for deg, coef in self.coef.items():
            res += coef * (x ** deg)
        return res
    
    def roots(self):
        """Finds the roots of a polynomial.

        Five cases are considered:  zero-polynomial;
                                    polynomial of 0-degree;
                                    polynomial of the first degree (linear);
                                    polynomial of the second degree (quadratic);
                                    polynomial of higher degrees.
        
        Returns:
            message (str): Case of zero-polynomial: displays that an object has infinetely many roots.
            message (str): Case of polynomial of 0-degree: displays that an objectf has no roots.
            value (RationalNumber): Case of the first-degree polynomial: the root.
            (x1, x2) (tuple): Case of the second-degree polynomial: the roots (probably, irrational).
            roots (list): Case of the higher-degree polynomial: rational roots (objects of class 
                            <RationalNumber>) if they exist; otherwise, an empty list.
        """
        if self.deg == 2:
            D = self.coef[1] ** 2 - 4 * self.coef[2] * self.coef[0]
            det = D.num / D.den
            x1 = (-self.coef[1].num/self.coef[1].den + det ** 0.5) / (2 * self.coef[2].num/self.coef[2].den)
            x2 = (-self.coef[1].num/self.coef[1].den - det ** 0.5) / (2 * self.coef[2].num/self.coef[2].den)
            return (x1, x2)
        elif self.deg == 1:
            return -self.coef[0] / self.coef[1]
        elif self.deg == 0 and self.coef[0] != 0:
            return 'Degree of the polynomial == 0, thus no roots.'
        elif self.deg == 0 and self.coef[0] == 0:
            return 'Any element from complex field is a root.'
        else:
            return self.roots_bruteforce()
    
    def coef_integers(self):
        """Checks if the coefficients of an <object> belong to class <int>.

        Returns:
            value (bool): True if all coefficients are integers, False otherwise.
        """
        value = True
        for deg, coef in self.coef.items():
            if coef.is_integer():
                pass
            else:
                value = False
                break
        return value
    
    def roots_bruteforce(self):
        """Finds rational roots of an object, using rational root theorem 
        and bruteforce method.

        Returns:
            roots (list): Rational roots of a polynomial, which are the objects
                          of class <RationalNumber>.
        """
        divisors_a0 = []          # a0 + a1*x + ... + an*x^n
        divisors_an = []
        roots = []
        if self.coef_integers():
            coef_0 = self.coef[0].num / self.coef[0].den
            for i in range(1, int((abs(coef_0))**0.5) + 1):
                if coef_0 % i == 0:
                    divisors_a0.append(i)
                    divisors_a0.append(-i)
            coef_n = self.coef[self.deg].num / self.coef[self.deg].den
            for i in range(1, int(abs(coef_n)**0.5) + 1):
                if coef_n % i == 0:
                    divisors_an.append(i)
            for p in divisors_a0:
                for q in divisors_an:
                    pot_root = RationalNumber(p, q)
                    if self(pot_root) == 0:
                        roots.append(pot_root)
        return roots
    
if __name__ == '__main__':
    
    with open("input2.txt") as f:
        polynomials_str = f.readlines()
    values = []
    roots = []
    for string in polynomials_str:
        p = Polynomial(string)
        values.append(p(1))
        roots_string = str(p.roots())
        roots.append(roots_string)

    with open("polynomials_values.txt", 'w') as f:
        for i in range(len(polynomials_str)):
            f.write(f'{Polynomial(polynomials_str[i])} := {values[i]}\n')
    
    with open("polynomials_roots.txt", 'w') as f:
        for i in range(len(polynomials_str)):
            f.write(f'{Polynomial(polynomials_str[i])} := {roots[i]}\n')