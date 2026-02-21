import math

def riemann_sum_step(func, x, delta_x):
    """ Calculate an individual step (f'(x)Δx) of the Riemmann sum
        - Note that func should be f'
    """
    return func(x) * delta_x

def riemann_sum(f_a, f_prime, a, b, n):
    """ Calculate the Riemann sum of f(x), over the interval x = [a, b], integrating over step sizes of (b-a) / n """
    
    # If there are no steps remaining to integrate, return the left bound
    if n <= 0 or (b-a) <= 0:
        return f_a
    
    return riemann_sum(f_a, f_prime, a+(b-a)/n, b, n - 1) + riemann_sum_step(f_prime, a, (b-a)/n)

# v_tilda analytical
def v(t):
    return 1 - math.cos(t)

# v_tilda'
def v_prime(t):
    return math.sin(t)

def main():
    f_name = "v_tilda"
    a = float(input("Enter the left limit: "))
    b = float(input("Enter the right limit: "))
    f_a = float(input("Enter the initial condition: "))
    n = int(input("Enter the number of integration steps: "))
    print("Finding the Riemann sum of " + f_name + ", over the interval x = [" f"{a}" + ", " + f"{b}" + "], with f_initial = " + f"{f_a}" + ", using " + f"{n:.0f}" + " integration steps...")
    print("Your Riemann sum is: " + f"{riemann_sum(f_a, v_prime, a, b, n)}")
    print("The analytical solution is: " + f"{v(b)}")

if __name__ == "__main__":
    main()