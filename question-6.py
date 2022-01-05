def sum():
    above = list(range(1,101))
    under = list(range(200, -2, -2))

    result = 0
    for i in range(0, 101):
        if under[i] != 0:
            result = (above[i] / under[i]) + result

    print(result)

sum()