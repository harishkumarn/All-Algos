from functools import lru_cache
import re
@lru_cache(maxsize=128)
def fact(n):
    if n <=1:
        return 1
    else:
        ret=1
        for i in range(2,n+1):
            ret*=i
    return ret
@lru_cache(maxsize=128)
def nCr(n,r):
    return fact(n)/(fact(n-r)*fact(r))
obj=re.compile(r'^\((\S+)(\+|-)(\d+)\)\^(\d+)$')    
def expand(expr):
    expr_grp=re.match(obj,expr)
    a=expr_grp.group(1)
    b=int(expr_grp.group(2)+expr_grp.group(3))
    expo=expr_grp.group(4)
    if expo == '0':
        return '1'
    elif expo == '1':
        return expr[1:expr.find('^')-1]
    ret=''
    a_coeff=re.match(r'^-?\d+',a)
    a_coeff=1 if a_coeff == None else abs(int(a_coeff.group(0)))
    expo=int(expo)
    x_var=re.match(r'^-?(\d+)?(\w+)$',a).group(2)
    if a[0] == '-':
        a_coeff*=-1
    for i in range(0,expo+1):
        mul=nCr(expo,i)
        temp=mul*(a_coeff**(expo-i))*(b**i)
        if temp < 0:
            ret+=str(temp)[:-2] if temp < -1  else '-' if expo != i else '-1'
        else :
            if temp>1 or expo == i :
                ret+='+'+str(temp)[:-2] if i>0 else str(temp)[:-2]    
            else:
                ret+='+' if i>0 else ''
        if expo != i :
            if (expo - i) > 1:
                ret+=x_var+'^'+str(expo-i)
            else:
                ret+=x_var
    return ret