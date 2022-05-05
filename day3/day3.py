
def __main__():
    with open("report.txt", "r", encoding="utf-8") as f:
        reports = f.readlines()

    gamma = []
    epsilon = []

    for i in range(len(reports[0]) - 1):
        counter_1 = 0
        counter_0 = 0
        for j in range(len(reports)):
            if int(reports[j][i]) == 1:
                counter_1 += 1
            else:
                counter_0 += 1
        if counter_1 > counter_0:
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)

    gamma_dec = int("".join(str(x) for x in gamma), 2)
    epsilon_dec = int("".join(str(x) for x in epsilon), 2)
    print(gamma_dec * epsilon_dec)


if __name__ == '__main__':
    __main__()