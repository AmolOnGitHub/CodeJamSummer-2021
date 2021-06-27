# pylint: disable=invalid-name, wrong-import-order, missing-module-docstring, unused-wildcard-import
# pylint: disable=missing-function-docstring, global-statement, multiple-statements, unused-argument, too-many-locals
# pylint: disable=pointless-statement, trailing-whitespace, redefined-outer-name, wildcard-import, line-too-long

from typing import Any, Optional

def getRow(text, maxLen, wordLen, centered):
    if centered:
        rowText = text.center(maxLen, " ")
    else:
        rowText = text + " " * (maxLen - wordLen)
    return " " + rowText + " "

def lines(lengths):
    temp = lengths[0] + 2
    top = "┌" + temp * "─"
    sep = "├" + temp * "─"
    bot = "└" + temp * "─"

    for length in lengths[1:]:
        length += 2
        top += "┬" + "─" * length 
        sep += "┼" + "─" * length 
        bot += "┴" + "─" * length 

    top += "┐"
    sep += "┤"
    bot += "┘"

    return [top, sep, bot]

def make_table(rows: list[list[Any]], labels: Optional[list[Any]] = None, centered: bool = False) -> str:
    labelPresent = True if labels is not None else False
    
    # Finds out the length of longest string in each column 
    lengths = []
    colNo = len(rows[0])
    for i in range(colNo):    
        l = [str(x[i]) for x in rows]
        if labelPresent: l.append(str(labels[i]))
        lengths.append(len(max(l, key = len)))

    # Makes formats
    lineList = lines(lengths)

    # Starts making table
    table = lineList[0] + "\n"

    # Makes labels
    counter = 0
    if labelPresent:
        table += "│"
        for label in labels:
            label = str(label)
            maxLen = lengths[counter]
            wordLen = len(label)
            table += getRow(label, maxLen, wordLen, centered) + "│"
            counter += 1
        table += "\n" + lineList[1] + "\n"

    # Makes rows
    for row in rows:
        counter = 0
        table += "│"
        for col in row:
            col = str(col)
            maxLen = lengths[counter]
            wordLen = len(col)
            table += getRow(col, maxLen, wordLen, centered) + "│"
            counter += 1
        table += "\n"

    table += lineList[2]   

    return table

table = make_table(
   rows=[
       ["Ducky Yellow", 3],
       ["Ducky Dave", 12],
       ["Ducky Tube", 7],
       ["Ducky Lemon", 1]
   ],
   labels=["Name", "Duckiness"],
   centered=True
)
print(table)
