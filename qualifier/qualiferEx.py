# pylint: disable=invalid-name, wrong-import-order, missing-module-docstring, unused-wildcard-import
# pylint: disable=missing-function-docstring, global-statement, multiple-statements, unused-argument, too-many-locals
# pylint: disable=pointless-statement, trailing-whitespace, redefined-outer-name, wildcard-import, line-too-long

from typing import Any, List, Optional, Literal

def make_table( rows: List[List[Any]], 
                title = Optional[str],
                labels: Optional[List[Any]] = None, 
                use_unicode: bool = False,
                use_double_lines: bool = False,
                alignment: Literal["left, center", "right"] = "left",
                centered: bool = False) -> str:
    pass

make_table(
   rows=[
       ["Ducky Yellow", 3],
       ["Ducky Dave", 12],
       ["Ducky Tube", 7],
       ["Ducky Lemon", 1]
   ],
   labels=["Name", "Duckiness"],
   centered=True
)
