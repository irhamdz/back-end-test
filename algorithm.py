def set_of_num(num: int):
    temp_list = []
    for x in range(num, 0, -1):
        temp_list.append(x)
        i = x
        while i > 0:
            if x + i > num:
                i -= 1
                continue
            temp_list.append(i)

            if sum(temp_list) == num:
                print(','.join(str(z) for z in temp_list))
                if i == 1:
                    temp_list = []
                else:
                    temp_list.pop()

            if i == 1 and sum(temp_list) < num and temp_list != []:
                i = 1
            else:
                i -= 1

        if sum(temp_list) == num:
            print(','.join(str(z) for z in temp_list))
            temp_list = []
