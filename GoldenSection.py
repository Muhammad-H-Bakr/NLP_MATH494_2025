import math

def f(x):
    return math.exp(-x) + 3 * x**2

def golden_section_search(a, b, tol=0.2):
    phi = 0.618
    resphi = 1 - phi

    lam = a + resphi * (b - a)
    mu = a + phi * (b - a)

    f_lam = f(lam)
    f_mu = f(mu)

    n = 1
    print(f"{'n':<3} {'a':<10} {'b':<10} {'λ':<10} {'μ':<10} {'f(λ)':<10} {'f(μ)':<10}")
    while abs(b - a) > tol:
        print(f"{n:<3} {a:<10.6f} {b:<10.6f} {lam:<10.6f} {mu:<10.6f} {f_lam:<10.6f} {f_mu:<10.6f}")
        if f_lam > f_mu:
            a = lam
            lam = mu
            f_lam = f_mu
            mu = a + phi * (b - a)
            f_mu = f(mu)
        else:
            b = mu
            mu = lam
            f_mu = f_lam
            lam = a + resphi * (b - a)
            f_lam = f(lam)
        n += 1

    print(f"{n:<3} {a:<10.6f} {b:<10.6f}")
    return (a + b) / 2

minimum = golden_section_search(-1, 5)
print(f"\nApproximate minimum at x = {minimum:.6f}")