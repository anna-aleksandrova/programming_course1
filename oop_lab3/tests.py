from rational import RationalNumber
from Polynomial import Polynomial, euclidean_algorithm

def test_appropriate_coeff_type():
    """Tests function (static method) appropriate_coeff_type()
          from class <Polynomial>.
    
    Raises:
        AssertionError: if a function does not work correctly.
    """
    assert Polynomial.appropriate_coeff_type(int)
    assert Polynomial.appropriate_coeff_type(RationalNumber)
    assert Polynomial.appropriate_coeff_type(float)
    assert Polynomial.appropriate_coeff_type(complex)
    assert not Polynomial.appropriate_coeff_type(str)
    assert not Polynomial.appropriate_coeff_type(list)

def test_appropriate_arg():
    """Tests function (static method) appropriate_arg()
          from class <Polynomial>.
    
    Raises:
        AssertionError: if a function does not work correctly.
    """
    assert Polynomial.appropriate_arg(5)
    assert Polynomial.appropriate_arg(RationalNumber(3, 4))
    assert Polynomial.appropriate_arg(3.14)
    assert Polynomial.appropriate_arg(1+1j)
    assert Polynomial.appropriate_arg("1+x")
    assert Polynomial.appropriate_arg([1, 2, 3])
    assert Polynomial.appropriate_arg({0: 1})
    assert not Polynomial.appropriate_arg((0, 1))
    assert not Polynomial.appropriate_arg({0, 1})

def test_from_string():
    """Tests function (static method) _from_string()
          from class <Polynomial>.
    
    Raises:
        AssertionError: if a function does not work correctly.
    """
    string = "1 + 2x + 3x^2"
    needed = {
        0: 1,
        1: 2,
        2: 3
    }
    res = Polynomial._from_string(string, int)
    assert res == needed

    string = "(1+1j) + 2x - (3+2j)x^3"
    needed = {
        0: (1+1j),
        1: (2+0j),
        3: (-3-2j)
    }
    res = Polynomial._from_string(string, complex)
    assert res == needed

    string = "(3/4) + (2/1)x - (3/2)x^3"
    needed = {
        0: RationalNumber(3,4),
        1: RationalNumber(2,1),
        3: RationalNumber(-3,2)
    }
    res = Polynomial._from_string(string, RationalNumber)
    assert res == needed

def test_from_dict():
    """Tests function (static method) _from_dict()
          from class <Polynomial>.
    """
    future_poly = {
        0: 3.4,
        2: 5.6,
        3: 4.98
    }
    needed = {
        0: 3.4,
        2: 5.6,
        3: 4.98
    }
    polynomial = Polynomial._from_dict(future_poly, float)
    assert polynomial == needed

    not_future_poly_1 = {
        "1": 3.4,
        2: 5.6,
        3: 4.98 
    }
    polynomial = Polynomial._from_dict(not_future_poly_1, float)
    assert isinstance(polynomial, ValueError)

    not_future_poly_2 = {
        1: RationalNumber._wrapper(3.4),
        2: 5.6,
        3: 4.98 
    }
    polynomial = Polynomial._from_dict(not_future_poly_2, float)
    assert isinstance(polynomial, TypeError)
    
def test_from_list():
    """Tests function (static method) _from_list()
          from class <Polynomial>.
    """
    future_poly = [1, 2, 3]
    polynomial = Polynomial._from_list(future_poly, int)
    needed = {
        0: 1,
        1: 2,
        2: 3
    }
    assert polynomial == needed
    polynomial = Polynomial._from_list(future_poly, complex)
    needed = {
        0: (1+0j),
        1: (2+0j),
        2: (3+0j)
    }
    assert polynomial == needed

    not_future_poly = [RationalNumber(3, 4), RationalNumber(1, -2)]
    polynomial = Polynomial._from_list(not_future_poly, float)
    assert isinstance(polynomial, TypeError)

def test_from_number():
    """Tests function (static method) _from_number()
          from class <Polynomial>.
    """
    future_poly = RationalNumber(3, 14)
    polynomial = Polynomial._from_number(future_poly, complex)
    needed = {
        0: complex(RationalNumber(3, 14))
    }
    assert polynomial == needed

    not_future_poly = 3.14
    polynomial = Polynomial._from_number(not_future_poly, int)
    assert isinstance(polynomial, TypeError)

def test_wrapper():
    """Tests function (static method) wrapper()
          from class <Polynomial>.
    """
    test = {
        0: 1+0j,
        2: 1+0j,
        4: 1+0j
    }
    needed = {
        0: 1+0j,
        1: 0j,
        2: 1+0j,
        3: 0j,
        4: 1+0j
    }
    res = Polynomial.wrapper(test)
    assert res == needed

def test_copy():
    """Tests function copy() from class <Polynomial>.
    """
    string = "1 + 2x - 3x^2"
    poly = Polynomial(string, float)
    test = poly._copy()
    assert test.coefficients == {
        0: 1.0,
        1: 2.0,
        2: -3.0
    } 
    assert isinstance(test, Polynomial)

def test_as_type():
    """Tests function as_type() from class <Polynomial>.
    """
    string = "1 + 2x - 3x^2"
    poly = Polynomial(string, float)
    assert poly.coefficients == {
        0: 1.0,
        1: 2.0,
        2: -3.0
    }

    test = poly.as_type(complex)
    assert test.coefficients == {
        0: (1+0j),
        1: (2+0j),
        2: (-3+0j)
    }
    assert isinstance(test, Polynomial)

    test = poly.as_type(int)
    assert isinstance(test, TypeError)

def test_to_degree():
    """Tests function to_degree() from class <Polynomial>.
    """
    string = "1 + 2x - 3x^2"
    poly = Polynomial(string, int)
    test = poly.to_degree(4)
    assert test.coefficients == {
        0: 1,
        1: 2,
        2: -3,
        3: 0,
        4: 0
    }
    assert isinstance(test, Polynomial)

def test_add():
    """Tests magic method __add__() from class <Polynomial>.
    """
    poly1 = Polynomial({0:1, 1:2, 2: -3}, int)
    poly2 = Polynomial({0:1.0, 1:2.0}, float)
    test_add = poly1 + poly2
    assert test_add.coefficients == {
        0: 2.0,
        1: 4.0, 
        2: -3.0
    }
    assert isinstance(test_add, Polynomial)

    poly1 = Polynomial({0:1, 1:2, 2: -3}, int)
    poly2 = 3.0
    test_add = poly2 + poly1
    assert test_add.coefficients == {
        0: 4.0,
        1: 2.0, 
        2: -3.0
    }
    assert isinstance(test_add, Polynomial)

def test_mul():
    """Tests magic method __mul__() from class <Polynomial>.
    """
    poly1 = Polynomial({0: 0, 1: 3}, int)
    poly2 = Polynomial({0: 1, 1: 0, 2: 1}, int)
    test_mul = poly1 * poly2
    assert test_mul.coefficients == {
        0: 0,
        1: 3,
        2: 0,
        3: 3
    }

    poly1 = Polynomial({0:1, 1:2, 2: -3}, int)
    poly2 = 1
    test_mul = poly1 * poly2
    assert test_mul.coefficients == {
        0: 1,
        1: 2, 
        2: -3
    }
    assert isinstance(test_mul, Polynomial)

    poly1 = Polynomial({0:1, 1:2, 2: -3}, int)
    poly2 = 1
    test_mul = poly2 * poly1
    assert test_mul.coefficients == {
        0: 1,
        1: 2, 
        2: -3
    }
    assert isinstance(test_mul, Polynomial)


def test_sub():
    """Tests magic method __sub__() from class <Polynomial>.
    """
    poly1 = Polynomial({0:1, 1:2, 2: 3}, int)
    poly2 = Polynomial({0:1.0, 1:2.0, 2: 3.0}, float)
    test_mul = poly1 - poly2
    assert test_mul.coefficients == {
        0: 0.0,
        1: 0.0, 
        2: 0.0
    }
    assert isinstance(test_mul, Polynomial)
    poly1 = Polynomial({0:1, 1:2, 2: 3}, int)
    poly2 = 1.0
    test_mul = poly2 - poly1
    assert test_mul.coefficients == {
        0: 0.0,
        1: -2.0, 
        2: -3.0
    }
    assert isinstance(test_mul, Polynomial)

def test_truediv():
    """Tests magic method __truediv__() from class <Polynomial>.
    """
    poly = Polynomial({0:2, 1:2, 2: 4}, int)
    value = 2
    test_truediv = poly / value
    assert test_truediv.coefficients == {
        0: 1.0,
        1: 1.0,
        2: 2.0
    }
    assert isinstance(test_truediv, Polynomial)

def test_call():
    """Tests magic method __call__() from class <Polynomial>.
    """
    poly = Polynomial({0:2, 1:2, 2: 4}, int)
    test = poly(2)
    assert test == 22

def test_derivative():
    """Tests function derivative() from class <Polynomial>.
    """
    poly = Polynomial({0:2, 1:2, 2: 4}, int)
    test_derivative = poly.derivative()
    assert test_derivative.coefficients == {
        0: 2,
        1: 8
    }
    assert isinstance(test_derivative, Polynomial)

def test_primitive():
    """Tests function primitive() from class <Polynomial>.
    """
    poly = Polynomial({0:2, 1:2, 2: 3}, int)
    test_primitive = poly.primitive()

    assert test_primitive.coefficients == {
        0: 0.0,
        1: 2.0,
        2: 1.0,
        3: 1.0
    }
    assert isinstance(test_primitive, Polynomial)

def test_div():
    """Tests function div() from class <Polynomial>.
    """
    poly1 = Polynomial({
        0: 4,
        1: 3,
        2: 4,
        3: 3
    }, int)
    poly2 = Polynomial({
        0: 1,
        2: 1
    }, int)
    test = poly1.div(poly2)
    assert test[0].coefficients == {
        0: 4.0,
        1: 3.0,
    }
    assert test[1] == 0

def test_euclidean_algorithm():
    """Tests function euclidean_algorithm() from class <Polynomial>.
    """
    poly1 = Polynomial({
        0: 1,
        1: 1,
        2: 1,
    }, int)
    test = euclidean_algorithm(poly1, poly1)
    assert test.coefficients == {
        0: 1,
        1: 1,
        2: 1
    }


if __name__ == "__main__":

    test_appropriate_coeff_type()  
    test_appropriate_arg() 
    test_from_dict()
    test_from_list()
    test_from_number()
    test_from_string()
    test_wrapper()
    test_copy()
    test_as_type()
    test_to_degree()
    test_add()
    test_mul()
    test_sub()
    test_truediv()
    test_call()
    test_derivative()
    test_primitive()
    test_div()
    test_euclidean_algorithm()