import math


def f_prime(x):
    return -math.exp(-x) + 6 * x


def bisection_table(a, b, max_n):
    print(f"{'n':<2} {'I':<25} {'a':<10}"
          f"{'b':<10}{'midpoint':<12}{'f`(midpoint)':<15}")
    print("-" * 80)

    for n in range(max_n + 1):
        midpoint = (a + b) / 2
        df_mid = f_prime(midpoint)

        print(f"{n:<2} [{a:.5f},{b:.5f}] {a:<10.5f}"
              f"{b:<10.5f}{midpoint:<12.5f}{df_mid:<15.5f}")
        if df_mid < 0:
            a = midpoint
        else:
            b = midpoint


a = -1
b = 5
max_n = 5
bisection_table(a, b, max_n)
