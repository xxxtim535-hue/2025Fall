def f(x):
    return x**3 - 5*x**2 + 10*x - 80

def newtonmi_method(a0, b0, tolerance=1e-10, max_iter=1000):
    a = a0
    b = b0
    for i in range(max_iter):
        fx1 = f(a)
        fx2 = f(b)
        if abs(fx1 - fx2) < 1e-10:
            raise ValueError("爆")
        x_new = (fx2*a - fx1*b)/(fx2 - fx1)
        fx_new = f(x_new)
        if fx_new > 0:
            if abs(x_new - b) < tolerance:
                return x_new
            b = x_new
        if fx_new < 0:
            if abs(x_new - a) < tolerance:
                return x_new
            a = x_new
    raise ValueError("寄")

a0 = 2
b0 = 6
root = newtonmi_method(a0, b0)

print(f"{root:.9f}")
