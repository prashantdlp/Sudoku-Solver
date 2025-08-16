"""
sudoku_solver.py

Implement the function solve_sudoku(grid: List[List[int]]) -> List[List[int]] using a SAT solver from PySAT.
"""

from pysat.formula import CNF
from pysat.solvers import Solver
from typing import List

rows = 9
cols = 9
row_matrix = 3
col_matrix = 3

def id(i, j, val):
   return (val)*1 + (j)*9 + (i)*81

def encode(cnf):
    for row in range(rows):
        for col in range(cols):
            cnf.append([id(row, col, v) for v in range(1, 10)])
            for v1 in range(1, 10):
                for v2 in range(v1 + 1, 10):
                    cnf.append([-id(row, col, v1), -id(row, col, v2)])

def encode_row(cnf):
    for row in range(rows):
        for v in range(1, 10):
            cnf.append([id(row, col, v) for col in range(cols)])

def encode_col(cnf):
    for col in range(cols):
        for v in range(1, 10):
            cnf.append([id(row, col, v) for row in range(rows)])

def block_encode(cnf):
    for m in range(row_matrix):
        for n in range(col_matrix):
            for v in range(1,10) :
                cnf.append([id(3*m+i, 3*n+j, v) for i in range(3) for j in range(3)])

def solve_sudoku(grid: List[List[int]]) -> List[List[int]]:
    """Solves a Sudoku puzzle using a SAT solver. Input is a 2D grid with 0s for blanks."""

    # TODO: implement encoding and solving using PySAT
    cnf = CNF()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0:  
                v = grid[i][j]
                cnf.append([id(i, j, v)])


    encode(cnf)
    encode_col(cnf)
    encode_row(cnf)
    block_encode(cnf)

    with Solver(name='glucose3') as solver:
        solver.append_formula(cnf.clauses)
        if solver.solve():
            model = solver.get_model()
            print("SAT solution:", model)
        else: 
            print("UNSAT")
            return []
          

    ans = [[0] * 9 for _ in range(9)]

    for r in range(rows):
        for c in range(cols):
            for v in range(1, 10):
                if id(r, c, v) in model:
                    ans[r][c] = v

    return ans