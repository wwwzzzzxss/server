import numpy as np

def dijkstra(key_point = 2):    
    e = np.zeros((11, 11), dtype=int)
    inf = 99999999
    # 讀入頂點個數，邊個數
    n = 6
    m = 9

    # 初始化
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j : 
                e[i][j] = 0
            else:
                e[i][j] = inf

    # 讀入邊
    t1 = [
    1, 2, 1,\
    1, 3, 12,\
    2, 3, 9,\
    2, 4, 3,\
    3, 5, 5,\
    4, 3, 4,\
    4, 5, 13,\
    4, 6, 15,\
    5, 6, 4]

    for i in range(m):
        e[t1[i*3]][t1[i*3+1]] = t1[i*3+2]

    # 初始 dis 陣列，從 key_point 到其餘各點的初始路程
    dis = np.zeros(11, dtype=int)
    for i in range(1, n+1):
        dis[i] = e[key_point][i]

    # 初始 book 陣列
    book = np.zeros(11, dtype=int)
    book[key_point] = 1

    # Dijkstra Algorithm
    for i in range(1, n):
        # 找到離 key_point 點最近的頂點
        min = inf
        for j in range(1, n+1):
            if book[j] == 0 and dis[j] < min :
                min = dis[j]
                u = j
        book[u] = 1
        for v in range(1, n+1):
            if e[u][v] < inf:
                if dis[v] > dis[u] + e[u][v]:
                    dis[v] = dis[u] + e[u][v]

    # 輸出
    for i in range(1, n+1):
        print(dis[i])


    target = 99999999
    index = -1
    for i in range(2, n+1,2):
        if dis[i] < target:
            index = i
    print(index)
    return index

    '''
    驗證資料:
    6 9
    1 2 1
    1 3 12
    2 3 9
    2 4 3
    3 5 5
    4 3 4
    4 5 13
    4 6 15
    5 6 4
    '''