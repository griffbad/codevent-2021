import numpy as np

with open('input.txt') as f:
	nums = f.readlines()

nums = np.asarray(nums, dtype=int)

tot_incs = 0
tot_decs = 0

for loc in np.arange(1, len(nums)):
	if nums[loc]>nums[loc-1]:
		tot_incs += 1
	else:
		tot_decs += 1
print(f"{tot_incs} increases, {tot_decs} decs, {len(nums)} total")

tot_incs_3 = 0
tot_decs_3 = 0
for loc in np.arange(3, len(nums)):
	curr_sum = np.sum([nums[loc-3], nums[loc-2], nums[loc-1]])
	next_sum = np.sum([nums[loc-2], nums[loc-1], nums[loc]])
	if next_sum>curr_sum:
		tot_incs_3+=1
	else:
		tot_decs_3+=1

print(f"{tot_incs_3} increases, {tot_decs_3} decreases")
