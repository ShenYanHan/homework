# 題目1a：Euler法求解 y' = 1 + (y/t) + (y/t)^2，y(1) = 0，步長h=0.1
def problem1a():
    print("-" * 50)
    print("題目 1a：Euler 方法 (h = 0.1)")
    h = 0.1
    t = 1.0
    y = 0.0
    while t <= 2.0001:
        print("1a -> t=%.1f, y=%.6f" % (t, y))
        f = 1 + (y / t) + (y / t)**2
        y = y + h * f
        t = round(t + h, 10)

# 題目1b：Taylor二階法解同一題，加入導數資訊，精度較高
def problem1b():
    print("-" * 50)
    print("題目 1b：Taylor 二階法 (h = 0.1)")
    h = 0.1
    t = 1.0
    y = 0.0
    while t <= 2.0001:
        print("1b -> t=%.1f, y=%.6f" % (t, y))
        f = 1 + (y / t) + (y / t)**2
        df = (1 / t**2) * (-y - 2*y**2) + (1 / t) * (1 + 2*y / t)
        y = y + h * f + (h**2 / 2) * df
        t = round(t + h, 10)

# 題目2：Runge-Kutta四階法解二元微分方程組，兩種h都跑
def runge_kutta(h):
    print("-" * 50)
    print("題目 2：Runge-Kutta 方法 (h = %.2f)" % h)

    def factorial(n):  # 計算n!
        if n == 0:
            return 1
        f = 1
        for i in range(2, n+1):
            f *= i
        return f

    def cos(x):  # cos泰勒展開
        s = 0
        for i in range(10):
            s += ((-1)**i) * (x**(2*i)) / factorial(2*i)
        return s

    def sin(x):  # sin泰勒展開
        s = 0
        for i in range(10):
            s += ((-1)**i) * (x**(2*i+1)) / factorial(2*i+1)
        return s

    def f1(t, u1, u2):  # 第一式
        return 9*u1 + 24*u2 + 5*cos(t) - (1.0/3)*sin(t)

    def f2(t, u1, u2):  # 第二式
        return -24*u1 - 52*u2 - 9*cos(t) + (1.0/3)*sin(t)

    t = 0.0
    u1 = 4.0 / 3.0
    u2 = 2.0 / 3.0
    while t <= 1.0001:
        print("2 -> h=%.2f t=%.2f u1=%.6f u2=%.6f" % (h, t, u1, u2))
        k1_1 = h * f1(t, u1, u2)
        k1_2 = h * f2(t, u1, u2)
        k2_1 = h * f1(t + h/2, u1 + k1_1/2, u2 + k1_2/2)
        k2_2 = h * f2(t + h/2, u1 + k1_1/2, u2 + k1_2/2)
        k3_1 = h * f1(t + h/2, u1 + k2_1/2, u2 + k2_2/2)
        k3_2 = h * f2(t + h/2, u1 + k2_1/2, u2 + k2_2/2)
        k4_1 = h * f1(t + h, u1 + k3_1, u2 + k3_2)
        k4_2 = h * f2(t + h, u1 + k3_1, u2 + k3_2)
        u1 += (k1_1 + 2*k2_1 + 2*k3_1 + k4_1)/6
        u2 += (k1_2 + 2*k2_2 + 2*k3_2 + k4_2)/6
        t = round(t + h, 10)

# 執行所有題目
problem1a()
problem1b()
runge_kutta(0.05)
runge_kutta(0.1)
