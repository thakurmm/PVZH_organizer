import random
import matplotlib.pyplot as plt

block_possibilities = [1,2,3]

def one_block(block_possibilities):
	block_amount = random.choice(block_possibilities)
	return block_amount

def set_of_blocks(num_blocks):
	total_block_amount = 0
	for block in range(num_blocks):
		total_block_amount += one_block(block_possibilities)
	return total_block_amount

def simulation_set_of_blocks(n, num_blocks):
	all_total_block_amounts = {}
	for trial in range(n):
		total_block_amount = set_of_blocks(num_blocks)
		if total_block_amount in all_total_block_amounts:
			all_total_block_amounts[total_block_amount] += 1
		else:
			all_total_block_amounts[total_block_amount] = 1
	print all_total_block_amounts
	return all_total_block_amounts

simulation_dist = simulation_set_of_blocks(100000, 5)
plt.bar(simulation_dist.keys(), simulation_dist.values(), color='blue')
plt.show()
