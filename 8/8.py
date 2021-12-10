import numpy as np

#with open('test.txt') as f:
with open('input.txt') as f:
	lines = f.read().splitlines()

#print(np.asarray(lines).shape)


num_count = 0
for line in lines:
	read = line.split('|')[-1]
	chars = read.split(' ')[1:]
	#print(chars)
	lens = [len(x) for x in chars if len(x) in [2,3,4,7]]
	#print(len(lens))
	num_count += len(lens)

print(f"there are {num_count} 1, 4, 7, and 8s in the data")

sum = 0
	
for line in lines:
	[code, read] = line.split('|')

	code = code.split(' ')[:-1]
	read = read.split(' ')[1:]
	
	key_dict = {}
	start_key = [x for x in code if len(x) in [2,3,4,7]]
	rest_key = [x for x in code if len(x) == 6]
	final_key = [x for x in code if len(x) == 5]
	for key in start_key:
		if len(key) == 2:
			key_dict[1] = key
		elif len(key) == 3:
			key_dict[7] = key
		elif len(key) == 4:
			key_dict[4] = key
		elif len(key) == 7:
			key_dict[8] = key
	
	for key in rest_key:  
		if np.all([x in key for x in key_dict[4]]): # 9 has to have all the elements of 4
			key_dict[9] = key
		elif np.all([x in key for x in key_dict[1]]): # 0 has to have both elements of 1 (6 won't)
			key_dict[0] = key
		else:
			key_dict[6] = key
	
	for key in final_key:		
		if np.all([x in key for x in key_dict[1]]): # 3 has to have all the elements of 1
			key_dict[3] = key
		elif np.all([x in key_dict[6] for x in key]):
			key_dict[5] = key
		else:
			key_dict[2] = key

	rev_key_dict = dict((v,k) for k,v in key_dict.items())
	#print(rev_key_dict)
	out_num = ''
	#print(read)
	for num in read:
		for key in rev_key_dict.keys():
			#print(key)
			if np.all([x in key for x in num]) and np.all([x in num for x in key]):
				out_num+=str(rev_key_dict[key])
	#print(out_num)
	#print(key_dict)
	#print(''.join(out_num))
	out_num_int = int(''.join(out_num))
	sum += out_num_int

print(f'final sum is {sum}')
