numbers = [1,2,-1,4,8,75,0]
positive_num_count = 0

for num in numbers:
    if num > 0:
        positive_num_count += 1
print("Final count of +ve nums : ",positive_num_count)