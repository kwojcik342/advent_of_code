def check_number(in_number):
    b_is_correct = False
    b_is_increasing = True
    b_has_pair = False
    s_curr = str(in_number)
    num_len = len(s_curr)

    for index, dig in enumerate(s_curr):
        curr_dig = int(dig)
        if index > 0:
            if curr_dig < int(s_curr[index-1]):
                b_is_increasing = False
                break

    for index, dig in enumerate(s_curr):
        curr_dig = int(dig)
        if index > 0 and index < num_len-1:
            if curr_dig == int(s_curr[index-1]) and curr_dig != int(s_curr[index-2]) and curr_dig != int(s_curr[index+1]):
                b_has_pair = True
                break
        elif index == num_len-1:
            if curr_dig == int(s_curr[index-1]) and curr_dig != int(s_curr[index-2]):
                b_has_pair = True

    if b_has_pair and b_is_increasing:
        b_is_correct = True
    
    return b_is_correct


def check_range(in_min, in_max):
    curr_num = in_min
    possibilities = 0

    while curr_num <= in_max:
        is_correct = check_number(curr_num)

        if is_correct:
            possibilities += 1

        curr_num += 1

    return possibilities


if __name__ == "__main__":
    # print(check_number(111111))
    # print(check_number(223450))
    # print(check_number(123789))

    # print(check_number(111122))
    # print(len("123455"))

    print(check_range(234208, 765869))

