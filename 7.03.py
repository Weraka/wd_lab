import math

def ex():
    try:
        a = int(input())
        b = int(input())
        result = a / b
        print(result)

    except Exception:
        print("Error")

    #except ValueError:
        #print("brak liczb")
    #else:
        #print(result)

#ex()

def ex2():
    l1 = [1, 2, 3]
    l2 = []
    for i in l1:
        l2.append(i**2)
    print(l2)

    b = [3**y for y in range(6)]
    print(b)
    c = [x for x in b if x%2 == 1]
    print(c)
    d = [(i, i) for i in l1 for j in l2]
    print(d)

#ex2()

def rown_kw(a, b, c):

    delta = b*b - 4*a*c
    if delta < 0:
        print("Brak rozwiązań")
    elif delta == 0:
        print((-b)/2*a)
    else:
        print(((-b) - math.sqrt(delta)) / 2*a)
        print(((-b) + math.sqrt(delta)) / 2*a)

def dl_odc(x1=1, x2=2, y1=3, y2=4):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#plik = open('Tekst.txt', 'r',  = 'utf-8')
#znaki = plik.read(10)
#linia = plik.readline()
#linia = plik.readline()
#plik.close()


















def main():
    #a = int(input("podfsjpfds"))
    #b = int(input("dhfsohfdos"))
    #c = int(input("fdsiuusii"))
    #rown_kw(a, b, c)
    print(dl_odc(x1=1, x2=2, y1=3, y2=4))
main()


