import collections


def zad1():
    print("Zadanie 1")
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididuntut labore et dolore magna aliqua. Dolor sed viverra ipsum nunc aliquet bibendum enim. Inmassa tempor nec feugiat. Nunc aliquet bibendum enim facilisis gravida. Nisl nunc mi ipsumfaucibus vitae aliquet nec ullamcorper. Amet luctus venenatis lectus magna fringilla. Volutpat maecenas volutpat blandit aliquam etiam erat velit scelerisque in. Egestas egestas fringillaphasellus faucibus scelerisque eleifend. Sagittis orci a scelerisque purus semper eget duis. Nullapharetra diam sit amet nisl suscipit. Sed adipiscing diam donec adipiscing tristique risus necfeugiat in. Fusce ut placerat orci nulla. Pharetra vel turpis nunc eget lorem dolor. Tristiquesenectus et netus et malesuada."
    text_words = len(text)
    text = text.lower().replace(",", "").replace(".", "")
    unique_words = set(text.split(" "))
    unique_words_count = len(unique_words)
    print(f"Słowa w całym tekście: {text_words}, unikatowe słowa: {unique_words_count}")


def zad2():
    print("Zadanie 2")
    a = {1, 2, 3, 4, 5}
    b = {2, 4, 5}
    print("A jest podzbiorem B", a.issubset(b))
    print("A jest podzbiorem B", a < b)
    print("A jest nadzbiorem B", a.issuperset(b))
    print("A jest nadzbiorem B", a > b)
    print("przecięcie A i B", a.intersection(b))
    print("przecięcie A i B", a and b)
    print("suma zbiorów A i B", a.union(b))
    print("suma zbiorów A i B", a or b)
    print("rózńica zbiorów A i B", a.difference(b))
    print("różnica symetryczna zbiorów A i B", a.symmetric_difference(b))


def zad4():
    slowa = {1: 'jeden', 2: 'dwa', 3: 'trzy', 4: 'cztery', 5: 'pięć', 6: 'sześć', 7: 'siedem', 8: 'osiem',
             9: 'dziewięć', 10: 'dziesięć', 11: 'jedenaście', 12: 'dwanaście', 13: 'trzynaście', 14: 'czternaście',
             15: 'piętnaście', 16: 'szesnaście', 17: 'siedemnaście', 18: 'osiemnaście', 19: 'dziewiętnaście',
             20: 'dwadzieścia', 30: 'trzydzieści', 40: 'czterdzieści', 50: 'pięćdziesiąt', 60: 'sześćdziesiąt',
             70: 'siedemdziesiąt', 80: 'osiemdziesiąt', 90: 'dziewięćdziesiąt', 100: 'sto'}

    num = int(input("Podaj liczbę <1-99>: "))
    if num in slowa:
        print(slowa[num])
    else:
        cyfra_jednostek = num % 10
        cyfra_dziesiatek = num - cyfra_jednostek
        print(slowa[cyfra_dziesiatek] + slowa[cyfra_jednostek])


def zad5():
    print("Zadanie 5")
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididuntut labore et dolore magna aliqua. Dolor sed viverra ipsum nunc aliquet bibendum enim. Inmassa tempor nec feugiat. Nunc aliquet bibendum enim facilisis gravida. Nisl nunc mi ipsumfaucibus vitae aliquet nec ullamcorper. Amet luctus venenatis lectus magna fringilla. Volutpat maecenas volutpat blandit aliquam etiam erat velit scelerisque in. Egestas egestas fringillaphasellus faucibus scelerisque eleifend. Sagittis orci a scelerisque purus semper eget duis. Nullapharetra diam sit amet nisl suscipit. Sed adipiscing diam donec adipiscing tristique risus necfeugiat in. Fusce ut placerat orci nulla. Pharetra vel turpis nunc eget lorem dolor. Tristiquesenectus et netus et malesuada."
    text = text.lower().replace(",", "").replace(".", "")
    unique_words = collections.Counter(text.split(" "))
    unique_words_count = len(unique_words)
    print(unique_words)
    print(unique_words_count)


def zad6():
    d = collections.defaultdict(lambda: 5)
    for _ in range(5):
        key = input("Enter a key: ")
        d[key] += 1
    print(d)


def zad7():
    queue = collections.deque(['k', 'a', 'j', 'a', 'o'])
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            print("Wyraz nie jest palindromem")
            break
    else:
        print("Wyraz jest palindromem")


if __name__ == '__main__':
    zad1()
    zad2()
    zad4()
    zad5()
    zad6()
    zad7()
