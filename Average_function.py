//Python Average Function
// This program is written by Nirbhay Kaushik


def avg(*args):
    length=len(args)
    average=0
    for arg in args:
        average+=arg
    total=float(average)/length
    return total
