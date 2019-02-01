with open('recept.txt') as f:
	def add_cook_book():
		cook_book = dict()
		for line in f:
			recept = line.strip()
			ingridient_count = f.readline()
			cook_book.setdefault(recept, list())
			for r in range(int(ingridient_count)):
				rec = f.readline().strip().split('|')
				ing = {'ingridient_name': rec[0], 'quantity': rec[1], 'measure': rec[2]}
				cook_book[recept].append(ing)
			f.readline()
		return cook_book
		
	def get_shop_list_by_dishes(dishes, person_count):
		rmk = list()
		n_rec = dict()
		rmk = dishes
		cbk = add_cook_book()
		for i in cbk.keys():
			for g in rmk:
				if g == i:
					for j in cbk[g]:
						j_dict = {'quantity': int(j['quantity'])  * person_count, 'measure': j['measure']}
						n_rec.setdefault(j['ingridient_name'], j_dict)
		print(n_rec)	
		
	
	get_shop_list_by_dishes(['Фахитос', 'Омлет'],2)
	
			
