import numpy as np
from tqdm import tqdm

#with open('test.txt') as f:
with open('input.txt') as f:
	lines = f.read().splitlines()

full_mat = []

for line in lines:
	full_mat.append(list(map(int, list(line))))

full_mat = np.asarray(full_mat)[:10, :10]

min_locs = []
min_vals = []

fuller_mat = full_mat.copy()
full_mat = full_mat[1:-1,1:-1]
#print(full_mat.shape)
#print(fuller_mat.shape)
for i, line in enumerate(full_mat):
	for j, char in enumerate(line):
		#print([i+1,j+1])
		box = [fuller_mat[i,j+1], fuller_mat[i+1, j], fuller_mat[i+1,j+1], fuller_mat[i+1,j+2], fuller_mat[i+2,j+1]]
		if np.argmin(box) == 2:
			#print(char)
			min_locs.append([i+1,j+1])
			min_vals.append(char)

for i, char in enumerate(fuller_mat[0,1:-1]):
	box = [fuller_mat[0,i], fuller_mat[0,i+1], fuller_mat[0,i+2], fuller_mat[1,i+1]]
	if np.argmin(box) == 1:
		min_locs.append([0,i+1])
		min_vals.append(char)
		#print(char)

for i, char in enumerate(fuller_mat[-1,1:-1]):
	box = [fuller_mat[-1,i], fuller_mat[-1,i+1], fuller_mat[-1,i+2], fuller_mat[-2,i+1]]
	if np.argmin(box) == 1:
		min_locs.append([-1,i+1])
		min_vals.append(char)
		#print(char)

for i, char in enumerate(fuller_mat[1:-1,0]):
	box = [fuller_mat[i, 0], fuller_mat[i+1,0], fuller_mat[i+2,0], fuller_mat[i+1,1]]
	if np.argmin(box) == 1:
		min_locs.append([i+1,0])
		min_vals.append(char)

for i, char in enumerate(fuller_mat[1:-1,-1]):
	box = [fuller_mat[i, -1], fuller_mat[i+1, -1], fuller_mat[i+2, -1], fuller_mat[i+1, -2]]
	if np.argmin(box) == 1:
		min_locs.append([i+1, -1])
		min_vals.append(char)

char = fuller_mat[0,0]
box = [fuller_mat[0,1], fuller_mat[0,0], fuller_mat[1,0]]

if np.argmin(box) == 1:
	min_locs.append([0,0])
	min_vals.append(char)

char = fuller_mat[0,-1]
box = [fuller_mat[0,-2], fuller_mat[0,-1], fuller_mat[1,-1]]
if np.argmin(box) == 1:
	min_locs.append([0,-1])
	min_vals.append(char)

char = fuller_mat[-1,0]
box = [fuller_mat[-1,1], fuller_mat[-1,0], fuller_mat[-2,0]]
if np.argmin(box) == 1:
	min_locs.append([-1,0])
	min_vals.append(char)

char = fuller_mat[-1,-1]
box = [fuller_mat[-2,-1], fuller_mat[-1,-1], fuller_mat[-1,-2]]
if np.argmin(box) == 1:
	min_locs.append([-1,-1])
	min_vals.append(char)

print(fuller_mat)
min_locs = list(map(tuple, min_locs))
print([fuller_mat[x] for x in min_locs])
#print(min_vals)
#print([fuller_mat[x] for x in min_locs])
print(f"sum is {sum(min_vals) + len(min_vals)}")

bin_fuller_mat = np.where(fuller_mat == 9, 0, 1)
bin_full_mat = np.where(full_mat == 9, 0, 1)
print(bin_fuller_mat)

counter = 2

def make_basin(arr, loc: tuple, all_locs):
	#print(arr.shape)
	#print(loc[0])
	if arr[loc] == 0:
		return []
	else:
		all_locs += [loc]
		new_tups = [tuple(np.add(loc, [0,1])), tuple(np.add(loc, [1,0])),
				tuple(np.add(loc, [-1,0])), tuple(np.add(loc, [0,-1]))]
		print([try: arr[x] except: pass for x in new_tups])
		if loc[1]<arr.shape[1]-1 and new_tups[0] not in all_locs and arr[new_tups[0]]!=0 :
			all_locs += make_basin(arr, new_tups[0],  all_locs)
		if loc[0]<arr.shape[0]-1 and new_tups[1] not in all_locs and arr[new_tups[1]]!=0 :
			all_locs += make_basin(arr, new_tups[1],  all_locs)
		if loc[0]>0 and new_tups[2] not in all_locs and arr[new_tups[2]]!=0 :
			all_locs += make_basin(arr, new_tups[2], all_locs)
		if loc[1]>0 and new_tups[3] not in all_locs and arr[new_tups[3]]!=0 :
			all_locs += make_basin(arr, new_tups[3], all_locs)
		return all_locs

sizes = []
all_visited = []
for i in tqdm(min_locs):
#	print(i)
	loc = list(i)
	if i[0]<0:
		loc[0] = bin_fuller_mat.shape[0] + i[0]
	if i[1]<0:
		loc[1] = bin_fuller_mat.shape[1] + i[1]
	loc = tuple(loc)
	if loc in all_visited:
		continue
	all_basin = make_basin(bin_fuller_mat, loc, [])
	all_basin = list(set([x for x in all_basin if x != ()]))
#	print(f'shape {np.asarray(all_basin).shape}')

	for z in all_basin:
		bin_fuller_mat[z] = counter
	sizes.append(len(all_basin))
	all_visited.append(all_basin)
#	print(all_basin)
	counter += 1

#print(bin_fuller_mat)
print(len(sizes))
print(len(all_visited))
sizes = np.sort(sizes)[::-1]
print(sizes[:3])
print(f'the 3 largest are {sizes[:3]}, mult out to be {np.prod(sizes[:3])}')
