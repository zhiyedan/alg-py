def full_package(capacity,costs,values):
    res = [0 for i in range(capacity+1)]
    num = len(values)
    selected = [[] for i in range(capacity+1)]
    for i in range(num):
        seq = range(costs[i],capacity+1)
        for j in seq:
#             temp_value = res[j-costs[i]] + values[i]
#             res[j] = max(temp_value,res[j])
            temp_value = res[j-costs[i]]+values[i]
            if res[j] < temp_value:
                res[j] = temp_value
                selected[j] = selected[j-costs[i]][:]
                selected[j].append(i)
    return res[capacity],selected[capacity]
capacity=10
costs=[4,6,6]
values=[4,5,6]
best_value,select = full_package(capacity,costs,values)
print('best value is %d ' % best_value)
print(select)