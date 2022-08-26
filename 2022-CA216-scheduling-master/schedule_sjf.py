# Primary Author: Jack Farrell - 20352136
# I acknoledge DCU's academic integrity policy

import header

total = 0
avg = 0

process_dict, process_list = header.dictionary('schedule.txt')

def tagger(item):
   return item[1][1]

for k, v in sorted(process_dict.items(), key=tagger):
    total += int(v[1])
    avg += total
    header.display(k, v[1], total)
avg = avg / len(process_dict)
header.average(avg)