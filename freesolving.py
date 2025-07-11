text = "Rivers and mountains. Rivers are beautiful. Mountains are tall."

def achar_counter(text):
	l_text=text.lower()
	char_l=list(l_text)
	achar_l=[]
	count = {}
	dk_list = []
	for char in char_l:
		if char.isalpha():
			achar_l.append(char)
	for letter in achar_l:
		if letter in count:
			count[letter] += 1
		else: count[letter] = 1 
	for entry in count:
		dk_list.append({"char": entry, "num": count[entry]})
	def get_num(dict):
		return dict["num"]
	dk_list.sort(reverse=True, key=get_num)
	for dict in dk_list:
		print (f"{dict['char']}: {dict['num']}")
achar_counter(text)
