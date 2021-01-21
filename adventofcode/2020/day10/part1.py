#!/usr/bin/env python

def day_1(file) -> int:
    diff1 = diff3 = 0
    input_list = []
    with open(file, "r") as f:
        for line in f:
            line = line.strip("\n")
            input_list.append(int(line))

    input_list.sort()
    previous = 0
    for i in input_list:
        if i - previous == 1:
            diff1 += 1
        elif i - previous == 3:
            diff3 += 1
        previous = i

    return diff1 * (diff3 + 1)


if __name__ == '__main__':
    assert day_1("test_input.txt") == 220
    print(day_1("input.txt"))
