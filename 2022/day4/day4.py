with open("data.txt", "r") as f:
    data = f.read().split("\n")

pairs = 0
overlaps = 0
for i in data:
    s1, s2 = i.split(",")
    s1_start, s1_end = map(int, s1.split("-"))
    s2_start, s2_end = map(int, s2.split("-"))

    # If s1 is in the range of s2 or vice versa
    if (s1_start <= s2_start and s1_end >= s2_end) or (
        s2_start <= s1_start and s2_end >= s1_end
    ):
        pairs += 1

    # If s1 and s1 overlaps each other
    if set(range(s1_start, s1_end + 1)) & set(range(s2_start, s2_end + 1)):
        overlaps += 1

print(pairs)  # Part 1
print(overlaps)  # Part 2
