import numpy as np
from tqdm import tqdm

#with open('test.txt') as f:
with open('input.txt') as f:
	lines = f.read().splitlines()

#print(lines)

template = lines[0]
instr = lines[2:]

instr_keys = [x[:2] for x in instr]
instr_vals = [x[-1] for x in instr]
instr_dict = dict(zip(instr_keys, instr_vals))

#print(instr_dict)

def step(template, instrs):
	curr = ''
	#print(curr)
	keys = instrs.keys()
	for loc in np.arange(1, len(template)):
		chars = template[loc-1:loc+1]
		#print(chars)
		if chars in keys:
			#print([chars[0], instrs[chars]])
			curr+=''.join([chars[0], instrs[chars]])
		else:
			curr+=chars[0]			
	return curr+template[-1]

def step_2(template_dict, instrs):
	next_dict = template_dict.copy()
	for i in template_dict.keys():
		count = template_dict[i]
		insert = instrs[i]
		next_dict[''.join([i[0],insert])] += count
		next_dict[''.join([insert,i[1]])] += count
		next_dict[i] -= count
	return next_dict


def scorer(template):
	uniques = np.unique(list(template))
	counts = np.zeros(len(uniques))
	for i, char in enumerate(uniques):
		counts[i] = template.count(char)
	
	return(max(counts)-min(counts))

def scorer_2(template_dict, template):
	uniques = np.unique(list(''.join(template_dict.keys())))
	counts_dict = dict.fromkeys(uniques,0)

	for key in template_dict.keys():
		counts_dict[key[0]] += template_dict[key]
		counts_dict[key[1]] += template_dict[key]
	counts_dict[template[-1]]+=1
	return max(list(counts_dict.values()))/2 - min(list(counts_dict.values()))/2

print(template)
template_dict = dict.fromkeys(instr_keys, 0)
for i in np.arange(1, len(template)):
	template_dict[template[i-1:i+1]] += 1

for i in tqdm(np.arange(40)):
	#print(template_dict)
	#template = step(template, instr_dict)
	template_dict = step_2(template_dict, instr_dict)	
	#print(template)
	#print(len(template))
	
print(scorer_2(template_dict, template))
