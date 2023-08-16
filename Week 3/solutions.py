def expanding(l: list):
	flag = True
	for i in range(len(l) - 2):
		prev = abs(l[i] - l[i + 1])
		curr = abs(l[i + 1] - l[i + 2])
		if prev < curr:
			continue
		else:
			return False
	return flag

def sumsquare(l: list):
	sum_odd, sum_even = 0, 0
	for n in l:
		if n % 2:
			sum_odd += n ** 2
		else:
			sum_even += n ** 2
	return [sum_odd, sum_even]

def transpose(m: list):
	return [[m[j][i] for j in range (len(m))] for i in range (len(m[0]))]
