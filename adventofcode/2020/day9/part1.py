#!/usr/bin/env python

def main(file, data) -> int:
    result_list = []
    input_list = []
    with open(file, "r") as f:
        i = 0
        for line in f:
            line = line.strip("\n")
            num = int(line)
            if i > data:
                for j in range(i-data-1, i):
                    if num in result_list[j]:
                        break
                else:
                    return num

            input_list.append(num)
            result_list.append([])
            for j in range(0, i):
                result_list[j].append(input_list[j] + input_list[i])
            i += 1


if __name__ == '__main__':
    assert main("test_input.txt", 5) == 127
    print(main("input.txt", 25))
