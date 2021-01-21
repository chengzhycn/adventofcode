#!/usr/bin/env python

def recursive(inp:list(), n:int) -> int:
    if n == 0 or n == 1:
        return 1
    if n == 2:
        if inp[2] - inp[0] <= 3:
            return 2
        else:
            return 1

    if inp[n] <= inp[n-3] + 3:
        return recursive(inp, n-1) + recursive(inp, n-2) + recursive(inp, n-3)
    elif inp[n] <= inp[n-2] + 3:
        return recursive(inp, n-1) + recursive(inp, n-2)
    else:
        return recursive(inp, n-1)


def day_2(file) -> int:
    input_list = [0]
    with open(file, "r") as f:
        for line in f:
            line = line.strip("\n")
            input_list.append(int(line))
    input_list.sort()

    # return recursive(input_list, len(input_list)-1)

    sum_list = [1, 1]
    if input_list[2] - input_list[0] <= 3:
        sum_list.append(2)
    else:
        sum_list.append(1)

    for i in range(3, len(input_list)):
        if input_list[i] <= input_list[i-3] + 3:
            sum_list.append(sum_list[i-3] + sum_list[i-2] + sum_list[i-1])
        elif input_list[i] <= input_list[i-2] + 3:
            sum_list.append(sum_list[i-2] + sum_list[i-1])
        else:
            sum_list.append(sum_list[i-1])

    return sum_list[-1]


if __name__ == '__main__':
    assert day_2("test_input.txt") == 19208
    print(day_2("input.txt"))
