# SAT Solver Based Sudoku Solver  

This project implements a **Sudoku Solver** using **Boolean Satisfiability (SAT)**.  
Instead of using traditional backtracking or constraint programming, this solver encodes Sudoku rules into **CNF (Conjunctive Normal Form) clauses** and solves them using a SAT solver (`python-sat`).  

## ✨ Features  
- Encodes Sudoku rules (row, column, subgrid, and uniqueness constraints) into SAT clauses.  
- Works with **any valid Sudoku puzzle** (9×9).  
- Uses the **PySAT** library for efficient SAT solving.  
- Outputs the solved Sudoku grid in a clean format.  

## 🧩 Motivation  
The idea for this project came from the **LeetCode Sudoku Solver** problem:  
👉 [LeetCode – Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)  

While LeetCode’s problem encourages a backtracking-based solution, this project demonstrates how SAT solvers can be applied to the same problem in a more general and elegant way.  

## ⚙️ Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/prashantdlp/sat-sudoku-solver.git
   cd sat-sudoku-solver
2. Create and activate a virtual environment (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Linux/macOS
    venv\Scripts\activate      # On Windows
3. Install dependencies:
    ```bash 
    pip install python-sat[pblib]

##▶️ Usage

Run the tester :
    ```bash
    python tester.py 

Here, Our **tester.py** randomly makes 500 sudoku and solves them (if they are valid Sudoku). 
Of course, you can tweak this code and solve any sudoku which u want.      
