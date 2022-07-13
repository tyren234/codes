def stack_operations (text):
	numbers = []
	operators = []
	for character in text:
		if character in "+-*/":
			print ("operacja")
			operators.append(character)
		elif character.isdigit():
			print ("cyfra")
			numbers.append(int(character))
		elif character == ')':
			second = numbers.pop()
			first = numbers.pop()
			op = operators.pop()
			if op == '+':
				numbers.append(first + second)
			elif op == '-':
				numbers.append(first - second)
			elif op == '*':
				numbers.append(first * second)
			elif op == '/':
				numbers.append(first / second)
			else:
				print("Wrong operator. Returning -1.")
				return -1
		else:
			continue
	print ("numbers: ", numbers)

#stack_operations ("(2 + (5 - 3))")
#print("12345".isdigit())	
