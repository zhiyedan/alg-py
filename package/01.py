# 0-1
# def zero_one_packete(values,costs,capacity):
#     temp_value = [0] * (capacity+1)
#     # temp_choose = [0] * len
#     for i in range(len(values)):
#         print(i,'round')
#         list_for = range(costs[i],capacity+1)
#         list_for.reverse()
#         for j in list_for:
#             temp_value[j] = max(temp_value[j],temp_value[j-costs[i]]+values[i])
#     return temp_value[capacity]
#
# values = [3,4,1]
# costs = [3,1,4]

def zero_one_package(capacity,costs,values):
    res = [0 for i in range(capacity+1)]
    num = len(values)
    selected = [[] for i in range(capacity+1)]
    for i in range(num):
        if costs[i]>capacity:
            continue
        seq = range(costs[i],capacity+1)
        seq.reverse()
        for j in seq:
            temp_value = res[j-costs[i]]+values[i]
            if res[j] < temp_value:
                res[j] = temp_value
                selected[j] = selected[j-costs[i]][:]
                selected[j].append(i)
    return res[capacity],selected[capacity]
capacity=10
costs=[4,5,6]
values=[3,5,6]
best_value,selected = zero_one_package(capacity,costs,values)
print('best value is %d ' % best_value)
selected