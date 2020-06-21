//Python Average Function


def avg(*args):
    length=len(args)
    average=0
    for arg in args:
        average+=arg
    total=float(average)/length
    return total
