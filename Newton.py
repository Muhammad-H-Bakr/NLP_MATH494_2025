import math

def df(x):
    return -math.exp(-x) + 6 * x

def d2f(x):
    return math.exp(-x) + 6

def newton_minimize(x0, tol=1e-5, max_iter=100):
    print(f"{'n':<3} {'x':<12} {'f_d(x)':<12} {'f_d_d(x)':<12}")
    print("-" * 45)

    x = x0
    for n in range(max_iter):
        dfx = df(x)
        d2fx = d2f(x)

        print(f"{n:<3} {x:<12.6f} {dfx:<12.6f} {d2fx:<12.6f}")
        if abs(dfx) < tol:
            break
        x = x - dfx / d2fx

    return x

x0 = 0.4
min_x = newton_minimize(x0)
print(f"\nApproximate minimum at x = {min_x:.6f}")