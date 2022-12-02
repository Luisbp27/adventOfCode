import csv
import numpy as np


def __main__():
    """" Main function """

    with open("data.txt", "r", encoding="utf-8") as f:
        data = list(csv.reader(f, delimiter='\t'))

    data = [int(data[i][0]) for i in range(len(data))]
    counter = 0

    print(part1(data, counter))
    print(part2(data, counter))


def part1(data, counter):
    for i in range(len(data)):
        if data[i] > data[i-1]:
            counter += 1

    return counter


def part2(data, counter):
    j = 0
    i = 0
    sum_group = []

    while i < (len(data) - 3):
        sum_group.append(data[i] + data[i+1] + data[i+2])
        i += 3
        j += 1
    return part1(sum_group, counter)


if __name__ == '__main__':
    __main__()
