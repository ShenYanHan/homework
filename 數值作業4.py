# 基本函數定義
def f1(x):
    return math.exp(x) * math.sin(4 * x)

def f2(x):
    return x**2 * math.log(x)

def f3(x, y):
    return 2 * y * math.sin(x) + math.cos(x)**2

def f4a(x):
    return x**(-1/4) * math.sin(x)

def f4b(x):
    return x**(-4) * math.sin(x)

# 自訂 sin, cos, exp, log 函數（簡化版）
def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def exp(x):
    return math.exp(x)

def log(x):
    return math.log(x)

# 複合梯形法
def trapezoidal(f, a, b, h):
    n = int((b - a) / h)
    total = f(a) + f(b)
    for i in range(1, n):
        total += 2 * f(a + i * h)
    return (h / 2) * total

# 複合Simpson法
def simpson(f, a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        weight = 4 if i % 2 == 1 else 2
        total += weight * f(a + i * h)
    return (h / 3) * total

# 複合中點法
def midpoint(f, a, b, h):
    n = int((b - a) / h)
    total = 0
    for i in range(n):
        mid = a + (i + 0.5) * h
        total += f(mid)
    return total * h

# 高斯積分（三點）
def gaussian3(f, a, b):
    # 範圍轉換 [-1, 1] 到 [a, b]
    x_vals = [-math.sqrt(3/5), 0, math.sqrt(3/5)]
    w_vals = [5/9, 8/9, 5/9]
    result = 0
    for i in range(3):
        t = ((b - a) / 2) * x_vals[i] + (a + b) / 2
        result += w_vals[i] * f(t)
    return ((b - a) / 2) * result

# 雙重積分用Simpson法
def simpson_double(f, ax, bx, ay_func, by_func, nx, ny):
    hx = (bx - ax) / nx
    total = 0
    for i in range(nx + 1):
        xi = ax + i * hx
        ay = ay_func(xi)
        by = by_func(xi)
        hy = (by - ay) / ny
        subtotal = 0
        for j in range(ny + 1):
            yj = ay + j * hy
            coeff_y = 1
            if j != 0 and j != ny:
                coeff_y = 4 if j % 2 == 1 else 2
            subtotal += coeff_y * f(xi, yj)
        coeff_x = 1
        if i != 0 and i != nx:
            coeff_x = 4 if i % 2 == 1 else 2
        total += coeff_x * subtotal * hy / 3
    return total * hx / 3

# 不定積分用變數變換
def transform_integral(f, t0, t1, n):
    h = (t1 - t0) / n
    total = 0
    for i in range(n + 1):
        t = t0 + i * h
        x = 1 / t
        dxdt = -1 / (t**2)
        val = f(x) * abs(dxdt)
        coeff = 1
        if i != 0 and i != n:
            coeff = 4 if i % 2 == 1 else 2
        total += coeff * val
    return (h / 3) * total

# 主程式
def main():
    h = 0.1
    print("題目 1a (梯形法):", trapezoidal(f1, 1, 2, h))
    print("題目 1b (Simpson):", simpson(f1, 1, 2, 10))
    print("題目 1c (中點法):", midpoint(f1, 1, 2, h))
    print("題目 2_n3 (高斯 n=3):", gaussian3(f2, 1, 1.5))
    print("題目 3a (雙重Simpson):", simpson_double(f3, 0, math.pi/4, math.sin, math.cos, 4, 4))
    print("題目 4a (不定積分 f4a):", transform_integral(f4a, 1, 100, 4))
    print("題目 4b (不定積分 f4b):", transform_integral(f4b, 0.01, 1, 4))

# 程式進入點
import math
main()
