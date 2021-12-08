import numpy as np
import itertools

with open('input.txt') as f:
	lines = np.asarray(f.read().splitlines())

#print(lines)

np_lines = []
for line in lines:
	line = ",".join(line.split(" ")[0::2])
	line = line.split(',')
	line = np.asarray(line, dtype=int).tolist()
	np_lines.append(line)

points = np.arange(1000)
all_combos = list(itertools.product(points, points))
count_dict = dict.fromkeys(all_combos, 0)
#print(list(count_dict.keys())[:5])
#print(len(count_dict[(0,0)]))
count = []
for line in np_lines:
	if line[0] == line[2]:
		maxy = max([line[1], line[3]])
		miny = min([line[1], line[3]])
		ys = np.arange(miny, maxy+1)
#		print(len(ys))
		xs = [line[0]] * len(ys)
		for loc in list(zip(xs, ys)):
#			print(loc)
#			if count_dict[loc]>0:
#				count.append(loc)
			count_dict[loc]+=1
	elif line[1] == line[3]:
		maxx = max([line[0], line[2]])
		minx = min([line[0], line[2]])
		xs = np.arange(minx, maxx+1)
		ys = [line[1]] * len(xs)
#		print(len(xs))		
		for loc in list(zip(xs, ys)):
#			print(loc)
#			if count_dict[loc]>0:
#				count.append(loc)
			count_dict[loc]+=1
	else:
		maxx = max([line[0], line[2]])
		minx = min([line[0], line[2]])
		maxy = max([line[1], line[3]])
		miny = min([line[1], line[3]])
		
		xs = np.arange(minx, maxx+1)
		ys = np.arange(miny, maxy+1)
		if line[0]>line[2]:
			xs = xs[::-1]
		if line[1]>line[3]:
			ys = ys[::-1]
		if len(xs) != len(ys) or len(xs) == 0 or len(ys) == 0:
			print('ERR')
		for loc in list(zip(xs, ys)):
#			print(loc)
			count_dict[loc]+=1
#print(line)
vals = np.asarray(list(count_dict.values()))
print(len(vals[vals>1]))
#print(count)
#vals, cnts = np.unique(count, return_counts=True)
#print(len(cnts))
