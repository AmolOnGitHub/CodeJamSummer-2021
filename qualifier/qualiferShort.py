# pylint: disable=invalid-name, wrong-import-order, missing-module-docstring, unused-wildcard-import
# pylint: disable=missing-function-docstring, global-statement, multiple-statements, unused-argument, too-many-locals
# pylint: disable=pointless-statement, trailing-whitespace, redefined-outer-name, wildcard-import, line-too-long

def gR(t, m, w, c):
    if c: r = t.center(m, " ")
    else: r = t + " " * (m - w)
    return " " + r + " "

def ln(ls):
    tp = ls[0] + 2
    t = "┌" + tp * "─"
    s = "├" + tp * "─"
    b = "└" + tp * "─"
    for l in ls[1:]:
        l += 2
        t += "┬" + "─" * l
        s += "┼" + "─" * l
        b += "┴" + "─" * l
    return [t + "┐", s + "┤", b + "┘"]

def make_table(rs, lb, cnt = False):
    lP = True if lb is not None else False
    ls = []
    cn = len(rs[0])
    for i in range(cn):    
        l = [str(x[i]) for x in rs]
        if lP: l.append(str(lb[i]))
        ls.append(len(max(l, key = len)))
    lL = ln(ls)
    t = lL[0] + "\n"
    c = 0
    if lP:
        t += "│"
        for l in lb:
            t += gR(str(l), ls[c], len(str(l)), cnt) + "│"
            c += 1
        t += "\n" + lL[1] + "\n"
    for r in rs:
        c = 0
        t += "│"
        for cl in r:
            t += gR(str(cl), ls[c], len(str(cl)), cnt) + "│"
            c += 1
        t += "\n"
    t += lL[2]
    return t

table = make_table(
   rs=[
       ["Ducky Yellow", 3],
       ["Ducky Dave", 12],
       ["Ducky Tube", 7],
       ["Ducky Lemon", 1]
   ],
   lb=["Name", "Duckiness"],
   cnt=True
)
print(table)
