def get_num_words(text):
    words = text.split()
    return len(words)

def character_counter(text):
	lower_text=text.lower()
	character_list=list(lower_text)
	count = {}
	for character in character_list:
		if character in count:
	    		count[character]+=1
		else: count[character] = 1 
	return count

def sort_character_counter(character_count):
	double_key_list=[]
	for character in character_count:
		double_key_list.append({"char": character, "num":character_count[character]})
	def get_num(item):
		return item["num"] 
	double_key_list.sort(reverse=True, key=get_num)
	return double_key_list
