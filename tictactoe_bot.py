import random
name = input("Введіть Ваше ім'я: ")


bot_goes = "\nХід бота:\n"
person_goes = "\nВаш хід:\n"

note_1 = """
Щоб зробити хід, Вам треба ввести число від 1 до 9. Кожне з них 
визначає певне місце на полі гри (поле - матриця 3х3).
"""

note_2 ="""
Число 1 - елемент a_11.
Число 2 - елемент a_12.
Число 3 - елемент a_13.
Число 4 - елемент a_21.
Число 5 - елемент a_22.
Число 6 - елемент a_23.
Число 7 - елемент a_31.
Число 8 - елемент a_32.
Число 9 - елемент a_33.
"""

print(note_1)
print("Модель поля:")
for i in range(1, 4):	
	print(f"a_{i}{1} a_{i}{2} a_{i}{3}")
	i += 1

print(note_2)


#бот_1
a = ['-', '-', '-'] 
b = ['-', '-', '-'] 
c = ['-', '-', '-']
a[0] = "x"

def matrix_output_bot(a, b, c):
	print(bot_goes)
	print(*a)
	print(*b)
	print(*c, end="\n")
matrix_output_bot(a, b, c)


#person_1
print("""
Оберіть, куди поставити нулик.""")
place = int(input())
while True:
	if 2 <= place <= 9:
		break
	else:
		print("Такого елемента не існує. Виберіть інший елемент.")
if place == 2:
	a[1] = "o"
elif place == 3:
	a[2] = "o"
elif place == 4:
	b[0] = "o"
elif place == 5:
	b[1] = "o"
elif place == 6:
	b[2] = "o"
elif place == 7:
	c[0] = "o"
elif place == 8:
	c[1] = "o"
elif place == 9:
	c[2] = "o"
print(person_goes)
print(*a)
print(*b)
print(*c, end = "\n")




#bot_2
if a[1] == "o" or a[2] == "o" or b[2] == "o":
	c[0] = "x"
	glob = 1
elif b[0] == "o" or c[0] == "o" or c[1] == "o":
	a[2] = "x"
	glob = 2
elif c[2] == "o":
	temp = random.randint(0, 1)
	if temp == 0:
		a[2] = "x"
		glob = 3
	elif temp == 1:
		c[0] = "x"
		glob = 4
elif b[1] == "o":
	temp = random.randint(0, 1)                          
	if temp == 0:
		a[2] = "x"
		glob = 5
	elif temp == 1:
		c[0] = "x"
		glob = 6

matrix_output_bot(a, b, c)



#person_2
def matrix_output_person(a, b, c):
	while True:
		print("""
Оберіть, куди поставити нулик""")
		place = int(input())
		if 1 <= place <= 9:
			if place == 2 and a[1] != "-" or place == 3 and a[2] != "-" or place == 4 and b[0] != "-"\
			or place == 5 and b[1] != "-" or place == 6 and b[2] != "-" or place == 7 and c[0] != "-"\
			or place == 8 and c[1] != "-" or place == 9 and c[2] != "-":
				print("Це місце вже зайнято. Виберіть інший елемент.")
			else:
				break
		else:
			print("Такого елемента не існує. Виберіть інший елемент.")
		
	if place == 2:
		a[1] = "o"
	elif place == 3:
		a[2] = "o"
	elif place == 4:
		b[0] = "o"
	elif place == 5:
		b[1] = "o"
	elif place == 6:
		b[2] = "o"
	elif place == 7:
		c[0] = "o"
	elif place == 8:
		c[1] = "o"
	elif place == 9:
		c[2] = "o"
	print(person_goes)
	print(*a)
	print(*b)
	print(*c, end = "\n")

matrix_output_person(a, b, c)



def win():
	matrix_output_bot(a, b, c)
	print("Бот виграв!")
	exit()



#bot_3
if glob == 1:
	if b[0] != "o":
		b[0] = "x"
		win()
	elif b[0] == "o":
		c[2] = "x"
		matrix_output_bot(a, b, c)
elif glob == 2:
	if a[1] != "o":
		a[1] = "x"
		win()
	elif a[1] == "o":
		c[2] = "x"
		matrix_output_bot(a, b, c)
elif glob == 3:
	if a[1] != "o":
		a[1] = "x"
		win()
	elif a[1] == "o":
		c[0] = "x"
		matrix_output_bot(a, b, c)
elif glob == 4:
	if b[0] != "o":
		b[0] = "x"
		win()
	elif b[0] == "o":
		a[2] = "x"
		matrix_output_bot(a, b, c)
elif glob == 5:
	if a[1] != "o":
		a[1] = "x"
		win()
	elif a[1] == "o":
		c[1] = "x"
		matrix_output_bot(a, b, c)
elif glob == 6:
	if b[0] != "o":
		b[0] = "x"
		win()
	elif b[0] == "o":
		b[2] = "x"
		matrix_output_bot(a, b, c)



#person_3
matrix_output_person(a, b, c)



#bot_4
if glob == 1:
	if b[1] != "o" and c[1] != "o":
		temp = random.randint(0, 1)
		if temp == 0:
			b[1] = "x"
			win()
		elif temp == 1:
			c[1] = "x"
			win()
	elif b[1] == "o":
		c[1] = "x"
		win()
	elif c[1] == "o":
		b[1] = "x"
		win()

if glob == 2:
	if b[1] != "o" and b[2] != "o":
		temp = random.randint(0, 1)
		if temp == 0:
			b[1] = "x"
			win()
		elif temp == 1:
			b[2] = "x"
			win()
	elif b[1] == "o":
		b[2] = "x"
		win()
	elif b[2] == "o":
		b[1] = "x"
		win()

if glob == 3:
	if b[0] != "o" and b[1] != "o":
		temp = random.randint(0, 1)
		if temp == 0:
			b[0] = "x"
			win()
		elif temp == 1:
			b[1] = "x"
			win()
	elif b[0] == "o":
		b[1] = "x"
		win()
	elif b[1] == "o":
		b[0] = "x"
		win()

if glob == 4:
	if a[1] != "o" and b[1] != "o":
		temp = random.randint(0, 1)
		if temp == 0:
			a[1] = "x"
			win()
		elif temp == 1:
			b[1] = "x"
			win()
	elif a[1] == "o":
		b[1] = "x"
		win()
	elif b[1] == "o":
		a[1] = "x"
		win()

if glob == 5:
	if b[0] == "o":
		b[2] = "x"
		glob = 5.1
	elif b[2] == "o":
		b[0] = "x"
		glob = 5.2
	elif c[0] == "o":
		temp = random.randint(0, 1)
		if temp == 0:
			b[2] = "x"
			glob = 5.31
		elif temp == 1:
			c[2] = "x"
			glob = 5.32
	elif c[2] == "o":
		temp = random.randint(0, 1)
		if temp == 0:
			b[0] = "x"
			glob = 5.41
		elif temp == 1:
			c[2] = "x"
			glob = 5.42
matrix_output_bot(a, b, c)		

if glob == 6:
	if c[1] == "o":            
		a[1] = "x"
		glob = 6.1
	elif a[1] == "o":
		c[1] = "x"
		glob = 6.2
	elif c[2] == "o":
		temp = random.randint(0, 1)
		if temp == 0:
			a[1] = "x"
			glob = 6.31
		elif temp == 1:
			a[2] = "x"
			glob = 6.32
	elif a[2] == "o":
		temp = random.randint(0, 1)
		if temp == 0:
			c[1] = "x"
			glob = 6.41
		elif temp == 1:
			a[2] = "x"
			glob = 6.42

	matrix_output_bot(a, b, c)



#person_4
matrix_output_person(a, b, c)


def tie_after_bot():
	matrix_output_bot(a, b, c)
	print("Зіграно внічию.")
	exit()


#bot_5

#case_5_1
if glob == 5.1:
	if c[2] != "o":
		c[2] = "x"
		win()
	elif c[2] == "o":
		c[0] = "x"
		tie_after_bot()

#case_5_2:
if glob == 5.2:
	if c[0] != "o":
		c[0] = "x"
		win()
	elif c[0] == "o":
		c[2] = "x"
		tie_after_bot()


#case_5_3_1 and case_5_3_2 and case_5_4_1 and case_5_4_2
if glob == 5.31:
	if c[2] != "o":
		c[2] = "x"
		win()
	elif c[2] == "o":
		b[0] = "x"
		tie_after_bot()
elif glob == 5.32:
	if b[2] != "o":
		b[2] = "x"
		win()
	elif b[2] == "o":
		b[0] = "x"
		tie_after_bot()
elif glob == 5.41:
	if c[0] != "o":
		c[0] = "x"
		win()
	elif c[0] == "o":
		b[2] = "x"
		tie_after_bot()
elif glob == 5.42:
	if b[0] != "o":
		b[0] = "x"
		win()
	elif b[0] == "o":
		b[2] = "x"
		tie_after_bot()


#case_6_1
if glob == 6.1:
	if a[2] != "o": 
		a[2] = "x"
		win()
	elif a[2] == "o":
		c[2] = "x"
		tie_after_bot()

#case_6_2:
if glob == 6.2:
	if c[2] != "o":
		c[2] = "x"
		win()
	elif c[2] == "o":
		a[2] = "x"
		tie_after_bot()


#case_6_3_1 and case_6_3_2 and case_6_4_1 and case_6_4_2
if glob == 6.31:
	if a[2] != "o":
		a[2] = "x"
		win()
	elif a[2] == "o":
		c[1] = "x"
		tie_after_bot()
elif glob == 6.32:
	if a[1] != "o":
		a[1] = "x"
		win()
	elif a[1] == "o":
		c[1] = "x"
		tie_after_bot()
elif glob == 6.41:
	if c[2] != "o":
		c[2] = "x"
		win()
	elif c[2] == "o":
		a[1] = "x"
		tie_after_bot()
elif glob == 6.42:
	if c[1] != "o":
		c[1] = "x"
		win()
	elif c[1] == "o":
		a[1] = "x"
		tie_after_bot()