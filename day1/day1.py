import csv
import numpy as np


def __main__():
    with open("data.txt", "r", encoding="utf-8") as f:
        data = list(csv.reader(f, delimiter='\t'))

    data = np.array(data).astype(int)
    counter = 0

    print(part1(data, counter))
    print(part2(data, counter))


def part1(data, counter):
    for i in range(len(data)):
        if data[i] > data[i-1]:
            counter += 1
    return counter


def part2(data, counter):
    pass

if __name__ == '__main__':
    __main__()
