#!/Users/mohit/anaconda/bin/python
#/usr/local/bin/python3


import sys
import math
import operator as op
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Binomial_distribution:
	def ncr(self, n, r):
		# found at <https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python#4941932>
		# May make own without operator module, but this is fast/efficient for now
	    r = min(r, n-r)
	    numer = reduce(op.mul, xrange(n, n-r, -1), 1)
	    denom = reduce(op.mul, xrange(1, r+1), 1)
	    return numer//denom

	def binomial_probability(self, n, k, p):
		# Find P( X = k )
		binom_coeff = self.ncr(n,k)
		probability = binom_coeff * p**k * (1-p)**(n-k)
		return probability

	def test_ncr(self):
		print self.ncr(3,3)
		print self.ncr(2,2)
		print self.ncr(2,1)
		print self.ncr(3,1)
		print self.ncr(3,2)
		print self.ncr(10,3)
	# test_ncr()

	def test_binomial_probability(self):
		print self.binomial_probability(1,1,1)
		print self.binomial_probability(3,0,0.5)
		print self.binomial_probability(3,1,0.5)
		print self.fbinomial_probability(3,2,0.5)
		print self.binomial_probability(3,3,0.5)
	# test_binomial_probability()


	def create_univariate_distribution(self, n1, p1):
		# creates a distribution of probabilities, i.e. the probability of getting
		# exactly 2 Super-Rares in a pack is found with key 2
		pack_distribution = {}
		for i in range (n1+1):	# n1 = 11
			pack_probability = self.binomial_probability(n1, i, p1)
			pack_distribution[i] = pack_probability
			print (i, pack_probability)

		# find the most probable number of SR or L in Multipack
		# print max(pack_distribution.iteritems(), key=op.itemgetter(1))[0]
		return pack_distribution

	def create_bivariate_distribution(self, n1, p1, n2, p2):
		# creates a distribution of probabilities, i.e. the probability of getting
		# exactly 2 Super-Rares and 1 Legendary in a pack is found with key (2,1)
		pack_distribution = {}
		x_key = 0
		for i in range (n1+1):	# n1 = 11
			for j in range (n2+1):	# n2 = 11
				pack_probability = self.binomial_probability(n1, i, p1) * self.binomial_probability(n1, j, p2)
				# pack_distribution[(i,j)] = pack_probability
				pack_distribution[x_key] = pack_probability
				x_key += 1
				print (x_key, pack_probability)

		# find the most probable number of SR and L in Multipack
		# print max(pack_distribution.iteritems(), key=op.itemgetter(1))[0]
		return pack_distribution



## ------ MAIN STARTS HERE ------- 

if __name__ == '__main__':
	# Probability of getting a super-rare in one pack
	P_SR = 0.3
	# Probability of getting a legendary in one pack
	P_L = 0.1


	# obj1 = Binomial_distribution()
	# obj2 = Binomial_distribution()
	# SR_pack_distribution = obj1.create_univariate_distribution(11, P_SR)
	# L_pack_distribution = obj2.create_univariate_distribution(11, P_L)

	# print (SR_pack_distribution)
	# print (L_pack_distribution)

	# plt.bar(SR_pack_distribution.keys(), SR_pack_distribution.values(), color='purple')
	# plt.show()
	# plt.bar(L_pack_distribution.keys(), L_pack_distribution.values(), color='orange')
	# plt.show()

	obj = Binomial_distribution()
	pack_distribution = obj.create_bivariate_distribution(11, P_SR, 11, P_L)

	print (pack_distribution)

	plt.bar(pack_distribution.keys(), pack_distribution.values(), color='blue')
	plt.show()

	sys.exit()