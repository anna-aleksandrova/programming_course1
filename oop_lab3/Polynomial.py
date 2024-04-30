from rational import RationalNumber 
from tokenizer import get_tokens, Token
from copy import deepcopy

class Polynomial(dict):

    @staticmethod
    def appropriate_coeff_type(coeff_type):
        """Checks if <+>, <*> and </> are defined on the set (class) <coeff_type>.

        Args:
            coeff_type: Any class.

        Returns:
            (bool): True if <+>, <*>, </> are defined, False otherwise. 
        """
        if hasattr(coeff_type, "__add__") and hasattr(coeff_type, "__mul__") and hasattr(coeff_type, "__truediv__"):
            Polynomial.POL_CREATE_FROM.add(coeff_type)
            return True
        else:
            return False
    
    POL_CREATE_FROM = {str, dict, list, int, RationalNumber, complex}
    NUM_PRIORITY = {
        int: 1,
        float: 2,
        RationalNumber: 3,
        complex: 4
    }

    @staticmethod
    def appropriate_arg(arg):
        """Checks if it's possible to create a polynomial from object <arg>.

        Args:
            arg: An object.

        Returns:
            (bool): True if possible to create a polynomial from object <arg>, False otherwise. 
        """
        if type(arg) in Polynomial.POL_CREATE_FROM:
            return True
        else:
            return False

    @staticmethod
    def _from_string(string, coeff_type):
        """Returns a dictionary, where <key, pair> = <degree, coefficient>.

        Args:
            string (str): A string which contains a polynomial in form "a0 + a1 x +
                            a2 x^2 + ... an x^n".
            coeff_type: Coefficients of a polynomial must belong to this class.

        Returns:
            polynomial (dict): A dictionary, where <key, pair> = <degree, coefficient>, 
                                  and type(coefficient) is coeff_type.
        """
        tokens = get_tokens(string)
        sign = {
            '+': 1,
            '-': -1
        }
        if coeff_type == RationalNumber:
            coeff_type = RationalNumber.from_string
        polynomial = {}
        while tokens:
            i = 0
            if tokens[i].type == 'constant':
                if tokens[i+1].type == 'variable':
                    if tokens[i+2].value == '^':
                        polynomial[int(tokens[i+3].value)] = coeff_type(tokens[i].value)
                        tokens = tokens[i+4:]
                    else:
                        polynomial[1] = coeff_type(tokens[i].value)
                        tokens = tokens[i+2:]
                else:
                    polynomial[0] = coeff_type(tokens[i].value)
                    tokens = tokens[i+1:]
            elif tokens[i].type == 'operation':
                if tokens[i+1].type == 'constant':
                    tokens[i+1].value = coeff_type(tokens[i+1].value) * sign[tokens[i].value]
                    tokens = tokens[i+1:]
                else:
                    tokens[i] = Token("constant", value = sign[tokens[i].value])
            else:
                NotImplementedError()
        return polynomial

    
    @staticmethod
    def _from_dict(dictionary, coeff_type):
        """Returns a dictionary, where <key, pair> = <degree, coefficient>.

        Args:
            dictionary (dict): A dictionary, which potentially contains degrees and
                                  coefficients of a polynomial as in pairs <key, value>.
            coeff_type: Coefficients of a polynomial must belong to this class.

        Returns:
            polynomial (dict): A dictionary, where <key, pair> = <degree, coefficient>, 
                                  and type(coefficient) is coeff_type.

        Raises:      
            ValueError: If dictionary contains non-integer or negative keys 
                         (a polynomial doesn't have such degrees)..
            TypeError: If a dictionary has values which can't be transformed into
                          objects of class <type_coeff>. 
        """
        polynomial = {}
        for deg, coeff in dictionary.items():
            if not (isinstance(deg, int) and deg >= 0):
                return ValueError(f"{deg} can't be a degree of a polynomial.")
            elif Polynomial.NUM_PRIORITY[type(coeff)] > Polynomial.NUM_PRIORITY[coeff_type]:
                return TypeError(f"Wrong coefficient type. {coeff} is not of {coeff_type} type and can't be transformed into it.")
            else:
                polynomial[deg] = coeff_type(coeff)
        return polynomial

    @staticmethod
    def _from_list(lst, coeff_type):
        """Returns a dictionary, where <key, pair> = <degree, coefficient>.

        Args:
            lst (list): A list, which potentially coefficients of a polynomial.
            coeff_type: Coefficients of a polynomial must belong to this class.

        Returns:
            polynomial (dict): A dictionary, where <key, pair> = <degree, coefficient>, 
                                  and type(coefficient) is coeff_type.

        Raises:      
            TypeError: If a list has values which can't be transformed into
                          objects of class <type_coeff>. 

        """
        polynomial = {}
        for i in range(len(lst)):
            if Polynomial.NUM_PRIORITY[type(lst[i])] > Polynomial.NUM_PRIORITY[coeff_type]:
                return TypeError(f"Wrong coefficient type. {lst[i]} is not of {coeff_type} type and can't be transformed into it.")
            else:
                polynomial[i] = coeff_type(lst[i])
        return polynomial
    
    def _from_number(number, coeff_type):
        """Returns a dictionary, where <key, pair> = <degree, coefficient>.

        Args:
            number (coeff_type): An object of class <coeff_type>.
            coeff_type: Coefficients of a polynomial must belong to this class.

        Returns:
            polynomial (dict): A dictionary, where <key, pair> = <degree, coefficient>, 
                                  and type(coefficient) is coeff_type.
        """
        if Polynomial.NUM_PRIORITY[type(number)] > Polynomial.NUM_PRIORITY[coeff_type]:
            return TypeError(f"Wrong coefficient type. {number} is not of {coeff_type} type and can't be transformed into it.")
        polynomial = {0: coeff_type(number)}
        return polynomial

    @staticmethod
    def wrapper(dictionary):
        """Adds missing keys (degrees). Their value = coeff_type(0), where <coeff_type> is
        a class where dictionery.values() belong.

        Args:
            dictionary (dict): A dictionary, where <key, value> = <degree, coefficient>.

        Returns:
            dictionary (dict): A dictionary without missing keys.
        """
        pol_degree = max(dictionary.keys())
        coeff_type = type(dictionary[pol_degree])
        for i in range(pol_degree + 1):
            if i not in dictionary.keys():
                dictionary[i] = coeff_type(0)
        return dict(sorted(dictionary.items()))

    FROM = {
        str: _from_string,
        dict: _from_dict,
        list: _from_list,    
    }

    def __init__(self, arg, coeff_type):
        """Creates a polynomial: an object of type <dict>, where pair <key, item> =
        <degree, coefficient>. Coefficient can belong to any set (be of any type) where 
        operations <+>, <*>, </> are defined.

        Args:
            arg (string/dict/list/coeff_type): A structure which contains a polynomial.
            coeff_type: Type(class) of coefficients where <+>, <*> are defined.
        
        Raises:
            TypeError: 1. If <arg> is not of type <string>, <dict>, <list>, or any type where <+>, <*>
                        are defined.  
                        2. If at least one coefficient in object <arg> can't be converted to <coeff_type>.
                        3. If <+>, <*>, </> are not defined in class <coeff_type>.          
            ValueError: If there is an attempt to create a polynomial from a dictionary with non-integer
                          or negative keys.
        """
        if not Polynomial.appropriate_coeff_type(coeff_type):
            raise TypeError(f"Objects of class {coeff_type} can't be coefficients of a polynomial.")
        if not Polynomial.appropriate_arg(arg):
            raise TypeError(f"Impossible to create a polynomial from {arg}")
        if type(arg) in Polynomial.FROM:
            function = Polynomial.FROM[type(arg)]
        else:
            function = Polynomial._from_number
        self.coefficients = Polynomial.wrapper(function(arg, coeff_type))
        self.deg = max(self.coefficients.keys())
        self.coeff_type = coeff_type
    
    def _copy(self):
        """Returns a copy of object <self>.
        """
        return deepcopy(self)
    
    def as_type(self, coeff_type):
        """Returns a copy of object <self>.

        Args:
            coeff_type: A class where coefficients of copy must belong.

        Returns:
            res (dict): A copy of <self>.
        
        Raises:
            TypeError: If self.coefficients can't be made objects of class <coeff_type>
        """

        if Polynomial.NUM_PRIORITY[self.coeff_type] > Polynomial.NUM_PRIORITY[coeff_type]:
            return TypeError(f"Objects of class <{self.coeff_type}> can't be transformed into objects of class <{coeff_type}>.")
        else:
            return Polynomial(self.coefficients, coeff_type)
    
    def __str__(self):
        res = ""
        for deg, coeff in self.coefficients.items():
            res += f"({coeff})*x^{deg} + "
        return res[:len(res)-2]
    
    def __repr__(self):
        res = ""
        for deg, coeff in self.coefficients.items():
            if type(coeff) == complex:
                operator = "+"
            elif type(coeff) == RationalNumber:
                if coeff.sign() == "1" or coeff.sign() == "0":
                    operator = "+"
                else:
                    operator = "-"
                    coeff = coeff * (-1)
            else:
                if coeff >= 0:
                    operator = "+"
                else:
                    operator = "-"
                    coeff = (-1)*coeff
            res += f"{operator} {coeff} x^{deg} "
        return res
    
    def __iter__(self):
        self.deg = 0
        self.coeff = self.coefficients[self.deg]
        return self
    
    def __next__(self):
        if self.deg <= self.maxdeg:
            res_deg = self.deg
            res_coeff = self.coefficients[self.deg]
            self.deg += 1
            return res_deg, res_coeff
        else:
            raise StopIteration
        
    def to_degree(polynomial, degree):
        """Returns an object of class <Polynomial> which has a degree <degree>.

        Args:
            degree (int): A value of degree of <res>.

        Returns:
            res (Polynomial): An object of class <Polynomial> which has a degree <degree>.
        """
        if degree < polynomial.deg:
            raise NotImplementedError()
        elif degree == polynomial.deg:
            return polynomial
        else:
            res = polynomial._copy()
            for i in range(polynomial.deg + 1, degree + 1):
                res.coefficients[i] = res.coeff_type(0)
        return res

        
    def __add__(self, other):
        """Adds two polynomials.

        Args:
            other: A polynomial or an object of numeric type.
        
        Returns:
            res (Polynomial): The result of addition of <self> and <other>.
        """
        if not isinstance(other, Polynomial) and Polynomial.appropriate_coeff_type(type(other)) and Polynomial.appropriate_arg(other):
            other = Polynomial(other, type(other))
        elif isinstance(other, Polynomial):
            pass
        else:
            raise NotImplementedError()
        if self.coeff_type != other.coeff_type:
            if Polynomial.NUM_PRIORITY[self.coeff_type] < Polynomial.NUM_PRIORITY[other.coeff_type]:
                self = self.as_type(other.coeff_type)
            else:
                other = other.as_type(self.coeff_type)
        if self.deg != other.deg:
            if self.deg > other.deg:
                other = other.to_degree(self.deg)
            else:
                self = self.to_degree(other.deg)
        res_dict = {}
        for i in range(len(self.coefficients)):
            res_dict[i] = self.coefficients[i] + other.coefficients[i]
        return Polynomial(res_dict, self.coeff_type)
    
    def __radd__(self, other):
        if isinstance(other, Polynomial):
            return other + self
        else:
            if not isinstance(other, Polynomial) and Polynomial.appropriate_coeff_type(type(other)) and Polynomial.appropriate_arg(other):
                other = Polynomial(other, type(other))
                return other + self
            else:
                raise NotImplementedError()
    
    def __mul__(self, other):
        """Multiplies two polynomials.

        Args:
            other: A polynomial or an object of numeric type.
        
        Returns:
            res (Polynomial): The result of multiplication of <self> and <other>.
        """
        if not isinstance(other, Polynomial) and Polynomial.appropriate_coeff_type(type(other)) and Polynomial.appropriate_arg(other):
            other = Polynomial(other, type(other))
        if self.coeff_type != other.coeff_type:
            if Polynomial.NUM_PRIORITY[self.coeff_type] < Polynomial.NUM_PRIORITY[other.coeff_type]:
                self = self.as_type(other.coeff_type)
            else:
                other = other.as_type(self.coeff_type)
        aux = self.deg + other.deg
        other = other.to_degree(aux)
        self = self.to_degree(aux)
        res = {}
        for k in range(aux+1):
            coeff_k = 0
            for i in range(k+1):
                coeff_k += self.coefficients[i]*other.coefficients[k-i]
            res[k] = coeff_k
        return Polynomial(res, self.coeff_type)
    
    def __rmul__(self, other):
        if isinstance(other, Polynomial):
            return other * self
        else:
            if not isinstance(other, Polynomial) and Polynomial.appropriate_coeff_type(type(other)) and Polynomial.appropriate_arg(other):
                other = Polynomial(other, type(other))
                return other * self
            else:
                NotImplementedError() 

    def __sub__(self, other):
        """Subtracts one polynomial from another.

        Args:
            other (Polynomial or numeric type): The second one.
        
        Returns:
            res (Polynomial): The result of subtraction of <self> and <other>.
        """
        return self + (-1) * other
    
    def __rsub__(self, other):
        return other + (-1)*self
    
    def __truediv__(self, value):
        """Divides a polynomial by value.

        Args:
            value (numeric type): A divisor.
        
        Returns:
            res (Polynomial): The result of division <self> by <value>.

        Raises (returns):
            ValueError: If value == 0.
        """
        if value == 0:
            return ValueError("Can't divide by 0.")
        res = {}
        for deg, coeff in self.coefficients.items():
            res[deg] = coeff / value
        return Polynomial(res, type(res[0]))
    
    def __call__(self, value):
        """Returns a value of polynomial <self> at point <value>.

        Args:
            value (numeric type): A point. 
        """
        res = 0
        for deg, coeff in self.coefficients.items():
            res += coeff * (value ** deg)
        return  res

    
    def derivative(self):
        """
        Returns:
            res (Polynomial): A derivative of <self>.
        """
        res = {}
        for i in range(len(self.coefficients)-1):
            res[i] = (i+1) * self.coefficients[i+1]
        return Polynomial(res, type(res[0]))
    
    def primitive(self):
        """Returns a primitive of object of class <Polynomial>.

        Args:
            self (Polynomial): A polynomial.
        
        Returns:
            res (Polynomial): A primitive of <self>.
        """
        res = {}
        for i in range(1, len(self.coefficients) + 1):
            res[i] = self.coefficients[i-1] / i
        res[0] = 0
        return Polynomial(res, type(res[1]))

    def _reduce(self):
        """Returns a polynomial without zero coefficients.
        """
        to_delete = []
        for deg, coeff in self.coefficients.items():
            if coeff == 0:
                to_delete.append(deg)
        for deg in to_delete:
            del self.coefficients[deg]
        if self.coefficients:
            return Polynomial(self.coefficients, type(self.coefficients[0]))
        else:
            return 0
    def div(self, other):
        """Divides one polynomial by another.

        Args:
            other(Polynomial) : An object of class <Polynomial>.

        Returns:
            res (Polynomial) : A quotient of division.
            remainder (Polynomial) : A remainder of division.
        """
        if self.deg >= other.deg:
            pass
        else:
            self, other = other, self
        res = Polynomial({0:0}, int)
        while self != 0 and self.deg >= other.deg:
            res.coefficients[self.deg - other.deg] = self.coefficients[self.deg] / other.coefficients[other.deg]
            aux = Polynomial({self.deg-other.deg : self.coefficients[self.deg] / other.coefficients[other.deg]}, type(self.coefficients[self.deg] / other.coefficients[other.deg]))
            self = (self - aux * other)._reduce()
        remainder = self
        return res, remainder


def euclidean_algorithm(poly1, poly2):
    if poly1.deg >= poly2.deg:
        pass
    else:
        poly1, poly2 = poly2, poly1
    while True:
        if poly2 == 0:
            break
        poly1, poly2 = poly2, poly1.div(poly2)[1]
    return poly1

    
    

    
        

