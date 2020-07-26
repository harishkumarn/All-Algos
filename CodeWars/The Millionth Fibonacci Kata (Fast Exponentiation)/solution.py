matrix=[[1,1],[1,0]]
mulMat = lambda a,b:[[a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]],[a[1][0]*b[0][0]+a[1][1]*b[1][0],a[1][0]*b[0][1]+a[1][1]*b[1][1]]]
def mul(mat,exp):
  if exp==0:
      return [[1,0],[0,1]]
  elif exp ==1:
      return mat
  R = mul(mat,int(exp/2))
  if exp%2 == 0:
      return mulMat(R,R)
  else:
      return mulMat(mat,mulMat(R,R))

def fib(n):
    if n==0:
        return 0
    elif abs(n)%2 == 1 or n>0:
        return mul(matrix,abs(n)-1)[0][0]
    else:
        return -1*mul(matrix,abs(n)-1)[0][0]
