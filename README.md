# Artificial Intelligence Nanodegree

### Introductory Project: Diagonal Sudoku Solver



# Question 1 (Naked Twins)
---

Q: How do we use constraint propagation to solve the naked twins problem?
  
A: The naked twin is solved by enforcing that no other peer box contains values from the twins boxes. This elimination reduces the number of possible values in the unsolved boxes.

# Question 2 (Diagonal Sudoku)
---

Q: How do we use constraint propagation to solve the diagonal sudoku problem?  

A: The diagonal sudoku is solved by adding boxes from the diagonal as a unit in the units list. This addition changes the number of peer-boxes for boxes belonging in the diagonal (or the inverse diagonal). A box in the diagonal will, therefore, have a total of 26 peers, while boxes off-diagonal will continue to have 20 peers. The constraint propagation considers the units list to reduce the number of possible values of every unsolved box (reduction process at reduce_puzzle function).



# References
---

1. Project Specifications:

https://review.udacity.com/#!/rubrics/689/view

2. Sudoku Strategies

http://www.sudokudragon.com/sudokustrategy.htm

3. Udacity Repository:

https://github.com/udacity/aind-sudoku

4. Peter Norvig Blog: http://norvig.com/sudoku.html



### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.


##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
