import numpy as np

#with open('test.txt') as f:
with open('input.txt') as f:
	lines = f.read().splitlines()

full_mat = []

for line in lines:
	full_mat.append(list(map(int, list(line))))

full_mat = np.asarray(full_mat)

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

print(len(min_locs))
#print(min_vals)
#print([fuller_mat[x] for x in min_locs])
print(f"sum is {sum(min_vals) + len(min_vals)}")

