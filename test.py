import re
with open("input.txt") as f:
	d = {}
	n = []
	last_num = 0
	for line in f:
		num = int(re.sub("\\D", "", line))
		last_num = num
		s = line[line.find(":")+1:]
		d[num] = s[:-1]
		n.append(num)
	
	n.sort()
	n.pop()
	
	a = ""
	for i in n:
		if last_num % i == 0:
			a += d[i]
	
	print(a)
