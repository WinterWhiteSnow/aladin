
def book_list_split(book_list):
	string_list = book_list.split("[중고]")
	list_list = []
	result_list = []
	for i in string_list:
		a = i.replace(" ","")
		list_list.append(a)
	for i in list_list:
		if i not in "":
			b = i[:i.find("1")]	
			if "(" in b:
				b = b[:b.find("(")]
			if "[" in b:
				b = b[:b.find("[")]
			if "{" in b:
				b = b[:b.find("{")]
			result_list.append(b)
	return result_list
