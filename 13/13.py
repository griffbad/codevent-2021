import numpy as np
from tqdm import tqdm

#with open('test.txt') as f:
with open('input.txt') as f:
	lines = f.read().splitlines()

dots = np.asarray([tuple(map(int, x.split(','))) for x in lines if len(x)>0 and len(x.split(','))==2])

instr = lines[len(dots)+1:]

#print(dots)
#print(instr)

maxx = max(dots[:,0])
maxy = max(dots[:,1])

full_sheet = np.full([maxx+1, maxy+1], '.')


for i in dots:
	#print(tuple(i))
	full_sheet[tuple(i)] = '#'

full_sheet = full_sheet.T

folded = np.full([maxy+1, maxx+1], '.')
for i in instr:
	loc = i.split(' ')[-1]
	loc = loc.split('=')
	if loc[0] == 'y':
		for i in np.arange(int(loc[1])+1):
			#print(full_sheet[i])
			#print(full_sheet[-1-i])
			folded[i]= np.where(full_sheet[-1-i]=='#','#',full_sheet[i]) 
		folded=folded[:i]
	if loc[0] == 'x':
		#print(loc)
		full_sheet = full_sheet.T
		folded = folded.T
		#print(full_sheet.shape)
		#print(folded.shape)
		for i in np.arange(int(loc[1])+1):
			#print(full_sheet[i])
			#print(full_sheet[-1-i])
			folded[i]= np.where(full_sheet[-1-i]=='#','#',full_sheet[i]) 
		folded=folded[:i]
		full_sheet=full_sheet.T
		folded=folded.T	
	full_sheet = folded	

print(full_sheet)
dot_count = len(np.where(full_sheet=='#')[0])
print(f'there are {dot_count} #s')

def printer(sheet):
	for i in sheet:
		print(''.join(i))

printer(full_sheet)
