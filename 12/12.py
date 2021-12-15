import numpy as np
from tqdm import tqdm

#with open('test.txt') as f:
with open('input.txt') as f:
	lines = f.read().splitlines()

#print(lines)

lines = np.asarray([x.split('-') for x in lines])

map_dict = dict.fromkeys(lines.flatten(),np.asarray([], dtype=str))
#print(map_dict.values())

for i in lines:
	#print(i)
	entry=[]
	#print(i[0])
	#print(i[1])
	#print(f'{i[0]}: {map_dict[i[0]]}')
	entry = map_dict[i[0]]
	entry = np.append(entry, i[1])
	#print(entry)
	map_dict[i[0]] = entry.tolist()
	entry = map_dict[i[1]]
	entry = np.append(entry, i[0])
	map_dict[i[1]] = entry.tolist()


def visit_all(start, visited, path):
	visitor = visited
	path=np.append(path, start)
	#print(start)
	possible = [x for x in map_dict[start] if x not in visited]
	#print(f'{start}: {possible}')
	if start == 'end':
		#print(path)
		return 1
	elif len(path)>1 and start=='start':
		return 0
	elif len(possible) == 0:
		return 0
	else:
		if start.islower():
			visitor=np.append(visitor,start)
		#print(visitor)
		return sum([visit_all(x,visitor,path) for x in possible])

def visit_all_2(start, visited, path, virginity):
	visitor = visited
	#print(start)
	possible = map_dict[start]
	if (start.islower() and start in visited) or (virginity==1):
		possible = [x for x in possible if x not in visited]
		virginity=1
	path = np.append(path, start)

	#print(f'{start}: {possible}')
	if start == 'end':
		#print(path)
		return 1
	elif len(path)>1 and start == 'start':
		return 0
	elif len(possible) == 0:
		return 0
	else:
		if start.islower():
			visitor=np.append(visitor,start)
		#print(visitor)
		return sum([visit_all_2(x,visitor,path, virginity) for x in possible])

print(visit_all('start',[], []))
print(visit_all_2('start', [], [], 0))

