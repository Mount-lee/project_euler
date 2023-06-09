num_1 = num_2 = 1
num_3 = 2
count = 3

while len(str(num_1)) != 1000 or len(str(num_2)) != 1000 or len(str(num_3)) != 1000:
    num_1 = num_2 + num_3
    num_2 = num_1 + num_3
    num_3 = num_1 + num_2
    count = count + 3


print(count)