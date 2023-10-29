import math
from random import sample, randint


def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a


def podbor_pp():
    global h
    h = 0
    # диапазон
    n = int(1e9)
    p = randint(100, int(n))
    while not is_prime(p):
        p = randint(100, int(n))
        print('радном', p)
    print('Выбрано p: ', p)
    return p


def gcd_extended(num1, num2):
    if num1 == 0:
        return num2, 0, 1
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return div, y - (num2 // num1) * x, x


def pod_c():
    # Подборы ключей
    p = podbor_pp()
    ca = randint(1, p - 1)
    cb = randint(1, p - 1)

    while math.gcd(ca, (p - 1)) != 1:
        ca = randint(1, p - 1)
    while math.gcd(cb, (p - 1)) != 1:
        cb = randint(1, p - 1)

    print('ca: ', ca)
    print('cb: ', cb)
    l = 0
    da = gcd_extended(ca, p - 1)[1]
    db = gcd_extended(cb, p - 1)[1]
    if da <= 0:
        da = da+(p-1)
    if db <= 0:
        db = db + (p - 1)
    print('da: ', da)
    print('db: ', db)

    n = 51
    # Формируется колода карт
    v = sample(range(1, p - 1), 52)  # выбираем разные числа в диапазоне
    print('Колода карт', v)

    suitsC = '♧'
    suitsD = '♦'
    suitsH = '♥'
    suitsS = '♤'
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    sr = []
    for i in range(len(ranks)):
        sr.insert(i, ranks[i] + str(suitsC))
    for i in range(len(ranks)):
        sr.insert(i, ranks[i] + str(suitsD))
    for i in range(len(ranks)):
        sr.insert(i, ranks[i] + str(suitsH))
    for i in range(len(ranks)):
        sr.insert(i, ranks[i] + str(suitsS))
    print('Карты', sr)

    matrix = [v, sr]

    v1 = []  # Алиса отправляет Бобу защифрованный список
    for i in range(n):
        v1.insert(i, pow(v[i],ca,p))
    print('Список зашифрованный Алисой', v1)

    y = randint(0, n)  # Боб выбирает 2 случайные карты из полученного списка
    y1 = randint(0, n)

    u = pow(v1[y],da,p) # Алиса расшифровывает 2 полученные карты от Боба
    u1 = pow(v1[y1],da,p)
    # Узнаём карты Алисы по списку V
    k = v.index(u)
    k1 = v.index(u1)
    print('Карты Алисы', matrix[1][k], matrix[1][k1])

    v2 = v1  # Боб удаляет отправленные карты из списка
    if y1 > y:
        del v2[y1]
        del v2[y]
    else:
        del v2[y]
        del v2[y1]

    v2s = []  # Боб шифрует список, отправляет зашифрованный список Алисе,Алиса шифрует его
    for i in range(n - 2):
        v2s.insert(i, pow(v2[i],cb,p))

    x = randint(0, n - 2)  # Алиса выбирает 2 случайные карты из полученного списка , шифрует их и отправляет Бобу
    x1 = randint(0, n - 2)
    m = pow(v2s[x],da*db,p)
    m1 = pow(v2s[x1],da*db,p)


    b = v.index(m)
    b1 = v.index(m1)

    print('Карты Боба', matrix[1][b], matrix[1][b1])

    vkolode = v2s  # Крупье удаляет отправленные карты из списка
    if x1 > x:
        del vkolode[x1]
        del vkolode[x]
    else:
        del vkolode[x]
        del vkolode[x1]

    nastole = []

    # Находим карты соответствующие значениям списка V
    for i in range(0, 5):
        i = randint(0, len(vkolode) - 1)
        a = pow(vkolode[i],db*da,p)
        k = v.index(a)
        del vkolode[i]
        nastole.append(matrix[1][k])

    print('Карты Алисы', u, '', u1)
    print('Карты Боба', m, '', m1)
    print('NAstole', nastole)
    return 0


pod_c()
