# pylint: disable=invalid-name, wrong-import-order, missing-module-docstring, unused-wildcard-import
# pylint: disable=missing-function-docstring, global-statement, multiple-statements
# pylint: disable=pointless-statement, trailing-whitespace, redefined-outer-name, wildcard-import

import blessed

term = blessed.Terminal()
term.green_reverse('ALL SYSTEMS GO')
print(term.white_on_firebrick3('SYSTEM OFFLINE'))
print(f"{term.yellow}Yellow is brown, {term.bright_yellow}"
          f"Bright yellow is actually yellow!{term.normal}")
print(term.blink("Insert System disk into drive A:"))       # Creates blinking text
print(term.underline_bold_green_on_yellow('They live! In sewers!'))

print(term.home + term.clear, end = "")
print(term.underline_bold_red_on_navy("test"))

if term.does_styling:
    with term.location(x=0, y=term.height - 1):
        print('Progress: [=======>   ]')
print(term.bold("60%"))

print(term.move_y(term.height - 1), end = "")
