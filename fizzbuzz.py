numbers = [45, 22, 14, 65, 97, 72]
fb_nums = []
for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        fb_nums.append('fizzbuzz')
    elif num % 3 == 0:
        fb_nums.append('fizz')
    elif num % 5 == 0:
        fb_nums.append('buzz')
    else:
        fb_nums.append(num)
print(fb_nums)