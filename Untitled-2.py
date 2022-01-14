import numpy as np

a = np.array((1, 2, 3, 4))
b = np.array((4, 3, 2, 1))

#ユークリッド距離の計算
c = np.linalg.norm(a-b)

#出力
print(c)