from pathlib import Path
import re

DATA = Path.cwd().joinpath("day3","input.txt")

def solve_1(data):
    total = 0
    mul_pattern = re.compile(r"(mul[(][0-9]{1,9}[,][0-9]{1,9}[)])")
    muls = mul_pattern.findall(data)
    for mul in muls:
        value_pattern = re.compile(r"[0-9]{1,9}")
        values = list(map(int, value_pattern.findall(mul)))
        total += values[0]*values[1]
    return total


if __name__ == "__main__":
    with open(DATA) as fp:
        data: str = fp.read().strip()
    
    total1 = solve_1(data)
    print(total1)

...