import json

inc = int(input('inc : '))
start = int(input('start : '))

x = 365
i = 0

res = [n for n in range(x)]
for i in range(len(res)):
    res[i] = 0
for i in range(len(res)):
    if i == 0:
        res[i] = start - 3600 + inc
    elif i % 5 == 0 and i != 0:
        res[i] = res[i - 1] - 3600 + inc
    else:
        res[i] = res[i - 1] + inc
    print(res[i])


def recording():
    with open('res.xls', 'w') as fw:
        json.dump(res, fw)


recording()
