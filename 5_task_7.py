import json

myl = []
profits = []

with open(file='firms.txt', encoding="UTF-8", mode='rt') as firms:
    for line in firms:
        line = tuple(line.split(' '))
        x = line[0]
        i = int(line[2]) - int(line[3])
        new_firm = {x : i}
        myl.append(new_firm)
        if i > 0:
            profits.append(i)
    aver_prof = {'average_profit': sum(profits)/len(profits)}
    myl.append(aver_prof)
with open("firms.json", "w") as jfirm:
    json.dump(myl, jfirm)

