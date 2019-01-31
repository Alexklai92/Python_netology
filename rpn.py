lst = input().split()

for i in lst:
	if len(lst) < 2:
		lst.pop(0)
		for j in i:
			lst.append(j)
				
if len(lst) > 3:
	raise SystemError('Много аргументов')
			

assert lst[0] == '+' or lst[0] == '-' or lst[0] == '*' or lst[0] == '/', f' Ваш оператор {lst[0]}'


try:
	if lst[0] == '+':
		rpn = int(lst[1]) + int(lst[2])
	elif lst[0] == '-':
		rpn = int(lst[1]) - int(lst[2])
	elif lst[0] == '*':
		rpn = int(lst[1]) * int(lst[2])
	elif lst[0] == '/':
		rpn = int(lst[1]) / int(lst[2])
	print(rpn)
	
except ZeroDivisionError:
	print('Деление на ноль')
	
except ValueError:
	print('Внимательней с типами данных')

