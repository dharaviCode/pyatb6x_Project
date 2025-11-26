response_time = [1200, 1300, 1400, 1500]

def mil_sec(x):
    return x/1000

#all_mil_sec = list(map(mil_sec, response_time))
all_mil_sec = list(map(lambda x: x/1000, response_time))
print(all_mil_sec)