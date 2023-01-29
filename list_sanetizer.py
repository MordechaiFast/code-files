def ints_in_list(given_list):
    return_list = list()
    for item in given_list:
        try:
            return_list.append(int(item))
        except ValueError:
            pass
    return return_list
   
print(ints_in_list((1,2,3,'4', 'five', 6.0)))