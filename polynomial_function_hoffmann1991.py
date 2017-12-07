from math import factorial

def newton_binom(n ,k):
    while(n>=k):
        n, k = int(n), int(k)
        n_fact = factorial(n)
        k_fact = factorial(k)
        nk_fact = factorial(n-k)

        denom = k_fact * nk_fact

        return int(n_fact/denom)

def coeff_1(k, q, j):
    u = q + k
    d = q + j
    return int(newton_binom(u, d))

def coeff_2(k, q, j):
    u = k - q
    d = j
    return int(newton_binom(u, d))

def coeff_3(j):
    if j>0:
        return "(z + r)^{}".format(j)
    else: return "1"

def coeff_4(k, q, j):
    e = k - q - j
    if e > 0:
        return "(z - r)^{}".format(e)
    else: return "1"

def G_func(k, q):

    eq_total = []

    for j in range(k - q):
        s1 = coeff_1(k, q, j)
        s2 = coeff_2(k, q, j)
        s3 = coeff_3(j)
        s4 = coeff_4(k, q, j)
        eq_total.append("{} x {} x {} x {}".format(s1, s2, s3, s4))

    for each in eq_total: print(each)

def a_func(k, q):
    eq_total = []

    for j in range(k - q):
        s1 = newton_binom(2*q+k-q, q+j)
        s2 = newton_binom(k-q, j)
        eq_total.append("{} x {}".format(s1, s2))

    for each in eq_total: print(each)

# G_func(2,0)
a_func(2,1)

# TODO ogólnie poprawić, bo coś nie działa - albo nie rozumiem tej publikacji (tabela 1 dotyczy jakich wzorów?)
