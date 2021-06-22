# pylint: disable=invalid-name, wrong-import-order, missing-module-docstring, unused-wildcard-import
# pylint: disable=missing-function-docstring, global-statement, multiple-statements, unused-argument
# pylint: disable=pointless-statement, trailing-whitespace, redefined-outer-name, wildcard-import, line-too-long

from typing import Any, List, Optional

def draw_table(rows = 1, columns = 1, text = " ", labelPresent: bool = False):
    spaces = "─" * len(text)
    top = "┌" + spaces + (("┬" + spaces) * (columns - 1)) + "┐"
    sep = "├" + spaces + (("┼" + spaces) * (columns - 1)) + "┤"
    bot = "└" + spaces + (("┴" + spaces) * (columns - 1)) + "┘"

    row = lambda x: (("│" + x) * (columns)) + "│"

    print(top)
    if labelPresent:
        print(row("label"))
        print(sep)
    for _ in range(rows):
        print(row(text))
    print(bot)
    

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    
    return 0

table = make_table(
   rows=[
       ["Ducky Yellow", 3],
       ["Ducky Dave", 12],
       ["Ducky Tube", 7],
       ["Ducky Lemon", 1]
   ],
   centered=True
)

draw_table(rows = 2, columns = 6, labelPresent = True, text = "text ")
