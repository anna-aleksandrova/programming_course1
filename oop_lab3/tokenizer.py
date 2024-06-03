"""
Модуль призначено для розбиття виразу, що містить многочлен у формі
'a0 + a1 x + a2 x^2 + ... an x^n'
"""

# типи токенів
TOKEN_TYPE = (
    "variable",
    "constant",
    "operation",
    "left_paren",
    "right_paren",
    "other"
)

# словник фіксованих токенів, що складаються з одного символа
TOKEN_TYPES = {
    "+": "operation",
    "-": "operation",
    "*": "operation",
    "/": "operation",
    "^": "operation",
    "(": "left_paren",
    ")": "right_paren",
}


class Token:

    def __init__(self, type, value):
        assert type in TOKEN_TYPE, 'недопустимий тип токена'
        self.type = type
        self.value = value

    def __eq__(self, __value: object) -> bool:
        return self.type == __value.type and self.value == __value.value

    def __repr__(self):
        return f"Token(type='{self.type}', value='{self.value}')"


def get_tokens(string):
    """Функція за рядком повертає список токенів типу Token.

    :param string: рядок
    :return: список токенів
    """
    tokens = []
    while string:
        token, string = _get_next_token(string)
        if token:
            tokens.append(token)
    return tokens


def _get_next_token(string):
    """Функція повертає наступний токен та залишок рядка.

    :param string: рядок
    :return:
        next_token: наступний токен, якщо є, або None
        string: залишок рядка
    """
    for func in [
        _get_operator,
        _get_constant,
        _get_complex_rational_constant,
        _get_variable,
        _get_other
        ]:
            res = func(string)
            if res is not None:
                return res


def _get_operator(string):
    """Функція за рядком повертає оператор (якщо є) та залишок рядка.

    :param string: рядок
    :return:
        next_token: оператор типу Token('operation', ...)
        string: залишок рядка
    """
    if string[0] == '+':
        string = string[1:]
        return Token('operation', '+'), string
    elif string[0] == '-':
        string = string[1:]
        return Token('operation', '-'), string
    elif string[0] == '*':
        string = string[1:]
        return Token('operation', '*'), string
    elif string[0] == '/':
        string = string[1:]
        return Token('operation', '/'), string
    elif string[0] == '^':
        string = string[1:]
        return Token('operation', '^'), string
    else:
        pass


def _get_constant(string):
    """Функція за рядком повертає константу (якщо є) та залишок рядка.

    :param string: рядок
    :return:
        next_token: константа типу Token('constant', ...) або None
        string: залишок рядка
    """
    if string[0].isdigit():
        i = 0
        point_count = 0
        while i < len(string):
            if string[i].isdigit():
                i += 1
            elif string[i] == '.' and point_count < 1:
                point_count += 1
                i += 1
            else:
                break
        return Token('constant', string[0:i]), string[i:]
    else:
        pass

def _get_complex_rational_constant(string):
    """Функція за рядком повертає комплексну константу (якщо є) та залишок рядка.

    :param string: рядок
    :return:
        next_token: константа типу Token('constant', ...) або None
        string: залишок рядка
    """
    if string[0] == "(":
        i = 0
        while i < len(string):
            i += 1
            if string[i] == ")":
                break
        return Token('constant', string[1:i]), string[i+1:]

def _get_variable(string):
    """Функція за рядком повертає змінну (якщо є) та залишок рядка.

    :param string: рядок
    :return:
        next_token: змінна типу Token('constant', ...) або None
        string: залишок рядка
    """
    if string[0].isidentifier():
        i = 0
        while i < len(string):
            if string[i].isidentifier() or string[i].isdigit():
                i += 1
            else:
                break
        return Token('variable', string[0:i]), string[i:]
    else:
        pass

def _get_other(string):
    """Функція за рядком повертає об'єкт типу other (якщо є) та залишок рядка.

    :param string: рядок
    :return:
        next_token: константа типу Token('other', ...) або None
        string: залишок рядка
    """
    if string[0] == " ":
        string = string[1:]
        return None, string
    elif string[0] in "+-*/=()" or string[0].isdigit() or string[0].isidentifier():
        return None, string
    else:
        i = 0
        while i < len(string) and string[i] not in "+-*/=() " and not string[i].isdigit() and not string[i].isidentifier():
            i += 1
        else:
            return Token('other', string[0:i]), string[i:]


if __name__ == "__main__":

    needed = [
        Token(type='operation', value='-'),
        Token(type='constant', value='5'),

        Token(type='operation', value='+'),
        Token(type='constant', value='3'),
        Token(type='variable', value='x'),

        Token(type='operation', value='-'),
        Token(type='constant', value='3 / 4'),
        Token(type='variable', value='x'),
        Token(type='operation', value='^'),
        Token(type='constant', value='2')
    ]

    success = (x := get_tokens("-5 + 3x - (3 / 4)x^2")) == needed
    if not success:
        if len(x) != len(needed):
            print(f'wrong amount of tokens. Expected: {len(needed)}, got: {len(x)}')
        for exp, real in zip(needed, x):
            if exp != real:
                print(f'Expected: {exp}, got {real}')

    needed = [
        Token(type='operation', value ='-'),
        Token(type='constant', value='3 + 2j'),

        Token(type='operation', value='+'),
        Token(type='constant', value='- 2/ 3'),
        Token(type='variable', value='x'),

        Token(type='operation', value='+'),
        Token(type='constant', value='5'),
        Token(type='variable', value='x'),
        Token(type='operation', value='^'),
        Token(type='constant', value='2'),

        Token(type='operation', value='+'),
        Token(type='constant', value='5+6j'),
        Token(type='variable', value='x'),
        Token(type='operation', value='^'),
        Token(type='constant', value='4')
    ]

    success = success and (x := get_tokens("-(3 + 2j) +  (- 2/ 3)x + 5x^2 + (5+6j) x^ 4")) == needed
    if not success:
        if len(x) != len(needed):
            print(f'wrong amount of tokens. Expected: {len(needed)}, got: {len(x)}')
        for exp, real in zip(needed, x):
            if exp != real:
                print(f'Expected: {exp}, got {real}')

    print("Success =", success)
