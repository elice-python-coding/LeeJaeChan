s = input()

eng = [x for x in s if x.isalpha()]
num = sum([int(x) for x in s if x.isdigit()])

eng.sort()

if num != 0:
    eng.append(str(num))

print(''.join(eng))