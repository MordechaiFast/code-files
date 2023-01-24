def ints_in_list(list):
    return_list = list()
    for item in list:
        try:
            return_list.append(int(item))
        exxcept TypeError:
            pass
    return return_list
   
print(ints_in_list((1,2,3,'4', 'five', 6.0))
