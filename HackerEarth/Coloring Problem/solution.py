from collections import defaultdict
t=int(raw_input())
while t>0:
    n=int(raw_input())
    e=int(raw_input())
    adjMat=defaultdict(lambda :[])
    maxDegree=0
    base=None
    for i in xrange(e):
        a,b=map(int,raw_input().split(' '))
        adjMat[a].append(b)
        adjMat[b].append(a)
        base=a
    visited=[base]
    colMap={base:True}
    parent={base:None}
    toBeVisited=adjMat[base]
    for i in toBeVisited:
        parent[i]=base
    notBiColor = False
    while toBeVisited:
        temp=[]
        for i in toBeVisited:
            parentColor = colMap[parent[i]]
            currentColor = not parentColor
            for j in adjMat[i]:
                if j not in visited:
                    if j not in toBeVisited:#cycle detection
                        parent[j]=i
                        temp.append(j)
                else:
                    if currentColor == colMap[j]:
                        notBiColor=True
                        break
            if notBiColor:
                break
            colMap[i]=currentColor   
            visited.append(i)
        if notBiColor:
            break     
        toBeVisited=temp
    if notBiColor:
        print('NOT BICOLORABLE.')
    else:
        print('BICOLORABLE.')
    t-=1
