import math


# Zadanie 1
def zad1():
    list1 = [0,-2,1,7,3,4]
    print(list1[::-1])

# Zadanie 2
# dla x = 2, y = 4 => 2.8183362733213935
# dla x = -9.5, y=6.4 => -1.3367487551407415
def zad2():
    x = float(input("Podaj x: "))
    y = float(input("Podaj y: "))
    result = math.e+math.log10(x**2 + 1)*(x-1)/(math.cos(y**3-1)+6)
    print(result)

# Zadanie 3
def zad3():
    x = float(input("Podaj x: "))
    y = float(input("Podaj y: "))
    z = float(input("Podaj z: "))
    c = input("Podaj opcje: ")
    result =0
    match c:
        case 1:
            result = x+y+z
        case 2:
            result = x-y-z
        case 3:
            result = x*y*z
        case _:
            if y==0 or z ==0:
                print("nie można dzielić przez 0!")
            else:
                result = x/y/z
    print(result)


# Zadanie 4
def zad4():
    traingle_height = int(input("Podaj wysokość trójkąta: "))
    for i in range(traingle_height):
        for j in range(1,i+2):
            print("X",end="")
        print()

# Zadanie 5
def zad5():
    matrix = [[i for i in range(1,8,3)] for j in range(1,8,3) ]
    print(matrix)

# Zadanie 6
def zad6():
    a=1
    b=2
    c=3
    time = lambda x,y,z: str(x)+" godzin "+str(y)+" minut "+str(z) +" sekund"
    print(time(a,b,c))

# Zadanie 7
# dla x = 2, k = 7 => 6.7749004086429565
def zad7():
    x1=2
    k1=7
    def calculate(x,n=10,k=2):
        result=math.log(x**2 + 5,n)*(k+1)*x
        return result
    print(calculate(x1,k1))

# Zadanie 8
def zad8():
    def recursive_factorial(n):
        if n==1:
            return 1
        factorial= n * recursive_factorial(n - 1)
        return factorial
    print(recursive_factorial(6))
    def iterative_factorial(n):
        if n<=1: return 1
        factorial_result=1
        for i in range(2,n+1):
            factorial_result*=i
        return factorial_result
    print(iterative_factorial(5))

# Zadanie 9
def zad9():
    def fibonacci(n):
        if n==0 or n==1:
            return 0
        if n==2:
            return 1
        return fibonacci(n-1)+fibonacci(n-2)+fibonacci(n-3)
    print(fibonacci(7))



if __name__ == '__main__':
    # zad1()
    # zad2()
    # zad3()
    # zad4()
    zad5()
    # zad6()
    # zad7()
    # zad8()
    # zad9()