# pylint: disable=invalid-name, wrong-import-order, missing-module-docstring, unused-wildcard-import
# pylint: disable=missing-function-docstring, global-statement, multiple-statements, unused-argument, too-many-locals
# pylint: disable=pointless-statement, trailing-whitespace, redefined-outer-name, wildcard-import, line-too-long

from typing import Any, List, Optional
import math

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
    rowNo = len(rows)
    for i in range(colNo):    
        l = [str(x[i]) for x in rows]
        if labelPresent: l.append(str(labels[i]))
        lengths.append(len(max(l, key = len)))

    rowCorrected = [["" for column in row] for row in rows]
    # Fixes word spacing
    for i in range(rowNo):
        for j in range(colNo):
            word = str(rows[i][j])
            maxLen = lengths[j]
            wordLen = len(str(word))
            if centered:
                left = " " * (1 + math.floor((maxLen - wordLen) / 2))
                right = " " * (1 + math.ceil((maxLen - wordLen) / 2))
                rowCorrected[i][j] = left + word + right
            else: rowCorrected[i][j] = " " + word + " " * (maxLen - wordLen) + " "
    
    # Fixes spacing for labels
    if labelPresent: 
        labelCorrected = ["" for label in labels]
        labelNo = len(labels)
        for i in range(labelNo):
            word = str(labels[i])
            maxLen = lengths[i]
            wordLen = len(str(word))
            if centered:
                left = " " * (1 + math.floor((maxLen - wordLen) / 2))
                right = " " * (1 + math.ceil((maxLen - wordLen) / 2))
                labelCorrected[i] = left + word + right
            else: labelCorrected[i] = " " + word + " " * (maxLen - wordLen) + " "

    # Prints table
    lineList = lines(lengths)
    rowFormat = lambda x: "│" + "│".join(x) + "│"

    table = ""

    table += lineList[0] + "\n"
    if labelPresent:
        table += rowFormat(labelCorrected) + "\n"
        table += lineList[1] + "\n"
    for row in rowCorrected:
        table += rowFormat(row) + "\n"
    table += lineList[2]

    return table
