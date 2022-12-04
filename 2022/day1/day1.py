with open("data.txt") as f:
    data = f.read().split("\n")
    calories = list()
    sum_calories = 0

    for i in data:
        if i == "":
            calories.append(sum_calories)
            sum_calories = 0

        else:
            sum_calories += int(i)

    calories.sort()

print(calories[-1])  # Problem 1
print(sum(calories[-3:]))  # Problem 2
