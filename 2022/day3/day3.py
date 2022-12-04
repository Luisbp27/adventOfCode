with open("data.txt", "r") as f:
    rucksacks = [line.replace("\n", "") for line in f.readlines()]


def get_priority(item):
    if "a" <= item <= "z":
        priority = ord(item) - ord("a") + 1
    else:
        priority = ord(item) - ord("A") + 1 + 26

    return priority


# Part 1
total = 0
for i in rucksacks:
    middle = len(i) // 2
    compartment1 = i[:middle]
    compartment2 = i[middle:]

    shared_item = [item for item in compartment2 if item in compartment1][0]

    total += get_priority(shared_item)

print(total)

# Part 2
total = 0
for i in range(0, len(rucksacks), 3):
    group = rucksacks[i : i + 3]

    shared_item = [item for item in group[0] if item in group[1] and item in group[2]][0]

    total += get_priority(shared_item)

print(total)
