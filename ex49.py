for i in range(1, 10, 1):
    print("Tabuada do {}: \n".format(i))# print("oi",end='') => não pula linha
    for j in range(1, 11, 1):
        print(" {} x {} = {}".format(i, j, i*j))
