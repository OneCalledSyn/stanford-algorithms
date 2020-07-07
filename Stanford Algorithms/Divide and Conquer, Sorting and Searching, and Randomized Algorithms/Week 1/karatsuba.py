import math

def karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y
    else:
        bigger = max(len(str(x)), len(str(y)))
        splitter = math.ceil(bigger/2)

        a = x // 10**splitter
        b = x % 10**splitter
        c = y // 10**splitter
        d = y % 10**splitter

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        adbc = karatsuba(a + b, c + d) - ac - bd

        return ac * 10**(splitter*2) + (adbc * 10**splitter) + bd

print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
2718281828459045235360287471352662497757247093699959574966967627))
