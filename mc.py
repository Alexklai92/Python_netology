import datetime

class FileOpener:
	d_start = datetime.datetime.today()
	
	def __init__(self, path_file):
		self.path_file = path_file
		
	def __enter__(self):
		self.file = open(self.path_file)	
		print(f'Начало работы программы: {self.d_start}')
		return self.file
		
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.file.close()
		d_end = datetime.datetime.today()
		print(f'Конец работы программы: {d_end}')
		delta = d_end - self.d_start
		print(f'Программа выполнялась: {delta}')
	
	
if __name__ == '__main__':
	
	cook_book = {}

	with FileOpener('recept.txt') as f:
		for line in f:
			recept = line.strip()
			ingridient_count = f.readline()
			cook_book.setdefault(recept, list())
			for r in range(int(ingridient_count)):
				rec = f.readline().strip().split('|')
				ing = {'ingridient_name': rec[0], 'quantity': rec[1], 'measure': rec[2]}
				cook_book[recept].append(ing)
			f.readline()
			

	def get_shop_list_by_dishes(dishes, person_count):
		rmk = list()
		n_rec = dict()
		rmk = dishes
		cbk = cook_book.keys()
		for i in cbk:
			for g in rmk:
				if g == i:
					for j in cook_book[g]:
						j_dict = {'measure': j['measure'], 'quantity': int(j['quantity']) * person_count}
						n_rec.setdefault(j['ingridient_name'], j_dict)
						
		print(n_rec)			
	get_shop_list_by_dishes(['Утка по-пекински', 'Омлет' ], 2)
