class Animals:
	min_weight = 100 #gramm
	max_weight = 1500 #gramm
	#weight = 1 #gramm
	is_alive = True
	voice = 'Привет' 
	#Требуется ли работать с животными (стричь и тд)
	is_job = False
	job_weight = 0
	job_value = 'неизвестно'
	sum_weight = []
	big_animal = {}
	
	def leader_animal(self):
		sorted(sum_weight)
		sum_weight.reverse()
		
		for i in self.big_animal:
			for g in self.big_animal[i]:
				if g == self.sum_weight[0]:
					print(big_animal[i])
		
	
	
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
		
		self.sum_weight.append(self.weight)
		self.big_animal.setdefault(self.name, self.weight)
	def who_is(self):
		if self.voice == 'Га-га-га':
			animal = 'Гусь'	
		elif self.voice == 'Муу':
			animal = 'Корова'		
		elif self.voice == 'Бее':
			animal = 'Овца'		
		elif self.voice == 'Ко-ко-ко':
			animal = 'Курица'			
		elif self.voice == 'Мее':
			animal = 'Коза'			
		elif self.voice == 'Кря-кря':
			animal = 'Утка'
		else:
			animal = 'Неизвестное животное!'
		print(animal)
	
	def animal_live(self):
		if self.weight > self.max_weight or self.weight < self.min_weight:
			is_alive = False
			print('Животное мертво')
			self.weight = self.max_weight + 1
		else:
			is_alive = True
		return is_alive
	
	def eating(self, weight):
		if self.weight > self.max_weight / 2:
				print('Кажется, пора заняться животным')
		if self.animal_live():	
			self.weight += weight
			
	def country_work(self):
		if self.weight > self.max_weight / 2:
			self.is_job = True
		
		if self.animal_live():	
			if self.is_job == True:
				print('{} "{}"'.format(self.job_value, self.name))
				self.weight -= self.job_weight #gramm
			else:
				print('Рано')

#Гусь		
class Goose(Animals):
	#У гуся собираем яйца, одно яйцо весит 20 грамм
	voice = 'Га-га-га'
	job_weight = 20 #gramm
	job_value = 'Собираем яйца, у '
		
	max_weight = 3500 #gramm
	min_weight = 500
	#weight = 1200
	
#Корова
class Cow(Animals):
	voice = 'Муу'
	job_weight = 1000 #ml
	job_value = 'Доим корову по имени '
	
	max_weight = 100000
	min_weight = 25000
	#weight =  45000

#Овца			
class Sheep(Animals):
	voice = 'Бее'
	job_weight = 500 #gr
	job_value = 'Стрижем овцу по имени '
	
	max_weight = 30000
	min_weight = 5000
	#weight = 9000

#Курица
class Chicken(Animals):
	voice = 'Ко-ко-ко'
	job_weight = 25 #gramm
	job_value = 'Собираем яйца у '
	
	max_weight = 2500
	min_weight = 300
	#weight = 700	
	
#Коза
class Goat(Animals):
	voice = 'Мее'
	job_weight = 800 #ml
	job_value = 'Доим козу по имени '
	
	max_weight = 55000
	min_weight = 9000
	#weight = 14000

#Утка
class Duck(Animals):
	voice = 'Кря-кря'
	job_weight = 21 #gramm
	job_value = 'Собираем яйца у '
	
	max_weight = 3500
	min_weight = 600
	#weight = 1000
				
goose_0 = Goose('Серый', 1500)
goose_1 = Goose('Белый', 1650)
cow_0 = Cow('Манька', 45000)
sheep_0 = Sheep('Барашек', 19000)
sheep_1 = Sheep('Кудрявый', 21000)
chicken_0 = Chicken('Ко-ко', 1450)
chicken_1 = Chicken('Кукареку', 1850)
goat_0 = Goat('Рога', 27000)
goat_1 = Goat('Копыто', 25550)
duck_0 = Duck('Кряква', 3250)

print('Общий вес животных ', sum(Animals.sum_weight))
Animals.leader_animal(Animals.big_animal)

