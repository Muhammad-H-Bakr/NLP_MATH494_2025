def function(x):
    return x**2 - 4 * x + 2

def main():
    interval_a = 0.0
    interval_b = 10.0
    final_x = -1.0
    final_value = float('inf')  # Equivalent to Integer.MAX_VALUE in Java

    for i in range(1, 4):  # Loop from 1 to 3 (inclusive)
        print(f"at n = {i}")
        print(f"current interval = [{interval_a}, {interval_b}]")
        delta = (interval_b - interval_a) / 4
        print(f"delta is = {delta}")

        for j in range(1, 4):  # Loop from 1 to 3 (inclusive)
            x = interval_a + j * delta
            fx = function(x)
            print(f"X{j} = {x} and F(x) = {fx}")

            if fx < final_value:
                final_x = x
                final_value = fx

        print(f"Xs = {final_x} F(Xs) = {final_value}")
        print("---")
        interval_a = final_x - delta
        interval_b = final_x + delta

    print(f"x* = {final_x} F(x*) = {final_value}")

if __name__ == "__main__":
    main()