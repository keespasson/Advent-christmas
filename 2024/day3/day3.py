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

def solve_2(data):
    total2 = 0
    do_till_dont = re.compile(r"(do[()](?!n't[()]).*don't[()])")
    do_donts = do_till_dont.findall(data)
    for do_dont in do_donts:
        mul_pattern = re.compile(r"(mul[(][0-9]{1,9}[,][0-9]{1,9}[)])")
        muls = mul_pattern.findall(do_dont)
        for mul in muls:
            value_pattern = re.compile(r"[0-9]{1,9}")
            values = list(map(int, value_pattern.findall(mul)))
            total2 += values[0]*values[1]
    
    till_do = data.split("do()")
    muls = mul_pattern.findall(till_do[0])
    mul_pattern = re.compile(r"(mul[(][0-9]{1,9}[,][0-9]{1,9}[)])")
    muls = mul_pattern.findall(do_dont)
    for mul in muls:
        value_pattern = re.compile(r"[0-9]{1,9}")
        values = list(map(int, value_pattern.findall(mul)))
        total2 += values[0]*values[1]

    return total2

if __name__ == "__main__":
    with open(DATA) as fp:
        data: str = fp.read().strip()
    
    total1 = solve_1(data)

    total2 = solve_2(data)
    print(total1)
    print(total2)

...