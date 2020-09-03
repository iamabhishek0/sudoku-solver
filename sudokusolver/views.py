import copy

from django.shortcuts import render

from .utils import SudokuGenerator


def index(request):
    grid = SudokuGenerator()
    solved = copy.deepcopy(grid.create_solved_grid())
    unsolved = grid.create_unsolved_grid()

    return render(request, 'sudoku-board.html', {'unsolved': unsolved, 'solved': solved})
