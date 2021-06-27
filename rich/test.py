# pylint: disable=invalid-name, wrong-import-order, missing-module-docstring, unused-wildcard-import
# pylint: disable=missing-function-docstring, global-statement, multiple-statements, unused-import
# pylint: disable=pointless-statement, trailing-whitespace, redefined-outer-name, wildcard-import

from rich.console import Console
import rich

console = Console()
console.print([1, 2, 3])
console.print("[blue underline]Looks like a link")

console.print("FOO", style="white on blue")

style = "bold red"
console.rule("[bold red]Chapter 2", style=style)
style = "blue"
console.print("once there was ", style = style, justify="center")

console = Console(width=14)
supercali = "supercalifragilisticexpialidocious"

overflow_methods = ["fold", "crop", "ellipsis"]
for overflow in overflow_methods:
    console.rule(overflow)
    console.print(supercali, overflow=overflow, style="bold blue")
    console.print()
    