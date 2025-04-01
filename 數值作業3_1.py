import math

# ----------------------------
# 1. 定義拉格朗日插值函數
# ----------------------------
def lagrange_interpolation(x_points, y_points, x_eval):
    """
    x_points: 已知節點 x 座標 (list or tuple)
    y_points: 已知節點對應的函數值 f(x) (list or tuple)
    x_eval:   要估計的目標 x
    return:   拉格朗日插值多項式在 x_eval 的近似值
    """
    n = len(x_points)
    total = 0.0
    for i in range(n):
        # 每一項對應 L_i(x_eval)
        xi = x_points[i]
        yi = y_points[i]
        Li = 1.0
        for j in range(n):
            if j != i:
                Li *= (x_eval - x_points[j]) / (xi - x_points[j])
        total += yi * Li
    return total

# ----------------------------
# 2. 已知資料點 (題目給定)
# ----------------------------
x_data = [0.698, 0.735, 0.768, 0.803]
y_data = [0.7661, 0.7432, 0.7193, 0.6946]

# 題目給的 cos(0.75) 近似值
cos_75_true = 0.7317 

# (A) 一次(線性)插值: 需 2 個點
x_lin   = [0.735, 0.768]
y_lin   = [0.7432, 0.7193]
lin_approx = lagrange_interpolation(x_lin, y_lin, 0.75)

# (B) 二次插值: 需 3 個點
x_quad  = [0.698, 0.735, 0.768]
y_quad  = [0.7661, 0.7432, 0.7193]
quad_approx = lagrange_interpolation(x_quad, y_quad, 0.75)

# (C) 三次插值: 需 4 個點
x_cubic = x_data
y_cubic = y_data
cubic_approx = lagrange_interpolation(x_cubic, y_cubic, 0.75)

# ----------------------------
# 4. 印出結果比較
# ----------------------------
print("實際 cos(0.75) (題目近似) =", cos_75_true)
print("一次插值近似 =", lin_approx, "誤差 =", abs(lin_approx - cos_75_true))
print("二次插值近似 =", quad_approx, "誤差 =", abs(quad_approx - cos_75_true))
print("三次插值近似 =", cubic_approx, "誤差 =", abs(cubic_approx - cos_75_true))
