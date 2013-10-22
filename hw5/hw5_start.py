def read_board(board_filename):
	bd = []
	for line in open(board_filename):
		bd.append(line.strip())
	return bd

def print_board(board):
	# This function should take in a list of strings and print the board
	for line in board:
		t = ""
		for c in line:
			t += c
			t += " "
		print t

def find_word_in_puzzle(board, word):
	# This function shoud call eight functions (one for each direction)
	# An example call:  is_word_going_right(board, word, row, col)
	# See the HW 5 pdf.
	for i in range(0, len(board)):
		for j in range(0, len(board[i])):
			if board[i][j] == word[0]:
				if right(board, word, i, j):
					return [True, "Right", i, j]
				if left(board, word, i, j):
					return [True, "Left", i, j]
				if down(board, word, i, j):
					return [True, "Down", i, j]
				if up(board, word, i, j):
					return [True, "Up", i, j]
				if downRight(board, word, i, j):
					return [True, "Down Right", i, j]
				if downLeft(board, word, i, j):
					return [True, "Down Left", i, j]
				if upRight(board, word, i, j):
					return [True, "Up Right", i, j]
				if upLeft(board, word, i, j):
					return [True, "Up Left", i, j]
	return [False]

def right(board, word, row, col):
	for i in range(0, len(word)):
		if col + i < len(board[row]):
			if word[i] != board[row][col + i]:
				return False
		else:
			return False
	return True

def left(board, word, row, col):
	for i in range(0, len(word)):
		if col - i >= 0:
			if word[i] != board[row][col - i]:
				return False
		else:
			return False
	return True

def down(board, word, row, col):
	for i in range(0, len(word)):
		if row + i < len(board):
			if word[i] != board[row + i][col]:
				return False
		else:
			return False
	return True

def up(board, word, row, col):
	for i in range(0, len(word)):
		if row - i >= 0:
			if word[i] != board[row - i][col]:
				return False
		else:
			return False
	return True

def downRight(board, word, row, col):
	for i in range(0, len(word)):
		if row + i < len(board) and col + i < len(board[row + i]):
			if word[i] != board[row + i][col + i]:
				return False
		else:
			return False
	return True

def downLeft(board, word, row, col):
	for i in range(0, len(word)):
		if row + i < len(board) and col - i >= 0:
			if word[i] != board[row + i][col - i]:
				return False
		else:
			return False
	return True

def upRight(board, word, row, col):
	for i in range(0, len(word)):
		if row - i >= 0 and col + i < len(board[row - i]):
			if word[i] != board[row - i][col + i]:
				return False
		else:
			return False
	return True

def upLeft(board, word, row, col):
	for i in range(0, len(word)):
		if row - i >= 0 and col - i >= 0:
			if word[i] != board[row - i][col - i]:
				return False
		else:
			return False
	return True



if __name__ == '__main__':
	board_filename = raw_input("Enter the file containing the board ==> ")
	print board_filename
	print # print an empty line

	# board is a list of strings (a bit simpler than the Sudoku structure)
	board = read_board(board_filename)

	# print the board, you must write this function
	print_board(board)

	print # print an empty line
	words_filename = raw_input("Enter the file containing the words ==> ")
	print words_filename

	print # print an empty line
	for line in open(words_filename):
		word = line.strip()
		isInPuzzle = find_word_in_puzzle(board, word)
		if isInPuzzle[0]:
			print word, "starts in (", isInPuzzle[2], ",", isInPuzzle[3], ") and runs", isInPuzzle[1]
		else:
			print word, "not found"
