# Primary Author: Jack Farrell - 20352136
# I acknoledge DCU's academic integrity policy

def dictionary(file):
    process_dict = {}
    process_list = []
    try:
        with open(file) as f:
            for lines in f:
                name, priority, time = lines.split(",")
                name = name.strip()
                priority = priority.strip()
                time = time.strip()
                process_dict[name] = [int(priority), int(time)]
                item = [name, int(time)]
                process_list.append(item)
        return process_dict, process_list
    except:
        print("Encountered an error when trying to open/read the file")
        exit(0)

def display(k, v, total):
    print(f'process ({k}) arrived at time (0) and ran for ({v}) MS. it had a turn-around time of ({total})')

def average(avg):
    print(f'The average turn-around time is {avg} MS')
