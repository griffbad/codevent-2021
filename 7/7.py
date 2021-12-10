import numpy as np

with open('input.txt') as f:
	lines = f.read().splitlines()

pos = np.asarray(lines[0].split(','), dtype=int)
#pos = np.asarray([16,1,2,0,4,2,7,1,2,14])
fuel = []
for i in np.arange(pos.min(), pos.max()):
	fuel.append(sum(abs(pos-i)))
fuel = [sum(abs(np.subtract(pos, np.median(pos))))]
print(f'min human fuel use is {min(fuel)}')

fuel = []
for i in np.arange(pos.min(), pos.max()):
	fuel.append(sum([(abs(x-i)*(abs(x-i)+1))/2 for x in pos]))

print(f'min crab fuel use is {int(min(fuel))}')
