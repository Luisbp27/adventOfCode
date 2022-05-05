import csv


def __main__():
    forward = 0
    depth = 0

    with open("commands.txt", "r", encoding="utf-8") as f:
        commands = list(csv.reader(f, delimiter=' '))

    part1(forward, depth, commands)
    part2(forward, depth, commands)

def part1(forward, depth, commands):
    for i in range(len(commands)):
        if commands[i][0] == "up":
            depth -= int(commands[i][1])
        elif commands[i][0] == "down":
            depth += int(commands[i][1])
        elif commands[i][0] == "forward":
            forward += int(commands[i][1])

    print(depth * forward)

def part2(forward, depth, commands):
    aim = 0

    for i in range(len(commands)):
        if commands[i][0] == "up":
            aim -= int(commands[i][1])
        elif commands[i][0] == "down":
            aim += int(commands[i][1])
        elif commands[i][0] == "forward":
            forward += int(commands[i][1])
            depth += aim * int(commands[i][1])
    
    print(depth * forward) 


if __name__ == '__main__':
    __main__()
