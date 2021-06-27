# pylint: disable=invalid-name, wrong-import-order, missing-module-docstring, unused-wildcard-import
# pylint: disable=missing-function-docstring, global-statement, multiple-statements
# pylint: disable=pointless-statement, trailing-whitespace, redefined-outer-name, wildcard-import

import blessed

term = blessed.Terminal()

print(term.home + term.clear, end = '', flush = True)

#print(term.move_xy(1, 2) + term.bold_red("h"), end = '')
#print(term.move_xy(2, 1) + term.bold_yellow("e"), end = '')
#print(term.move_xy(3, 0) + term.bold_green("l"), end = '')
#print(term.move_xy(4, 0) + term.bold_blue("l"), end = '')
#print(term.move_xy(5, 1) + term.bold_purple("o"), end = '')
#


with term.location(0, term.height - 1):
    print('Here is the bottom.', end = "")

print('This is back where I came from.', end = "")
print(term.move_y(term.height - 1), end = "")

#with term.location():
#    print(term.move_xy(1, 1) + 'Hi Mom!' + term.clear_eol)
