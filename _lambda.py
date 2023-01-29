def read_data():
    return [1,2,3,4,5,6,7,8,9,10]

mean = lambda data: sum(data)/len(data)

average = mean(read_data())