from sys import argv
from itertools import islice, cycle

def rotate(lst, k):
    return list(islice(cycle(lst[::-1]), k, len(lst)+k))

def main(*args):
    n = int(argv[1])
    m = int(argv[2])

    a = [i for i in range(1,n+1)]

    b =[1]

    while True:
        for i in range(m):
            var = a[i]
        b.append(var)  
        a = rotate(a, 2)[::-1]
  
        if b[-1] == 1:
            b.pop()
            break

    for i in b:
        print(i, end='')
    print()

if __name__ == "__main__":
    main()
