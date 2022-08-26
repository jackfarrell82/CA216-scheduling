# Primary Author: Jack Farrell - 20352136
# I acknoledge DCU's academic integrity policy

import header

total = 0
avg = 0
quantum = 10

process_dict, process_list = header.dictionary('schedule.txt')

while(1):
    done = True
    for items in process_list:
        if items[1] <= quantum and items[1]:
            total += items[1]
            avg += total
            header.display(items[0], process_dict[items[0]][1], total)
            done = True
            items[1] = 0
        elif items[1] <= 0:
            pass
        else:
            items[1] = items[1] - quantum
            total += quantum
            done = False
        
    if done == True:
        break

avg = avg / len(process_dict)
header.average(avg)