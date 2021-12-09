import numpy as np

with open('input.txt') as f:
	lines = f.read().splitlines()

fish = np.asarray(lines[0].split(','), dtype=int)

#fish = np.asarray([3,4,3,1,2])
count = 0
fish_dict = dict.fromkeys(np.arange(-1,8), 0)
fish.sort()

for i in fish:
	fish_dict[i] += 1

print(fish_dict)
while count<257:
	temp = fish_dict[7]
	for i in list(fish_dict.keys())[::-1][:-1]:
		store = fish_dict[i-1]
		fish_dict[i-1] = temp
		temp = store
#		print(fish_dict)
	fish_dict[7] = temp
	fish_dict[5] = fish_dict[5] + temp
	count += 1
	print(fish_dict)

print(f"there are now {sum(list(fish_dict.values()))} fish")	
	
