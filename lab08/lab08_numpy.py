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

matrix = np.arange(1, 26).reshape(5, 5)
print(matrix[:3], matrix[:3].shape)
print(matrix[-2:], matrix[-2:].shape)
print(matrix[:, :2], matrix[:, :2].shape)
print(matrix[1:4, 2:5], matrix[1:4, 2:5].shape)
print(matrix[-2:, -2:], matrix[-2:, -2:].shape)

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print(vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
print(small_matrix)
small_matrix[1:, 1:] = 9
print(small_matrix)

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2]=-1
print(changed_hours , hours)

changed_matrix = matrix.copy()

changed_matrix[1, :] = 0       
changed_matrix[:, -1] = -1     
changed_matrix[1:4, 1:4] = 100 
print(changed_matrix, matrix)

numbers = np.arange(12)          
table = numbers.reshape(3, 4)    
transposed = table.T             

print( numbers.shape, table.shape, transposed.shape)  