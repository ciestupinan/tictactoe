from pprint import pprint

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

			if player.player_name() == "P1":
				board[row][col] = " X"
			else:
				board[row][col] = " O"
		
		row1 = ('').join(board[0])
		row2 = ('').join(board[1])
		row3 = ('').join(board[2])

		print('\n'+row1+'\n'+row2+'\n'+row3+'\n')
		print('*******')

	def add_move(self, move):
		"""Adds move to moves attribute.
		Takes an instance of Move."""
		self.moves.append(move)


class Game:
	"""Game has one board, two players."""

	def __init__(self, board, player1, player2, started_at=None, finished_at=None):
		self.board = board
		self.player1 = player1
		self.player2 = player2
		self.started_at = started_at
		self.finished_at = finished_at

# create a board + players
p1 = Player('P1', 'X')
p2 = Player('P2', 'O')
board = Board()

# create a game
my_game = Game(board, p1, p2)

# P1 make move
first_move = Move(p1, [0,2])
board.add_move(first_move)
board.display()

second_move = Move(p2, [2,1])
board.add_move(second_move)
board.display()
