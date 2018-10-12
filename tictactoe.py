from pprint import pprint
import random

class Player:

	def __init__(self, name, game_piece):
		self.name = name
		self.game_piece = game_piece

	def player_name(self):
		return str(self.name)


class Move:
	"""Move has one player and one board.
	Author is player making move.
	Position is a 2 index list -> [row, column]"""
	def __init__(self, player, position):
		self.player = player
		self.position = position


class Board:
	"""Board has many moves."""
	def __init__(self, moves=[]):
		self.moves = moves


	def display(self):
		"""Prints out the board for users to see it.
		Board is a 3x3 matrix. Update index each time with new move."""
		board = [[' -',' -',' -'], [' -',' -',' -'], [' -',' -',' -']]

		for move in self.moves:
			player = move.player
			position = move.position
			row,col = position

			if player.player_name() == "Computer":
				board[row][col] = " 0"
			else:
				board[row][col] = " X"
		
		row1 = ('').join(board[0])
		row2 = ('').join(board[1])
		row3 = ('').join(board[2])

		print('\n'+row1+'\n'+row2+'\n'+row3+'\n')
		print('*******')

	def add_move(self, move):
		"""Adds move to moves attribute.
		Takes an instance of Move."""
		self.moves.append(move)

	def is_move(self, move):
		for m in self.moves:
			if move.position == m.position:
				return True
		return False



class Game:
	"""Game has one board, two players."""

	def __init__(self, board, player1, player2, started_at=None, finished_at=None):
		self.board = board
		self.player1 = player1
		self.player2 = player2
		self.started_at = started_at
		self.finished_at = finished_at


def random_move(player, board):
	row = random.randint(0,2)
	col = random.randint(0,2)
	move = Move(player,[row,col])
	
	"""If move is already taken, pick different coordinates."""
	while board.is_move(move):
		row = random.randint(0,2)
		col = random.randint(0,2)
		move = Move(player,[row,col])

	return move


def is_won(board):
	pass

# -------------- MAIN -------------
print("Ready to play tic-tac-toe against the computer?")
player_name = input("What's your name? ")
print("\nHi, {}. You get to go first!".format(player_name))
print("To make your move, input a row and column: ie. 1 0")

# create a board + players + game
p1 = Player(player_name, 'X')
comp = Player('Computer', 'O')
board = Board()
game = Game(board, p1, comp)

while True:
	p1_input = input("Make your move (row col): ")
	p1_position = p1_input.split(" ")
	p1_position = [int(i) for i in p1_position]
	p1_move = Move(p1, p1_position)
	
	"""If the board position is taken, make user pick a new coordinate."""
	while board.is_move(p1_move):
		print("\nThat spot is taken! Try again.")
		p1_input = input("Make your move (row col): ")
		p1_position = p1_input.split(" ")
		p1_position = [int(i) for i in p1_position]
		p1_move = Move(p1, p1_position)

	board.add_move(p1_move)
	board.display()

	print("Computer's turn.")
	comp_move = random_move(comp, board)
	board.add_move(comp_move)
	board.display()

	"""If the game is won, print the winner and end session."""
	if is_won(board):
		winner = is_won(board)
		if winner == "Computer":
			print("You lose!")
		else:
			print("Congrats {}! You win!".format(p1.name))
		break