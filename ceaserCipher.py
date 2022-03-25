from random import randint
import csv
def get_range(number, size, min_value, max_value):
    all_ranges = []
    idx = 0
    for _ in range(size+1):
        c_min = number - (size - idx)
        c_max = number + idx
        if c_min >= min_value and c_max <= max_value:
            all_ranges.append([str(c_min), str(c_max)])
        idx+=1
    random_range_index = randint(0,len(all_ranges)-1)
    return ' to '.join(all_ranges[random_range_index])


def encrypt(text,s):
	result = ""
	for i in range(len(text)):
		char = text[i]
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)
	return result
range_size = 3
data = open('data.csv','r')
data = data.read().split()
output = open('output.csv','w')
output = csv.writer(output)

output.writerow(['Pc Name', 'Key', 'Range', 'Encrypted Message'])
for pc_num in data:
    key = randint(1,25)
    current_range = get_range(key, range_size, 0, 25)
    en_msg = encrypt(pc_num, key)
    output.writerow([pc_num, key, current_range, en_msg])

text = "Techteam01"
s = 5
print ("Text : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(text,s))
