#!/usr/bin/python3

for idx in range(0, 100):
    if idx < 99:
        sep = ", "
        end = ""
    else:
        sep = ""
        end = "\n"
    print("{:02d}{}".format(idx, sep), end=end)
