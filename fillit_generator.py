# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fillit_generator.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nlavrine <nlavrine@student.unit.ua>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/12/26 21:20:29 by nlavrine          #+#    #+#              #
#    Updated: 2018/12/26 21:20:32 by nlavrine         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from random import randint, choice

def put_to_file(i, tetraminos, filename):
	f = open(filename, 'a')
	if (i != 0):
		f.write('\n')
	for i in range(4):
		for j in range(4):
			f.write(tetraminos[i][j])
		f.write('\n')

def	get_random_position(start_row, start_column):
	if (randint(0, 1) == 1):
		start_row = randint(start_row - 1 if start_row - 1 >= 0 else start_row,
							start_row + 1 if start_row + 1 <= 3 else start_row)
	else:
		start_column = randint(start_column - 1 if start_column - 1 >= 0 else start_column,
							start_column + 1 if start_column + 1 <= 3 else start_column)
	return (start_row, start_column)

def random_tetraminos():
	fill_tetraminos = [['.' for _ in range(4)] for _ in range(4)]
	start_row = randint(0, 3)
	start_column = randint(0, 3)
	count_of_grid = 0
	while (count_of_grid < 4):
		if (fill_tetraminos[start_row][start_column] != '#'):
			fill_tetraminos[start_row][start_column] = '#'
			start_row, start_column = get_random_position(start_row, start_column)
			count_of_grid += 1
		else:
			start_row, start_column = get_random_position(start_row, start_column)
	return fill_tetraminos

def clear_file(name):
	f = open(name, 'w')
	f.close()

def	generate_random_tetraminos(num, filename):
	clear_file(filename)
	for i in range(num):
		put_to_file(i, random_tetraminos(), filename)

filenames = []
nums_of_tetraminos = []
for i in range(len(sys.argv)):
	if (sys.argv[i] == "-o" and i + 1 < len(sys.argv)):
		filenames.append(sys.argv[i + 1])
	elif (sys.argv[i] == "-n" and i + 1 < len(sys.argv)):
		nums_of_tetraminos.append(int(sys.argv[i + 1]))

if (min(len(filenames), len(nums_of_tetraminos)) == 0):
	print("usage: fillit_generator -o (filename) -n (number of tetraminos)")

for i in range(min(len(filenames), len(nums_of_tetraminos))):
	generate_random_tetraminos(nums_of_tetraminos[i], filenames[i])



