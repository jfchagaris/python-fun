def add_to_list(a_list,new_item):
	
	if new_item in a_list:
		#pos = a_list.index(new_item)
		#a_list[pos] = new_item
		return False
	else:
		#a_newer_list = 
		a_list.append(new_item)
		print(a_list)
		#print(a_newer_list)

my_list = ['tree','flower','a','b','c','d']

my_list_new = add_to_list(my_list,'smelly')