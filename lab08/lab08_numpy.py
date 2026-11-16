import numpy as np
hours = np.arange(0,22,3)
line =np.linspace(0,1,5)
zeros =np.zeros(6, dtype=int)
unknown_table=np.full((2,3,), -1)
identity=np.eye(3)

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

print(hours[2], hours[-1], hours[2:6], hours[0:-1:2], hours[::-1])
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print(temperatures.shape,temperatures.ndim,temperatures.size)

print(temperatures[1,2], temperatures[0], temperatures[:, -1], temperatures[:2,1:], temperatures[0:2,1:3])