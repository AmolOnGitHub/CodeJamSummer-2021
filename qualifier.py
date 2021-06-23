# pylint: disable=invalid-name, wrong-import-order, missing-module-docstring, unused-wildcard-import
# pylint: disable=missing-function-docstring, global-statement, multiple-statements, unused-argument, too-many-locals
# pylint: disable=pointless-statement, trailing-whitespace, redefined-outer-name, wildcard-import, line-too-long

from typing import Any, List, Optional
import math

def getRow(text, maxLen, wordLen, centered):
    if centered:
        left = " " * (1 + math.floor((maxLen - wordLen) / 2))
        right = " " * (1 + math.ceil((maxLen - wordLen) / 2))
        rowText = left + text + right
    else:
        rowText = " " + text + " " * (maxLen - wordLen) + " "
    return rowText

def lines(lengths):
    top = "┌"
    sep = "├"
    bot = "└"
    for length in lengths:
        length += 2
        top += "─" * length + "┬"
        sep += "─" * length + "┼"
        bot += "─" * length + "┴"

    top = top[:-1] + "┐"
    sep = sep[:-1] + "┤"
    bot = bot[:-1] + "┘"

    return [top, sep, bot]

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
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
    rowFormat = lambda x: "│" + "│".join(x) + "│"

    # Starts making table
    table = lineList[0] + "\n"

    # Makes labels
    counter = 0
    if labelPresent:
        labelWords = []
        for label in labels:
            label = str(label)
            maxLen = lengths[counter]
            wordLen = len(label)
            labelWords.append(getRow(label, maxLen, wordLen, centered))
            counter += 1
        table += rowFormat(labelWords) + "\n"
        table += lineList[1] + "\n"

    # Makes rows
    for row in rows:
        counter = 0
        rowWords = []
        for col in row:
            col = str(col)
            maxLen = lengths[counter]
            wordLen = len(col)
            rowWords.append(getRow(col, maxLen, wordLen, centered))
            counter += 1
        table += rowFormat(rowWords) + "\n"

    table += lineList[2]   

    return table
    