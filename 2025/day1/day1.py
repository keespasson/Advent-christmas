from pathlib import Path

DATA = Path.cwd().joinpath("2025/day1","input.txt")

def part1(data: str) -> int:
    data = data.split("\n")

    directions = []
    distances = []
    for line in data:
        directions.append(line[0])
        distances.append(line[1:])


    point = 50
    password = 0

    for index, distance in enumerate(distances):
        if directions[index] == "R":
            point += int(distance)
        else:
            point -= int(distance)

        if point > 99:
            while True:
                point -= 100
                if point < 99:
                    break
        elif point < 0:
            while True:
                point += 100
                if point >= 0:
                    break

        if point == 0:
            password += 1

    return password


def part2(data: str) -> int:
    data = data.split("\n")

    directions = []
    distances = []
    for line in data:
        directions.append(line[0])
        distances.append(line[1:])

    point = 50
    password = 0

    for index, distance in enumerate(distances):
        if directions[index] == "R":
            point += int(distance)
        else:
            point -= int(distance)

        if point > 99:
            while True:
                point -= 100
                password += 1
                if point < 99:
                    break
        elif point < 0:
            while True:
                point += 100
                password += 1
                if point >= 0:
                    break

        if point == 0:
            password += 1


    return password

if __name__ == "__main__":
    with open(DATA) as fp:
            data: str = fp.read().strip()

    # part1(data)
    part2(data)
    ...