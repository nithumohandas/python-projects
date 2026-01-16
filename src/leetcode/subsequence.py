s = "aqc"
t = "ahbgdc"

def is_subsequence(sub_sequence, main_string):
    iter_1 = 0
    iter_2 = 0

    while iter_1 < len(sub_sequence) and iter_2 < len(main_string):
        if sub_sequence[iter_1] == main_string[iter_2]:
            iter_1 += 1
            iter_2 += 1
        else:
            iter_2 += 1

    if iter_1 == len(sub_sequence):
        return True
    return False

print(is_subsequence(s, t))