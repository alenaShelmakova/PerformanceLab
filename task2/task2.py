from sys import argv

def IsPointInCircle(x, y, xc, yc, r):
    if (x - xc) ** 2 + (y - yc) ** 2 < r**2:
       return 1
    if (x - xc) ** 2 + (y - yc) ** 2 == r**2: 
       return 0
    return 2
 
def main(*args):
    data1 = argv[1]
    data2 = argv[2]
     
    c = [] # записываем координаты круга
    with open(data1) as file: #'circle.txt'
        for line in file.readlines():
             c.append(line.split())

    x = [] # записываем координаты точек
    with open(data2) as file: #'points2.txt'
         for line in file.readlines():
             x.append(line.split())

    xc, yc, r = c[0][0], c[0][1], c[1][0]

    for i in x:
        x, y = i
        print(IsPointInCircle(float(x), float(y), float(xc), float(yc), float(r)))
    
if __name__ == "__main__":
    main()
