line = input().split()
size, number, angle = [int(e) for e in line[:-1]]
hp = float(line[-1])

print(
    size,
    number,
    angle,
    hp,
)
blade = Blade(
    size=size,
    number=number,
    angle=angle,
    hp=hp,
)
blade.printInfo()