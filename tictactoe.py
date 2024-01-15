# Tic Tac Toe!
# Uses the MiniMax algorithm to defeat you ;D

# imports and stuff
import random
from math import ceil, inf

# difficulty constants
easy = 'easy'
medium = 'medium'
impossible = 'impossible'

# returns a fresh, empty board
def new_board():
	return [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
	
# checks if a spot is free
def is_free(board, row, col):
	return board[row][col] in 'abcdefghi'

# returns the number of free spots in the board
def free_spots(board):
	free_spots = 0
	for row in range(3):
		for col in range(3):
			if is_free(board, row, col):
				free_spots += 1
	return free_spots

# tells if someone has won yet or not	
def winner(board):
	
	for num in range(3):
		
		# horizontally
		if board[num][0] == board[num][1] and board[num][1] == board[num][2]:
			return board[num][0]
			
		# vertically
		if board[0][num] == board[1][num] and board[1][num] == board[2][num]:
			return board[0][num]
	
	# diagonally
	if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
		return board[1][1]
	if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
		return board[1][1]
	
	# checks if the board is filled up with no winner, then it's a tie
	for row in range(3):
		for col in range(3):
			if not (board[row][col] == 'X' or board[row][col] == 'O'):
				return None
	else:
		return 'Nobody'	

# plays a move at a chosen spot for a chosen player
def play_move(board, spot, player):
	for row in range(3):
		for col in range(3):
			if (spot not in 'XO') and board[row][col] == spot:
				board[row][col] = player
				return True
	return False
	
# returns the best possible score for a player
def minimax(board, depth, is_maximising):
	if winner(board) == 'X': return 1
	elif winner(board) == 'O': return -1
	elif winner(board) == 'Nobody': return 0
	
	# return a score if we've already reached the deepest depth
	if depth == 0:
		if winner(board) == 'X': return 1
		elif winner(board) == 'O': return -1
		else: return 0
		
	if is_maximising:
		bestScore = -inf
		for row in range(3):
			for col in range(3):
				if board[row][col] in 'abcdefghi':
					temp = board[row][col]
					board[row][col] = 'X'
					score = minimax(board, depth-1, False)
					board[row][col] = temp
					bestScore = max(score, bestScore)
		return bestScore # best maximum score possible
		
	else:
		bestScore = inf
		for row in range(3):
			for col in range(3):
				if board[row][col] in 'abcdefghi':
					temp = board[row][col]
					board[row][col] = 'O'
					score = minimax(board, depth-1, True)
					board[row][col] = temp
					bestScore = min(score, bestScore)
		return bestScore # best minimum score possible

# returns the best possible move spot for a player and given depth
def best_move(board, player, diff):
	if diff == easy:
		return random.choice('abcdefghi')
	elif diff == medium:
		depth = ceil(free_spots(board)/2)
	elif diff == impossible:
		depth = free_spots(board)
	best_score = -inf if player == 'X' else inf
	for row in range(3):
		for col in range(3):
			if board[row][col] in 'abcdefghi':
				temp = board[row][col]
				board[row][col] = player
				is_maximising = not (player == 'X')
				score = minimax(board, depth-1, is_maximising)
				if player == 'X':
				    if score > best_score:
					    best_score = score
					    best_move_spot = temp
				else:
				    if score < best_score:
					    best_score = score
					    best_move_spot = temp
				board[row][col] = temp
	return best_move_spot