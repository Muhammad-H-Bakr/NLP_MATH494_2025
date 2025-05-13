def function(x):
    return x ** 2 + 2 * x


def main():
    a = -3.0
    b = 5.0
    l = 'λ'  # Unicode for lambda
    m = 'μ'  # Unicode for mu
    feb = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]  # Fibonacci sequence

    for i in range(1, 9):  # Loop from 1 to 8
        lamda = a + (feb[9 - i - 1] / feb[9 - i + 1]) * (b - a)
        mu = a + (feb[9 - i] / feb[9 - i + 1]) * (b - a)
        f_lamda = function(lamda)
        f_mu = function(mu)

        print(
            f"m = {i}, a = {a:.6f}, b = {b:.6f}, {l} = {lamda:.6f},"
            f" {m} = {mu:.6f}, f({l}) = {f_lamda:.6f}, f({m}) = {f_mu:.6f}")

        # Update interval based on comparison
        if f_lamda > f_mu:
            a = lamda
        else:
            b = mu

    print(f"Final interval: a = {a:.6f}, b = {b:.6f}")


if __name__ == "__main__":
    main()
