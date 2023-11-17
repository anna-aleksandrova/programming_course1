# Без перевірки, чи правильно введено вираз

def value(expression):

	operators = {"+": lambda x, y: x + y,
				 "-": lambda x, y: x - y,
				 "*": lambda x, y: x * y,
				 "/": lambda x, y: x / y}

	if type(expression) == float:
		return float(expression)

	elif len(expression.split()) == 3:
		expression = expression.replace("(", "")
		expression = expression.replace(")", "")
		if expression.split()[0].isdigit() and expression.split()[2].isdigit():
			x = int(expression.split()[0])
			y = int(expression.split()[2])
			operator = expression.split()[1]
			result = operators[operator](x, y)
			return result
		else:
			x = float(expression.split()[0])
			y = float(expression.split()[2])
			operator = expression.split()[1]
			result = operators[operator](x, y)
			return result

	else:
		opening_par = 0
		closing_par = 0

		index_symb = -1                       # first expression
		for symb in expression:
			index_symb += 1
			if symb == "(":
				opening_par += 1
			elif symb == ")":
				closing_par += 1
			if opening_par == closing_par and index_symb != len(expression) - 1:
				x = expression[0:index_symb]
				expression = expression[index_symb + 1:len(expression)]
				break
			elif opening_par == closing_par and index_symb == len(expression) - 1:
				min_index = len(expression)
				for operator in operators:
					if operator in expression:
						m = expression.index(operator)
						if m < min_index:
							min_index = m
				x = float((expression[0:min_index].replace("(", "")).replace(" ", ""))
				expression = expression[min_index:len(expression) - 1]


		index_symb = -1                       # operator
		for symb in expression:
			index_symb += 1
			if symb in operators:
				operator = expression[index_symb]
				break

		if expression[index_symb + 1] == " ":               # second expression
			y = expression[index_symb + 2:len(expression)]
		else:
			y = expression[index_symb + 1:len(expression)]

		result = operators[operator](value(x), value(y))
		return result


expression = "(" + input() + ")"
print(value(expression))