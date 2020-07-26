memoize={0:[''],1:['()']}
def balanced_parens(n):
    global memoize
    if n in memoize.keys():
        return memoize[n]
    generate=lambda a,b:'('+a+')'+b
    l=[]
    for i in range(0,n):
        alpha_list=balanced_parens(i)
        beta_list=balanced_parens(n-1-i)
        for alpha in alpha_list:
            for beta in beta_list:
                l.append(generate(alpha,beta))
    memoize[n]=l
    return l
    