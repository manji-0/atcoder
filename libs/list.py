def goright(v, i, S):
    for idx in range(i, len(S)):
        if S[idx] == v:
            return idx

    return -1

def goleft(v, i, S):
    for idx in range(i, 0, -1):
        if S[idx] == v:
            return idx

    return -1

from operator import add

def cumulative(L, op=add, start=0):
    Res = [start]

    for l in L:
        Res.append(op(Res[-1], l))

    return Res[1:]
