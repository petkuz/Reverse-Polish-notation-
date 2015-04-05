import operator as op
# functions


def replace(f, o):  # replace all operands in function by numbers and convert string to list
	delimmer = " "
	operandsArr = o.split(delimmer)
	l = ["^", "*", "/", "+", "-","(",")"]
	for i in range(0, len(f)):
		for h in operandsArr:
			h = h.split("=")
			f = f.replace(h[0], h[1])
	i = 0
	while(i < len(f)):
		for x in l:
			if(f[i] == x):
				f = f[:i] + "|" + f[i] + "|" + f[i+1:]
				if(i < (len(f)-3)):
					if(f[i+3] == "+" or f[i+3] == "-"):
						i += 2
				i += 2	
		i += 1
	f = f.replace("||", "|")
	f = f.split("|")
	while '' in f:
		f.remove('')
	return f


def priority(x):  # returns piority level of char
	d = {"(": 0, ")": 1, "+": 2, "-": 2, "*": 3, "/": 3, "^": 4}
	return d[x]


def last(stack):  # returns last element in stack
	return(stack[len(stack) - 1])


def is_number(s):  # check element is it integer
	try:
		int(s)
		return True
	except ValueError:
		return False


def getRPNfromExpr(expression):  # convert infix into postfix notation
	pString = []
	pStack = []
	for x in expression:
		if(is_number(x)):
			pString.append(x)
		else:
			if(pStack == [] or x == "("):
				pStack.append(x)
			elif(x == ")"):
				stop = True
				while(stop):
					poped = pStack.pop()
					if(poped == "("):
						stop = False
					else:
						pString.append(poped)
			else:
				for i in range(0, len(pStack)):
					if(priority(last(pStack)) >= priority(x)):
						pString.append(pStack.pop())
				pStack.append(x)
	for i in range(0, len(pStack)):
		pString.append(pStack.pop())
	return pString


def solveRPN(rpn):  # solve reverse polish notation
	result = []
	ops = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.truediv, "^": op.pow}
	for x in rpn:
		if(is_number(x)):
			result.append(int(x))
		else:
			b = result.pop()
			a = result.pop()
			result.append(ops[x](a, b))
	return result

# input data
formula = input("Enter formula: ")
operands = input("Enter operands: ")


# get and solve reverse polish notation
expression = replace(formula, operands)
print("Exp: " + "".join(expression))
pNotation = getRPNfromExpr(expression)
print("RPN: " + "".join(pNotation))
result = solveRPN(pNotation)
print("Solvation: " + str(result[0]))
