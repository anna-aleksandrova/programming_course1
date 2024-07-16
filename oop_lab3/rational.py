"""The module is designed for work with rational numbers.

Class RationalNumber is exported. Class methods _wrapper()
and from_string() are the most used.

Typical usage example:

    number = RationalNumber(5, 2)
    x = RationalNumber._wrapper(5)
    y = RationalNumber.from_string('7/2')

"""
from functools import total_ordering

@total_ordering
class RationalNumber:
    """Rational number, whose numerator is an integer and 
    denominator is a positive integer.

    Attributes:
        _num: The numerator.
        _den: The denominator.
    """
    
    @staticmethod
    def gcd(p, q):
        """Calculates the greatest common divisor of two given integers.

        Args:
            p (int): The first number.
            q (int): The second number.

        Returns:
            res (int): The greatest common divisor.
        """
        a = max(abs(p), abs(q))
        b = min(abs(p), abs(q))
        if b == 0:
            res = a
        else:
            res = 0
            while True:
                r = a % b
                if r == 0:
                    res = b
                    break
                else:
                    a = b
                    b = r
        return res
    
    @staticmethod
    def lcm(p, q):
        """Calculates the least common multiple of two given integers.

        Args:
            p (int): The first number.
            q (int): The second number.

        Returns:
            res (int): The least common multiple.
        """
        return (p * q) / RationalNumber.gcd(p, q)
            

    def __init__(self, m, n):
        """Initializes the instance, which is an irreducible fraction, 
        based on two numbers.

        Args:
            m (int): The numerator.
            n (int): The denominator.
        
        Raises:
            AssertionError: If n == 0 (unable to divide by zero).
        """

        assert n != 0

        if m * n < 0:
            self._num =  int(- abs(m) / RationalNumber.gcd(m, n))
            self._den = int(abs(n) / RationalNumber.gcd(m, n))
        else:
            self._num =  int(abs(m) / RationalNumber.gcd(m, n))
            self._den = int(abs(n) / RationalNumber.gcd(m, n))

    @property
    def num(self):
        return self._num

    @property
    def den(self):
        return self._den
    
    def __repr__(self):
        """Defines the form in which the object <self> will be represented 
        when it's located in another structure (e.g. list or tuple).
        """
        return f'RationalNumber({self.num}, {self.den})'

    def __str__(self):
        """Defines the form in which the object <self> will be
        represented when print() is called.
        """
        return f'{self.num} / {self.den}'

    @classmethod
    def from_string(cls, string):
        """Converts a string into an object of a class <cls>.
        Considers a string to have an appropriate form (e.g.
        "m / n", minuses and spaces are allowed).

        Args:
            string (str): A string.

        Returns:
            cls(m, n): An object of class <cls>.
        """
        if isinstance(string, RationalNumber):
            return string
        string = string.replace(" ", "")
        if "/" not in string:
            m = int(string)
            n = 1
        else:
            aux = string.find("/")
            m = int(string[0:aux])
            n = int(string[aux + 1:]) 
        return cls(m, n)  

    @classmethod
    def _wrapper(cls, other):
        """Makes <other> an object of class <cls> if it's 
        an object of class <int> or <float>. Doesn't change
        <other> if it's an object of class <cls>.

        Args:
            other: An object of some class.

        Returns:
            other (cls): An object of class <cls>.

        Raises:
            TypeError: If 'other' is not an object of class
                          <int>, or <float>, or <cls>. 
        """

        if isinstance(other, int):
            other = cls(other, 1)
        elif isinstance(other, float):
            aux_str = str(other)
            dot_place = aux_str.find(".")
            power_10 = len(aux_str[dot_place + 1:])
            m = int(aux_str.replace(".", ""))
            n = 10 ** power_10
            other = cls(m, n)
        elif isinstance(other, cls):
            return cls(other.num, other.den)
        elif not (isinstance(other, int) or isinstance(other, float) or isinstance(other, cls)):
            raise TypeError(f"Unsupported operation for {cls} and {type(other)}.")
        else:
            pass
        return other
    
    def __add__(self, other):
        other = RationalNumber._wrapper(other)
        lcm = RationalNumber.lcm(self.den, other.den)
        num = int((self.num / self.den + other.num / other.den) * lcm)
        den = int(lcm)
        return type(self)(num, den)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        other = RationalNumber._wrapper(other)
        return type(self)(self.num * other.num, self.den * other.den)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        neg_other = (-1) * other
        return self + neg_other

    def __rsub__(self, other):
        return (-1)*(self - other)
    
    def __neg__(self):
        return (-1)*self

    def inverse(self):
        if self.num == 0:
            raise ValueError(f'{self} has no inverse in rational field.')
        else:
            return type(self)(self.den, self.num)

    def __truediv__(self, other):
        other = RationalNumber._wrapper(other)
        return self * other.inverse()

    def __rtruediv__(self, other):
        return other * self.inverse()

    def __abs__(self):
        return type(self)(abs(self.num), self.den)

    def sign(self):
        if self.num > 0:
            return 1
        elif self.num == 0:
            return 0
        else:
            return -1

    def __eq__(self, other):
        other = self._wrapper(other)
        return self.num == other.num and self.den == other.den

    def is_integer(self):
        if self.den == 1:
            return True
        else:
            return False
        
    def __gt__(self, other):
        other = RationalNumber._wrapper(other)
        if self.den == other.den:
            if self.num > other.num:
                return True
            else:
                return False
        else:
            lcm = RationalNumber.lcm(self.den, other.den)
            if self.num * lcm / self.den > other.num * lcm / other.den:
                return True
            else:
                return False
            
    def __pow__(self, other):
        """Raises an object to the power of <other> value,
        if <other> is an object of class <int> or <float> .

        Args:
            other: An object of some class.

        Returns:
            obj (RationalNumber): <self> raised to the power of <other>.
        
        Raises:
            TypeError: If other is not of type <int>, or <float>,
                          or <RationalNumber>.
        """
        if isinstance(other, int) or isinstance(other, float):
            return type(self)(self.num ** other, self.den ** other)
        elif isinstance(other, type(self)):
            NotImplementedError()
        else:
            raise TypeError(f"Unsupported operation for {type(self)} and {type(other)}.")
        
    def __complex__(self):
        return self.num/self.den + 0j
    
