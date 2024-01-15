# Tic Tac Toe in GUI!
# Uses the MiniMax algorithm to defeat you ;D

# imports and stuff
import pygame
from tictactoe import *
from colors import *

# game rendering constants
screen_width, screen_height = 400, 600
fps = 60

# other constants
TEXT_SIZE = 66
GAP = 13 # standard gap unit to be used throughout the program to position stuff

pygame.init()
display = pygame.display.set_mode((screen_width, screen_height), 
                                  pygame.SCALED|pygame.RESIZABLE)
pygame.display.set_caption('Tic Tac Toe!')

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, TEXT_SIZE)

# load required images
boardimg = pygame.image.load('images/board.png').convert_alpha()
x = pygame.image.load('images/x.png').convert_alpha()
o = pygame.image.load('images/o.png').convert_alpha()
title_text = pygame.image.load('images/title_text.png').convert_alpha()
play_comp_btn = pygame.image.load('images/play_computer_button.png').convert()
play_human_btn = pygame.image.load('images/play_human_button.png').convert()
easy_btn = pygame.image.load('images/easy_button.png').convert()
medium_btn = pygame.image.load('images/medium_button.png').convert()
impossible_btn = pygame.image.load('images/impossible_button.png').convert()
back_btn = pygame.image.load('images/back_button.png').convert()
restart_btn = pygame.image.load('images/restart_button.png').convert()

# position of the title text to be displayed on all screens
title_pos = [display.get_width()/2 - title_text.get_width()/2, GAP]

def write_text(text, color, x, y):
	screen_text = font.render(text, True, color)
	display.blit(screen_text, [x, y])
	return screen_text
	
def fade_in(image):
	if image.get_alpha() < 255:
		image.set_alpha(image.get_alpha() + 20)

def diff_screen():
	
	easy_pos = [display.get_width()/2 - easy_btn.get_width()/2,
		title_pos[1] + title_text.get_height() + 10*GAP]
	medium_pos = [display.get_width()/2 - medium_btn.get_width()/2,
		easy_pos[1] + easy_btn.get_height() + GAP]
	impossible_pos = [display.get_width()/2 - impossible_btn.get_width()/2,
		medium_pos[1] + medium_btn.get_height() + GAP]
	
	easy_rect = easy_btn.get_rect(x=easy_pos[0], y=easy_pos[1])
	medium_rect = medium_btn.get_rect(x=medium_pos[0], y=medium_pos[1])
	impossible_rect = impossible_btn.get_rect(x=impossible_pos[0],
	                                          y=impossible_pos[1])
	                                          
	easy_btn.set_alpha(0)
	medium_btn.set_alpha(0)
	impossible_btn.set_alpha(0)
	
	# the difficulty screen rendering loop
	while True:
		clock.tick(fps)
		
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				pygame.quit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				# TODO: animate button on mouse down
				pass
			elif event.type == pygame.MOUSEBUTTONUP:
				if easy_rect.collidepoint(event.pos):
					game_screen(new_board(), easy)
				elif medium_rect.collidepoint(event.pos):
					game_screen(new_board(), medium)
				elif impossible_rect.collidepoint(event.pos):
					game_screen(new_board(), impossible)
			
		display.fill(cream)
		display.blit(title_text, title_pos)
		display.blit(easy_btn, easy_pos)
		display.blit(medium_btn, medium_pos)
		display.blit(impossible_btn, impossible_pos)
		pygame.display.flip()
		
		fade_in(easy_btn)
		fade_in(medium_btn)
		fade_in(impossible_btn)
			
def menu_screen():
	
	play_comp_pos = [display.get_width()/2 - play_comp_btn.get_width()/2,
		title_pos[1] + title_text.get_height() + 10*GAP]
	play_human_pos = [display.get_width()/2 - play_human_btn.get_width()/2,
		play_comp_pos[1] + play_comp_btn.get_height() + GAP]
		
	play_comp_rect = play_comp_btn.get_rect(topleft=play_comp_pos)
	play_human_rect = play_human_btn.get_rect(topleft=play_human_pos)
	
	title_text.set_alpha(0)
	play_comp_btn.set_alpha(0)
	play_human_btn.set_alpha(0)
	
	# the menu screen rendering loop
	while True:
		clock.tick(fps)
		
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				pygame.quit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				# TODO: Animate button on mouse down
				pass
			elif event.type == pygame.MOUSEBUTTONUP:
				if play_comp_rect.collidepoint(event.pos):
					diff_screen()
				elif play_human_rect.collidepoint(event.pos):
					game_screen(new_board())
			
		display.fill(cream)
		display.blit(title_text, title_pos)
		display.blit(play_comp_btn, play_comp_pos)
		display.blit(play_human_btn, play_human_pos)
		pygame.display.flip()
		
		fade_in(title_text)
			
		if title_text.get_alpha() == 255:
			fade_in(play_comp_btn)
			fade_in(play_human_btn)		

# loads the game screen
# presence of diff indicates a v/s computer match, else a v/s human match
def game_screen(board, diff=None):
	
	x_small = pygame.transform.scale(x, (TEXT_SIZE, TEXT_SIZE)).convert_alpha()
	o_small = pygame.transform.scale(o, (TEXT_SIZE, TEXT_SIZE)).convert_alpha()
	
	board_pos = [display.get_width()/2 - boardimg.get_width()/2, 
		display.get_height() - boardimg.get_height()]
	
	# a dictionary that maps each spot to its corresponding position
	# represented by position of the top left corner of that spot
	pos_dict = {(0,0): [board_pos[0]+23, board_pos[1]+23],
	            (0,1): [board_pos[0]+151, board_pos[1]+23],
	            (0,2): [board_pos[0]+280, board_pos[1]+23],
	            (1,0): [board_pos[0]+23, board_pos[1]+151],
	            (1,1): [board_pos[0]+151, board_pos[1]+151],
	            (1,2): [board_pos[0]+280, board_pos[1]+151],
	            (2,0): [board_pos[0]+23, board_pos[1]+280],
	            (2,1): [board_pos[0]+151, board_pos[1]+280],
	            (2,2): [board_pos[0]+280, board_pos[1]+280],}
	
	# position of game status text
	status_pos = [GAP, board_pos[1] - TEXT_SIZE - GAP]
	back_pos = [GAP, GAP]
	restart_pos = [display.get_width() - restart_btn.get_width() - GAP, GAP]
	
	back_rect = back_btn.get_rect(topleft=back_pos)
	restart_rect = restart_btn.get_rect(topleft=restart_pos)
	
	waiting_for_input = True
	current_symbol = 'X'
	
	def switch_symbol():
		nonlocal current_symbol
		if current_symbol == 'X':
			current_symbol = 'O'
		else:
			current_symbol = 'X'
	
	# the game screen rendering loop
	while True:
		clock.tick(fps)
		
		for event in pygame.event.get():
			 
			if event.type == pygame.QUIT:
				pygame.quit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				# TODO: animate button on mouse button down
				pass
			elif event.type == pygame.MOUSEBUTTONUP:
				if back_rect.collidepoint(event.pos):
					menu_screen()
				elif restart_rect.collidepoint(event.pos):
					game_screen(new_board(), diff if diff else None)
				
				if waiting_for_input:
					for row in range(3):
						for col in range(3):
							spot_rect = x.get_rect(x=pos_dict[(row, col)][0], 
							                       y=pos_dict[(row, col)][1])
							if (spot_rect.collidepoint(event.pos)
							    and is_free(board, row, col)):
								board[row][col] = current_symbol
								switch_symbol()
								waiting_for_input = False
		
		display.fill(cream)
		display.blit(boardimg, board_pos)
		display.blit(back_btn, back_pos)
		display.blit(restart_btn, restart_pos)
								
		win = winner(board)		
		if not win:
			status_text = write_text('Current turn: ', black, 
			                         status_pos[0], status_pos[1])
			status_rect = status_text.get_rect(topleft=status_pos)
		
			if current_symbol == 'X':
				display.blit(x_small, 
			          (status_rect.right, status_rect.y - font.get_linesize()/4))
			else:
				display.blit(o_small,
			          (status_rect.right, status_rect.y - font.get_linesize()/4))
		else:
			if win == 'X':
				status_text = write_text('WINS!', black, 
			                    x_small.get_width() + GAP*2, status_pos[1])
				status_rect = status_text.get_rect(topleft=status_pos)
				display.blit(x_small, 
			             (GAP, status_rect.y - font.get_linesize()/4))
			elif win == 'O':
				status_text = write_text('WINS!', black, 
			                    o_small.get_width() + GAP*2, status_pos[1])
				status_rect = status_text.get_rect(topleft=status_pos)
				display.blit(o_small,
			             (GAP, status_rect.y - font.get_linesize()/4))
			else:
				write_text('It\'s a TIE!', black, 
				           status_pos[0], status_pos[1])
				
		for row in range(3):
			for col in range(3):
				if board[row][col] == 'X':
					display.blit(x, pos_dict[(row, col)])
				elif board[row][col] == 'O':
					display.blit(o, pos_dict[(row, col)])
		pygame.display.flip()
		
		if (not waiting_for_input) and (not winner(board)):
			if diff == easy:
				while True:
					spot = best_move(board, current_symbol, easy)
					if play_move(board, spot, current_symbol):
						switch_symbol()
						break
			elif diff == medium:
				spot = best_move(board, current_symbol, medium)
				play_move(board, spot, current_symbol)
				switch_symbol()
			elif diff == impossible:
				spot = best_move(board, current_symbol, impossible)
				play_move(board, spot, current_symbol)
				switch_symbol()
			waiting_for_input = True

def main():
	menu_screen()
	
if __name__ == '__main__':
	main()