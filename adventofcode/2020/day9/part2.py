#!/usr/bin/env python


def day_2(file, invalid) -> int:
    sum_list = []
    input_list = []
    with open(file, "r") as f:
        i = 0
        for line in f:
            line = line.strip("\n")
            num = int(line)
            input_list.append(num)
            for j in range(len(sum_list)):
                sum_list[j] += num
                if sum_list[j] == invalid:
                    return min(input_list[j:i+1]) + max(input_list[j:i+1])
            sum_list.append(num)
            i += 1

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
    assert day_2("test_input.txt", main("test_input.txt", 5)) == 62
    invalid = main("input.txt", 25)
    print(day_2("input.txt", invalid))
