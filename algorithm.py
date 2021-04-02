def set_of_num(num: int):
    i = num
    temp_list = []
    for x in range(num, 1, -1):
        temp_list.append(x)

        while i > 1:

            if sum(temp_list) == num:
                print(''.join(str(z) for z in temp_list))
                temp_list = []


set_of_num(4)
