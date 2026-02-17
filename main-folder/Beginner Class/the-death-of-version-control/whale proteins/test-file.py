def compare(x, y):
    counts = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            counts += 1
            #print(i, x[i], y[i])
    print(counts)
    return(0)

list1 = "eeeeee eeeeee"
list2 = "unitad statas"
compare(list1, list2)