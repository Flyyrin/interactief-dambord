dict = {}
for i in range(64):
    if 24 < i < 64-24:
        dict[str(i)] = "e"
    elif i < 24:
        if (i % 2) == 0:
            dict[str(i)] = "e"
        else:
            dict[str(i)] = 1
    elif i > 64-24:
        if (i % 2) == 0:
            dict[str(i)] = "e"
        else:
            dict[str(i)] = 2

print(dict)