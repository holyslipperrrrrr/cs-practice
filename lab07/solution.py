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