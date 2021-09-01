#! /usr/bin/env python3
# -*-coding:utf-8-*-

""" 
	Game horse
	author Evgeniy Tulenev (c)
	Boroviha 2021 year 
	stage preparation
"""
import random
import math

def goodplace(source):
	h = 0
	p = 0
	for i in source:
		for j in i:
			if (j == 1):
				h+=1
			if (j == 0):
				p+=1
	if (h*p != 0):
		if (h / p <= 2 /3):
			return 1
		else:
			return 0
	return 0 

def gameplace(m, n):
	deltlp = [[2,1], [1, 2], [-1, -2], [-2, -1], [-1, 2], [-2, 1], [1, -2], [2, -1]]
	blp = [[0 for i in range(n)] for i in range(m)]
	blp[m-1][n-1] = 2
	while(goodplace(blp) != 1):
		blp = [[0 for i in range(n)] for i in range(m)]
		blp[m-1][n-1] = 2
		y = m - 1
		x = n - 1
		while((x != 0) or (y != 0)):
			ij = random.choice(deltlp)
			blp[m-1][n-1] = 2
			if((0 <= x + ij[0] < n) and (0 <= y + ij[1] < m)):
				x += ij[0]
				y += ij[1]
				blp[y][x] = 1

	return blp

def placeprint(source):
	for i in source:
		for j in i:
			print(j, end = '')
		print()

lp = gameplace(8, 8)

placeprint(lp)
