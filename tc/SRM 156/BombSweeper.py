# -*- coding: utf-8 -*-
from __future__ import division
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class BombSweeper:
    def winPercentage(self, board):
        m = len(board)
        n = len(board[0])
        bomb = 'B'
        win = loss = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == bomb:
                    loss += 1
                    continue
                # horizontal
                h1 = h2 = False
                if j > 0:
                    h1 = board[i][j-1] == bomb
                if j < n - 1:
                    h2 = board[i][j+1] == bomb
                horizontal = h1 or h2
                # vertical
                v1 = v2 = False
                if i > 0:
                    v1 = board[i-1][j] == bomb
                if i < m - 1:
                    v2 = board[i+1][j] == bomb
                vertical   = v1 or v2
                # right diagonal
                r1 = r2 = False
                if i > 0 and j > 0:
                    r1 = board[i-1][j-1] == bomb
                if i < m - 1 and j < n - 1:
                    r2 = board[i+1][j+1] == bomb
                rdiag      = r1 or r2
                # left diagonal
                l1 = l2 = False
                if i < m - 1 and j > 0:
                    l1 = board[i+1][j-1] == bomb
                if i > 0 and j < n - 1:
                    l2 = board[i-1][j+1] == bomb
                ldiag      = l1 or l2
                if not(horizontal or vertical or rdiag or ldiag):
                    win += 1
        # print win, loss
        return win / (win + loss) * 100

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(board, __expected):
    startTime = time.time()
    instance = BombSweeper()
    exception = None
    try:
        __result = instance.winPercentage(board);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("BombSweeper (300 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("BombSweeper.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            board = []
            for i in range(0, int(f.readline())):
                board.append(f.readline().rstrip())
            board = tuple(board)
            f.readline()
            __answer = float(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(board, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1479684666
    PT, TT = (T / 60.0, 75.0)
    points = 300 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
