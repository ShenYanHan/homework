# 題目資料
T = [0, 3, 5, 8, 13]         # 時間（秒）
D = [0, 200, 375, 620, 990]  # 距離（英尺）
V = [75, 77, 80, 74, 72]     # 速度（英尺/秒）

# 建立 Hermite 插值所需的 z 和 Q 表格
n = len(T)
z = [0] * (2 * n)
Q = [[0 for _ in range(2 * n)] for _ in range(2 * n)]

for i in range(n):
    z[2 * i] = T[i]
    z[2 * i + 1] = T[i]
    Q[2 * i][0] = D[i]
    Q[2 * i + 1][0] = D[i]
    Q[2 * i + 1][1] = V[i]
    if i != 0:
        Q[2 * i][1] = (Q[2 * i][0] - Q[2 * i - 1][0]) / (z[2 * i] - z[2 * i - 1])

# 計算差商表
for j in range(2, 2 * n):
    for i in range(2 * n - j):
        Q[i][j] = (Q[i + 1][j - 1] - Q[i][j - 1]) / (z[i + j] - z[i])

# Hermite 插值函數
def hermite_poly(t):
    result = Q[0][0]
    product = 1.0
    for i in range(1, 2 * n):
        product *= (t - z[i - 1])
        result += Q[0][i] * product
    return result

# 數值微分求導數（速度）
def hermite_derivative(t):
    h = 0.0001
    return (hermite_poly(t + h) - hermite_poly(t - h)) / (2 * h)

# === (a) 在 t = 10 時的位置與速度 ===
pos_10 = hermite_poly(10)
vel_10 = hermite_derivative(10)

print("(a) t = 10 秒")
print("    預測位置：", round(pos_10, 2), "英尺")
print("    預測速度：", round(vel_10, 2), "英尺/秒")

# === (b) 檢查是否超過 55 mi/h（約 80.67 英尺/秒）===
limit = 80.67
t = 0.0
exceed_time = None

while t <= 13:
    v = hermite_derivative(t)
    if v > limit:
        exceed_time = round(t, 2)
        break
    t += 0.05  # 間距可調整

if exceed_time:
    print("(b) 有超速！第一次超過 55 mi/h 發生在 t =", exceed_time, "秒")
else:
    print("(b) 沒有超速")

# === (c) 找最大速度（預測值）===
t = 0.0
max_v = -1000
max_t = 0

while t <= 13:
    v = hermite_derivative(t)
    if v > max_v:
        max_v = v
        max_t = t
    t += 0.05

print("(c) 預測最大速度：", round(max_v, 2), "英尺/秒，發生在 t =", round(max_t, 2), "秒")

