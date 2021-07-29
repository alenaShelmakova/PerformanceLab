from sys import argv

def main(*args):

    data = argv[1]
    a = []
    with open(data) as file: 
        for line in file.readlines():
             a.append(int(line))
    a.sort()

    counter = 0
    steps = 0
    max = 0
    maxN = 0
    b = [0]*len(a)

    for i in range(len(a)):
        counter = a.count(a[i])
        if counter == len(a):
            break
        b[i] += a.count(a[i])

    for i in range(len(b)):
        for j in range(len(a)):
            if b[i]>max:
                max = b[i]
                maxN = a[i]

    if maxN > 1:
        for i in range(len(a)):
            while a[i] != maxN:
                if a[i] < maxN:
                    a[i] +=1
                    steps +=1
                if a[i] > maxN:
                    a[i] -=1
                    steps +=1
    else:
        for i in range(len(a)):
            while a[i] != a[1]:
                if a[i] < a[1]:
                    a[i] +=1
                    steps +=1
                if a[i] > a[1]:
                    a[i] -=1
                    steps +=1
    print(steps)

if __name__ == "__main__":
    main()