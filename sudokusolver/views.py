import copy
import json

from django.http import JsonResponse
from django.shortcuts import render

from .utils import SudokuGenerator, isValidConfig


def index(request):
    grid = SudokuGenerator()
    solved = copy.deepcopy(grid.create_solved_grid())
    unsolved = grid.create_unsolved_grid()

    return render(request, 'sudoku-board.html', {'unsolved': unsolved, 'solved': solved})

def custom(request):

    if(request.method=="POST"):
        body_unicode = request.body.decode('utf-8')
        json_data = json.loads(body_unicode)
        grid, row = [], []
        cnt = 1
        for x in json_data:
            row.append(x['value'])
            cnt = cnt + 1
            if cnt == 10:
                grid.append(row)
                row = []
                cnt = 1

        if isValidConfig(grid):
            sudoku_grid = copy.deepcopy(SudokuGenerator(grid).grid)
            response_data = {}
            response_data['sudoku_grid'] = sudoku_grid
            response_data['valid'] = True
            return JsonResponse(data=response_data, status=200)

        else:
            response_data = {}
            response_data['sudoku_grid'] = grid
            response_data['valid'] = False
            return JsonResponse(data=response_data, status=200)
    else:
        sudoku_grid = [[0 for i in range(9)] for j in range(9)]
        return render(request, 'custom-sudoku-board.html', {'sudoku_grid': sudoku_grid, 'valid':True})
