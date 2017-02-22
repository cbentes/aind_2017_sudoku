"""
----------------------------------------------------------------------------
                       Project: Solve a Sudoku with AI
----------------------------------------------------------------------------
- AI Nanodegree
- Student: Carlos Bentes
- Date: 23.02.2017
"""

from collections import defaultdict

assignments = []


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def naked_twins(values):
    """ Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers
    """
    # Twins should belong to the same group
    for group in unitlist:

        elements = set(group)

        # Map all naked values and boxes
        naked_boxes_map = defaultdict(list)
        for box in elements:
            v = values[box]
            if len(v) == 2:
                naked_boxes_map[v].append(box)

        # Keep only values that are in two boxes - double naked Twins
        twins = [v for v in naked_boxes_map if len(naked_boxes_map[v]) == 2]

        # Eliminate twin values from peers possibilities
        for twin in twins:
            twin_peers = elements - set(naked_boxes_map[twin])
            for peer in twin_peers:
                new_value = ''.join(sorted(set(values[peer]) - set(twin)))
                values = assign_value(values, peer, new_value)

    return values


def cross(A, B):
    """ Cross product of elements in A and elements in B
    """
    return [a + b for a in A for b in B]


def grid_values(grid):
    """ Convert grid into a dict of {square: char}
        with '123456789' for empties values.
    """
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))


def display(values):
    """ Display the values as a 2-D grid
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print()


def eliminate(values):
    """ Eliminate solved values from its peers
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            new_value = values[peer].replace(digit, '')
            values = assign_value(values, peer, new_value)
    return values


def only_choice(values):
    """ Applies the Only Choice strategy to reduce possible values in boxes
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                box = dplaces[0]
                values = assign_value(values, box, digit)
    return values


def reduce_puzzle(values):
    """ Iterate eliminate(), only_choice() and naked_twins(), and reduces the puzzle.
        - Returns False if something goes wrong (no possible values)
    """
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values):
    """ Using depth-first search and propagation
    """
    # Reduce Puzzle
    values = reduce_puzzle(values)

    # Check if reduction worked
    if values is False:
        return False

    # Check if the solution if complete
    if all(len(values[s]) == 1 for s in boxes):
        return values

    # If not complete, select unsolved box with
    # smaller number of options, and expand the search
    unsolved_boxes = [s for s in boxes if len(values[s]) > 1]
    n, s = min((len(values[s]), s) for s in unsolved_boxes)

    # DFS
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt


rows = 'ABCDEFGHI'
cols = '123456789'
boxes = cross(rows, cols)

# Traditional Mapping
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
# Diagonal Mapping
diagonal_units = [[a+b for (a,b) in zip(rows, cols)], [a+b for (a,b) in zip(rows, cols[::-1])]]

unitlist = row_units + column_units + square_units + diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)


def solve(grid):
    """ Solve Sudoku
    """
    # Transform input in a dictionary from: {box: possible_values}
    values = grid_values(grid)
    # Reduce all possible values into the puzzle solution using
    # Search and Constraint Propagation
    solution = search(values)
    return solution


if __name__ == '__main__':

    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))
    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
