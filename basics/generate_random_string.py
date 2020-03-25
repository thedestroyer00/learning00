# To genterate random string in python 

import random
import string

def string_generate(str_length):
	rand_str = string.ascii_letters
	return ''.join(random.choice(rand_str) for i in range(str_length))

length = random.randint(1,9)
print(string_generate(length))

