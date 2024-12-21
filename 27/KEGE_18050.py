def centr(cluster):
    x_centr, y_centr, minim = 0, 0, 10 ** 100
    for i in range(len(cluster)):
        res = 0
        for j in range(len(cluster)):
            x1, y1 = cluster[i]
            x2, y2 = cluster[j]
            res += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if res < minim:
            minim = res
            x_centr, y_centr = x1, y1
    return x_centr, y_centr

#Файл A
with open('27A_18050.txt') as f:
    cluster1, cluster2 = [], []
    f.readline()
    for i in f:
        x, y = map(float, i.replace(',', '.').split())
        if -1.5 < x < 0.6 and 0.6 < y < 3.2:
            cluster1.append((x, y))
        if 0.6 < x < 2.6 and 3.2 < y < 5.7:
            cluster2.append((x, y))
x1, y1 = centr(cluster1)
x2, y2 = centr(cluster2)
print((x1 + x2) / 2 * 10000, (y1 + y2) / 2 * 10000)

#Файл B
with open('27B_18050.txt') as f:
    cluster1, cluster2, cluster3 = [], [], []
    f.readline()
    for i in f:
        x, y = map(float, i.replace(',', '.').split())
        if 2.5 < x < 4.7 and 7.4 < y < 9.8:
            cluster1.append((x, y))
        if 4.1 < x < 6.3 and 4.8 < y < 7.4:
            cluster2.append((x, y))
        if 6.1 < x < 8.4 and 7.2 < y < 10.2:
            cluster3.append((x, y))
x1, y1 = centr(cluster1)
x2, y2 = centr(cluster2)
x3, y3 = centr(cluster3)
print((x1 + x2 + x3) / 3 * 10000, (y1 + y2 + y3) / 3 * 10000)