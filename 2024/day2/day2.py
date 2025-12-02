from pathlib import Path

DATA = Path.cwd().joinpath("day2","input.txt")

# def solvepart1(data):
#     total = 0
#     last_val = None

#     for line in data.split("\n"):
#         values = list(map(int,line.split()))
#         for i, value in enumerate(values):
#             if i == 0:
#                 last_val = value
#                 continue
#             if last_val < value and 3 >= abs(last_val-value) >= 1:
#                 if i == len(values)-1:
#                     total = total + 1
#                     break
#                 else: 
#                     last_val = value
#             else:
#                 break


#     for line in data.split("\n"):
#         values = list(map(int,line.split()))
#         for i, value in enumerate(values):
#             if i == 0:
#                 last_val = value
#                 continue
#             if last_val > value and 3 >= abs(last_val-value) >= 1:
#                 if i == len(values)-1:
#                     total = total + 1
#                     break
#                 else:
#                     last_val = value
#             else:
#                 break
#     return total

# def solvepart2(data):
#     total = 0
#     last_val = None

#     for line in data.split("\n"):
#         first_fail = None
#         values = list(map(int,line.split()))
#         for i, value in enumerate(values):
#             if i == 0:
#                 last_val = value
#                 continue
#             if last_val < value and 3 >= abs(last_val-value) >= 1:
#                 if i == len(values)-1:
#                     total = total + 1
#                     break
#                 else: 
#                     last_val = value
#             else:
#                 if first_fail:
#                     break
#                 else:
#                     if i == len(values)-1:
#                         total = total + 1
#                         break
#                     else:
#                         first_fail = 1
#                         continue


#     for line in data.split("\n"):
#         first_fail = None
#         values = list(map(int,line.split()))
#         for i, value in enumerate(values):
#             if i == 0:
#                 last_val = value
#                 continue
#             if last_val > value and 3 >= abs(last_val-value) >= 1:
#                 if i == len(values)-1:
#                     total = total + 1
#                     break
#                 else: 
#                     last_val = value
#             else:
#                 if first_fail:
#                     break
#                 else:
#                     if i == len(values)-1:
#                         total = total + 1
#                         break
#                     else:
#                         first_fail = 1
#                         continue
#     return total



def is_good(line):
    inc_or_dec = (line==sorted(line) or line==sorted(line, reverse=True))
    ok = True
    for i in range(len(line)-1):
        difference = abs(line[i]-line[i+1])
        if not 1<=difference<=3:
            ok = False
    return inc_or_dec and ok

def do_the_thing(data):
    total = 0
    total2 = 0
    lines = data.split("\n")
    for line in lines:
        line = list(map(int,line.split()))
        if is_good(line):
            total += 1
        good = False
        for j in range(len(line)):
            lineless = line[:j] + line[j+1:]
            if is_good(lineless):
                good = True
        if good:
            total2 += 1
    print(total2)

if __name__ == "__main__":
    with open(DATA) as fp:
        data: str = fp.read().strip()
    
    do_the_thing(data)



