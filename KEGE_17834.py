#Функция нахождения центра кластера
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
with open('27_A_17834.txt') as f:
    f.readline()
    cluster1, cluster2 = [], []
    for i in f:
        x, y = map(float, i.replace(',', '.').split())
        if -2 <= x <= 6 and -3 <= y <= 5:
            cluster1.append((x, y))
        if 6 <= x <= 14 and 3 <= y <= 11:
            cluster2.append((x, y))
x1, y1 = centr(cluster1)
x2, y2 = centr(cluster2)
print((x1 + x2) / 2 * 100, (y1 + y2) / 2 * 100)

#Файл B
with open('27_B_17834.txt') as f:
    f.readline()
    cluster1, cluster2, cluster3 = [], [], []
    for i in f:
        x, y = map(float, i.replace(',', '.').split())
        if -3 <= x <= 3 and 2 <= y <= 8:
            cluster1.append((x, y))
        if 1 <= x <= 7 and -4 <= y <= 2:
            cluster2.append((x, y))
        if 5 <= x <= 11 and 3 <= y <= 9:
            cluster3.append((x, y))
x1, y1 = centr(cluster1)
x2, y2 = centr(cluster2)
x3, y3 = centr(cluster3)
print((x1 + x2 + x3) / 3 * 100, (y1 + y2 + y3) / 3 * 100)