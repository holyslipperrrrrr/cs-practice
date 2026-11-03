import numpy as np
def reshape_rows(values,width):
    if width!=0:
        if len(values)% width!=0:
                return []
        else:
            arr=np.asarray(values,dtype=float).reshape(-1,width)
            return arr.tolist()
    else:
          return []

def block (matrix,rows,columns):
     arr = np.asarray(matrix,dtype=float)
     return arr[np.ix_(rows,columns)].tolist()

def column_means(matrix):
      if len(matrix)==0:
           return []
      arr = np.asarray(matrix,dtype=float)
      sr=arr.mean(axis=0)
      return [round(float(x), 6) for x in sr]

def column_range(matrix,column):
     if len(matrix)==0:
          return 0.0
     arr = np.asarray(matrix,dtype=float)
     col= arr[:,column]
     return round(float(col.max()-col.min()), 6)