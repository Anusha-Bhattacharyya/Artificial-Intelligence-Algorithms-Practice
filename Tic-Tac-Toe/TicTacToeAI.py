import os.path
import csv
import math
class Tic_Tac_Toe:
#initialize
	def __init__(self):
		self.board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

		self.printboard()
		self.Human = 'X'
		self.Comp = 'O'

		while not self.game_over():
			self.human_turn()
			self.ai_turn(self.board)

#print/writing
	def printboard(self):
		print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
		print('-----')
		print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
		print('-----')
		print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
		print("\n")

	def write_turn(self, turn, position):
		if self.check_blank(position):
			self.board[position] = turn
			self.printboard()
			if self.game_over():
				if turn == 'X':
					print("Human is the winner!")
					exit()
				else:
					print("Computer is the winner!")
					exit()
			if self.checkDraw():
				print("Draw!")
				exit()
			return
			
		else:
			print("Not a possible move")
			print("\n")
			position = int(input("Please enter new position:  "))
			self.write_turn(turn, position)
			return


#board checks
	def check_blank(self, position):
		if self.board[position] == ' ':
			return True
		else:
			return False
			
	def game_over(self):
		#horizontal
		if self.board[1] == self.board[2] == self.board[3] != ' ':
			return True
		elif self.board[4] == self.board[5] == self.board[6] != ' ':
			return True
		elif self.board[7] == self.board[8] == self.board[9] != ' ':
			return True
		#vertical
		elif self.board[1] == self.board[4] == self.board[7] != ' ':
			return True
		elif self.board[2] == self.board[5] == self.board[8] != ' ':
			return True
		elif self.board[3] == self.board[6] == self.board[9] != ' ':
			return True
		#diagonal
		elif self.board[1] == self.board[5] == self.board[9] != ' ':
			return True
		elif self.board[7] == self.board[5] == self.board[3] != ' ':
			return True
		else:
			return False
			
	def checkDraw(self):
		for key in self.board.keys():
			if (self.board[key] == ' '):
				return False
		return True

	def WhoWon(self, turn):
		#horizontal
		if self.board[1] == self.board[2] == self.board[3] == turn:
			return True 
		elif self.board[4] == self.board[5] == self.board[6] == turn:
			return True
		elif self.board[7] == self.board[8] == self.board[9] == turn:
			return True
		#vertical
		elif self.board[1] == self.board[4] == self.board[7] == turn:
			return True
		elif self.board[2] == self.board[5] == self.board[8] == turn:
			return True
		elif self.board[3] == self.board[6] == self.board[9] == turn:
			return True
		#diagonal
		elif self.board[1] == self.board[5] == self.board[9] == turn:
			return True
		elif self.board[7] == self.board[5] == self.board[3] == turn:
			return True
		else:
			return False


#Turns
	def human_turn(self):
		position = int(input("Use numpad (1..9):"))
		self.write_turn(self.Human, position)
		return


	def ai_turn(self, state):
		best = -1
		bestMove = 0
		for key in state.keys():
			if (state[key] == ' '):
				state[key] = self.Comp
				score = self.minimax(state, 0, False)
				state[key] = ' '
				if (score > best):
					best = score
					bestMove = key

		self.write_turn(self.Comp, bestMove)
		return

#Minimax/AlphaBetaPruning
	def minimax(self, state, depth, AI, alpha = -math.inf , beta = math.inf):
		if (self.WhoWon(self.Comp)):
			return 1
		elif (self.WhoWon(self.Human)):
			return -1
		elif (self.checkDraw()):
			return 0
		if self.game_over() or depth == 9:
			score = self.evaluate(state)
		if (AI):
			best = -math.inf
			for key in state.keys():
				if (state[key] == ' '):
					state[key] = self.Comp
					score = self.minimax(state, depth + 1, False, alpha, beta) 
					state[key] = ' '
					best = max(score, best)
					alpha = max(alpha, score)
					if (beta >= alpha):
						pass
			return best
		else:
			best = math.inf
			for key in state.keys():
				if (state[key] == ' '):
					state[key] = self.Human
					score = self.minimax(state, depth + 1, True, alpha, beta)
					state[key] = ' '
					best = min(score, best)
					beta = min(beta, score)
					if (alpha >= beta):
						pass 
			return best