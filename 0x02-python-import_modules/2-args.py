#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    h = 0
    leen = len(sys.argv)
    if leen >= 2:
        args = sys.argv[1:]
        print(leen-1, "arguments:")
        for i in sys.argv:
            if i != sys.argv[0]:
                print("{:d}: {:s}".format(h, i))
            h += 1
    else:
        print("0 arguments.")
