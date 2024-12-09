l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

def add_TwoNumbers(l1,l2):
    l1 = l1[ ::-1]
    l2 = l2[::-1]
    res = []
    temp = 0
    l1_str=""
    l2_str=""
    for i in range(len(l1)):
        l1_str = l1_str+str(l1[i])

    for i in range(len(l2)):
        l2_str = l2_str+str(l2[i])

    l1_int = int(l1_str)
    l2_int = int(l2_str)
    res_int = l1_int + l2_int
    # print(l1_int)
    # print(l2_int)
    # print(res_int)
    for i in range(len(str(res_int))):
        res.append(res_int%10)
        res_int = int(res_int/10)

    return(res)