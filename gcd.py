def gcd(n1, n2):
    gcf = 1
    for i in range(1, min(n1, n2)+1):
        if n1 % i == 0 and n2 % i == 0:
            gcf = i
    return gcf


print(gcd(3, 18))
