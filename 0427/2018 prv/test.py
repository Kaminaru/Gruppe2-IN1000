fil = open("test.txt", "r")
linje = fil.readline().strip()
while linje != "":
    linjeTo = fil.readline().strip()
    print(f"{linje} ----- {linjeTo}")
    linje = fil.readline().strip()
    print(linje)

print("Her")