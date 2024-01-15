# Tic Tac Toe in CLI!
# Uses the MiniMax algorithm to defeat you ;D

# imports and stuff
from tictactoe import *
	
# prints the board to screen nicely (I guess)
def show_board(board):
	print('\n-----------')
	print('Present state of board:')
	print('-----------')
	print("", board[0][0], "|", board[0][1], "|", board[0][2], "")
	print("——— ——— ———")
	print("", board[1][0], "|", board[1][1], "|", board[1][2], "")
	print("——— ——— ———")
	print("", board[2][0], "|", board[2][1], "|", board[2][2], "")
	print('-----------\n')
	
# takes move input from a human player and plays it
def human_input(board, player_1):
	while True:
		player_name = 'Player 1' if player_1 else 'Player 2'
		symbol = 'X' if player_1 else 'O'
		spot = input(player_name + ', enter letter of spot to enter "' + symbol + '": ')
		if play_move(board, spot, symbol):
			print(player_name, ' plays "', symbol, '" at ', spot, sep='')
			return not player_1
		else:
			print('That spot isn\'t there. Try again!')

# starts a game against the computer
def play_computer(board):
	print('\nChoose difficulty, 1 or 2:')
	print('1. Easy')
	print('2. Medium')
	print('3. Impossible')
	diff = input('> ')
		
	print('\nChoose who goes first, 1 or 2:')
	print('1. You')
	print('2. Computer')
	player_1 = True if input('> ') == '1' else False
	
	# easy difficulty - computer plays random moves	
	if diff == '1':
		while(not winner(board)):
			show_board(board)
			if player_1:
				player_1 = human_input(board, player_1)
				continue
			else:
				while True:
					spot = best_move(board, 'O', )
					if play_move(board, spot, 'O'):
						player_1 = True
						print('Computer plays "O" at', spot)
						break
				continue
	
	# medium difficulty - computer plays best move based on limited depth	
	elif diff == '2':
		while(not winner(board)):
			show_board(board)
			if player_1:
				player_1 = human_input(board, player_1)
				continue
			else:
				spot = best_move(board, 'O', medium)
				play_move(board, spot, 'O')
				player_1 = True
				print('Computer plays "O" at', spot)
				continue
	
	# impossible difficulty - computer plays best move based on full depth
	elif diff == '3':
		while(not winner(board)):
			show_board(board)
			if player_1:
				player_1 = human_input(board, player_1)
				continue
			else:
				spot = best_move(board, 'O', impossible)
				play_move(board, spot, 'O')
				player_1 = True
				print('Computer plays "O" at', spot)
				continue

# starts a game between two human players			
def play_human(board):
	player_1 = True
	while(not winner(board)):
		show_board(board)
		player_1 = human_input(board, player_1)

def main():
	print('Welcome to Tic Tac Toe!')
	
	while True:
	    print('\nChoose 1, 2 or 3:')
	    print('1. Play vs computer')
	    print('2. Play vs another human')
	    print('3. Exit')
	    choice = input('> ')
	    
	    if choice == '1':
	    	board = new_board()
	    	play_computer(board)
	    	print('Board:')
	    	show_board(board)
	    	print('-----------')
	    	print(winner(board), "wins!")
	    	print('-----------')
	    elif choice == '2':
	    	board = new_board()
	    	play_human(board)
	    	print('Board:')
	    	show_board(board)
	    	print('-----------')
	    	print(winner(board), "wins!")
	    	print('-----------')
	    elif choice == '3':
	    	print('Exiting program, thanks for playing! :D')
	    	break
	    else:
	    	print('Invalid input! :(')
	
if __name__ == "__main__":
	main()
	