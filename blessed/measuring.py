# pylint: disable=invalid-name, wrong-import-order, missing-module-docstring, unused-wildcard-import
# pylint: disable=missing-function-docstring, global-statement, multiple-statements
# pylint: disable=pointless-statement, trailing-whitespace, redefined-outer-name, wildcard-import

import blessed

term = blessed.Terminal()

print(term.home + term.clear, end = "")

poem = (term.bold_cyan('Plan difficult tasks'),
        term.cyan('through the simplest tasks'),
        term.bold_cyan('Achieve large tasks'),
        term.cyan('through the smallest tasks'))

for line in poem:
    print('\n'.join(term.wrap(line, width=25, subsequent_indent=' ' * 4)))