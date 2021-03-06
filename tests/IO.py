def INPUT_SOLVER():
    """Return list of Sudoku boards for Solver class tests ./src/solver.py/Solver:class"""
    return {
        "nextpos": {
            "board": [
                [1, 5, 0, 0, 0, 0, 0, 0, 3],
                [0, 0, 0, 0, 0, 6, 4, 2, 0],
                [0, 8, 4, 5, 0, 0, 7, 9, 0],
                [0, 0, 0, 3, 0, 0, 0, 0, 7],
                [5, 0, 3, 2, 8, 7, 9, 0, 4],
                [7, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 9, 7, 0, 0, 2, 3, 5, 0],
                [0, 3, 5, 1, 0, 0, 0, 0, 0],
                [8, 0, 0, 0, 0, 0, 0, 7, 0],
            ]
        },
        "exists": {
            "board": [
                [0, 5, 0, 0, 0, 0, 0, 0, 3],
                [0, 0, 0, 0, 0, 6, 4, 2, 0],
                [0, 8, 4, 5, 0, 0, 7, 9, 0],
                [0, 0, 0, 3, 0, 0, 0, 0, 7],
                [5, 0, 3, 2, 8, 7, 9, 0, 4],
                [7, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 9, 7, 0, 0, 2, 3, 5, 0],
                [0, 3, 5, 1, 0, 0, 0, 0, 0],
                [8, 0, 0, 0, 0, 0, 0, 7, 0],
            ],
            "success": {"n": 2, "rc": (0, 2)},
            "row0": {"n": 3, "rc": (0, 2)},
            "column0": {"n": 4, "rc": (0, 2)},
            "3*3area0": {"n": 8, "rc": (0, 2)},
        },
        "solve": [
            [0, 5, 0, 0, 0, 0, 0, 0, 3],
            [0, 0, 0, 0, 0, 6, 4, 2, 0],
            [0, 8, 4, 5, 0, 0, 7, 9, 0],
            [0, 0, 0, 3, 0, 0, 0, 0, 7],
            [5, 0, 3, 2, 8, 7, 9, 0, 4],
            [7, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 9, 7, 0, 0, 2, 3, 5, 0],
            [0, 3, 5, 1, 0, 0, 0, 0, 0],
            [8, 0, 0, 0, 0, 0, 0, 7, 0],
        ],
    }


def OUTPUT_SOLVER():
    """Return list of solved Sudoku boards for Solver class tests ./src/solver.py/Solver:class"""
    return {
        "nextpos": (0, 2),
        "exists": {
            "success": (),
            "row0": (0, 8),
            "column0": (2, 2),
            "3*3area0": (2, 1),
        },
        "solve": [
            [9, 5, 6, 7, 2, 4, 1, 8, 3],
            [3, 7, 1, 8, 9, 6, 4, 2, 5],
            [2, 8, 4, 5, 1, 3, 7, 9, 6],
            [4, 2, 8, 3, 6, 9, 5, 1, 7],
            [5, 1, 3, 2, 8, 7, 9, 6, 4],
            [7, 6, 9, 4, 5, 1, 8, 3, 2],
            [1, 9, 7, 6, 4, 2, 3, 5, 8],
            [6, 3, 5, 1, 7, 8, 2, 4, 9],
            [8, 4, 2, 9, 3, 5, 6, 7, 1],
        ],
    }
