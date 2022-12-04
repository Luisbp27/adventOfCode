# Oponent: A = Rock, B = Paper, C = Scissors
# Me: X = Rock, Y= Paper, Z = Scissors
# Points: 1 Rock, 2 Paper, 3 Scissors + 0 Loose, 3 Draw, 6 Win

with open("data.txt", "r") as f:
    data = f.read()

shapes = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

turns = [[shapes[i] for i in turn.split(" ")] for turn in data.split("\n")]

# Part 1
total = 0
for i in turns:
    me = i[1]
    oponent = i[0]

    # Win
    if (
        (me == 1 and oponent == 3)
        or (me == 2 and oponent == 1)
        or (me == 3 and oponent == 2)
    ):
        total += 6

    # Draw
    elif me == oponent:
        total += 3

    total += me

print(total)

# Part 2
win = {1: 2, 2: 3, 3: 1}
draw = {1: 1, 2: 2, 3: 3}
loose = {1: 3, 2: 1, 3: 2}

total = 0
for i in turns:
    oponent = i[0]
    end = i[1]

    # Me win
    if end == 3:
        total += win[oponent]
        total += 6

    # Me draw
    if end == 2:
        total += draw[oponent]
        total += 3

    # Me loose
    if end == 1:
        total += loose[oponent]

print(total)
