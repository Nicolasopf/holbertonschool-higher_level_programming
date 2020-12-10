#!/usr/bin/python3


if __name__ == "__main__":
    from sys import argv
    h = 0
    leen = len(argv)
    if leen == 2:
        print("1 argument:\n{:d}: {:s}".format(leen-1, argv[1]))
    elif leen > 2:
        args = argv[1:]
        print(leen-1, "arguments:")
        for i in argv:
            if i != argv[0]:
                print("{:d}: {:s}".format(h, i))
            h += 1
    else:
        print("0 arguments.")
