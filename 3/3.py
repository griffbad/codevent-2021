import numpy as np
from operator import methodcaller

with  open('input.txt') as f:
	lines = f.readlines()

# lines = np.asarray(lines).astype(str)

gamma = 0
epsilon = 0

lines = [list(x) for x in lines]
lines = np.asarray(lines)

counts = [np.unique(lines[:, x], return_counts = True) for x in np.arange(lines.shape[1])]

gamma_list = [x[0][np.argmax(x[1])] for x in counts]
epsilon_list = [x[0][np.argmin(x[1])] for x in counts]
gamma = int(''.join(gamma_list), 2)
epsilon = int(''.join(epsilon_list), 2)

print(f'gamma = {gamma}, epsilon = {epsilon}, mult = {gamma*epsilon}')

ox = np.copy(lines)
co2 = np.copy(lines)
ox_fin = None
co2_fin = None

for i in np.arange(lines.shape[1]-1):
	curr_ox = np.unique(ox[:,i], return_counts=True)
	curr_co2 = np.unique(co2[:,i], return_counts=True)
	curr_max = curr_ox[0][np.argmax(curr_ox[1])]
	curr_min = curr_co2[0][np.argmin(curr_co2[1])]
	if len(curr_ox[1])==2 and  curr_ox[1][0] == curr_ox[1][1]:
		curr_max = 1
	if len(curr_co2[1])==2 and curr_co2[1][0] == curr_co2[1][1]:
		curr_min = 0
	ox = ox[ox[:,i]==str(curr_max)]
	co2 = co2[co2[:,i]==str(curr_min)]
	if len(ox) == 1:
		ox_fin = ox
	if len(co2) == 1:
		co2_fin = co2
#	if ox_fin and co2_fin:
#		break

ox = int(''.join(ox_fin[0, :-1]), 2)
co2 = int(''.join(co2_fin[0, :-1]), 2)

print(f'ox: {ox}')
print(f'co2: {co2}')
print(f'mult: {co2*ox}')
