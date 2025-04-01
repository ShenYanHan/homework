
def inverse_interpolation(x, y, guess, times=5):
    for _ in range(times):
        # 套用簡化的線性插值公式（兩點間插值，多點可近似）
        for i in range(len(x) - 1):
            if y[i] >= guess >= y[i+1] or y[i] <= guess <= y[i+1]:
                # 線性反插值公式
                new_x = x[i] + (guess - y[i]) * (x[i+1] - x[i]) / (y[i+1] - y[i])
                guess = new_x  # 更新猜測值
                break
    return guess

# 給定的 (x, e^(-x)) 資料
x_vals = [-0.3, -0.4, -0.5, -0.6]
y_vals = [0.740818, 0.670320, 0.606531, 0.548812]

# 初始猜測（任選在 y 值範圍內的數）
init_guess = 0.6

# 執行反插值
result = inverse_interpolation(x_vals, y_vals, init_guess)

# 輸出結果
print("近似解 x ≈", result)
