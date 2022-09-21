import os.path
import csv
from Utility import *
from AC3 import *
from forward_checking_backtracking import *

def flatten(seqs):
	return sum(seqs, [])

easy1 = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
e = Sudoku(easy1)
e.display(e.infer_assignment())
QUIT = False
while (QUIT == False):
	print("""
	a.Backtracking + forward checking
	b.Arc Consistency
	""")
	ans = input("Select which algorithm to use (Enter letter of choice):")
	if (ans == "a"):
		AC3(e)
		print("----------------------AC3solved-------")
		e.display(e.infer_assignment())
	elif (ans == "b"):
		test_2 = Sudoku(easy1)
		print("----------------------Backtrackingsolved-------")
		backtracking_search(test_2, select_unassigned_variable=mrv, inference=forward_checking) 
		e.display(e.infer_assignment())
	else: 
		QUIT = True
		print("Not a Option Try again")
quit()
