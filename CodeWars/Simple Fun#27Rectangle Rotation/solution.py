import math
def rectangle_rotation(a, b):
    theta=math.atan(b/a)*(180/math.pi)
    hypotenuse=math.sqrt((a/2)**2 + (b/2)**2)
    delta=(45-theta) * (math.pi/180)
    ref_pnt1= hypotenuse * math.cos(delta)
    ref_pnt2= hypotenuse * math.sin(delta)
    A=(ref_pnt2, ref_pnt1)
    B=(ref_pnt1, ref_pnt2)
    C=(-ref_pnt2,-ref_pnt1)
    D=(-ref_pnt1,-ref_pnt2)
    y_lb=math.floor(C[1])+1 # lower bound for y axis
    y_ub=math.floor(A[1]) # upper bound for y axis
    eqn_1=lambda y: A[0] + A[1] - y  
    eqn_2=lambda y: y - B[1] + B[0]
    eqn_3=lambda y: C[0] + C[1] -y
    eqn_4=lambda y: y - D[1] + D[0]
    total_points=0
    for i in range(y_lb,y_ub+1):
        if i < B[1]:
            x_crd=eqn_2(i)
        else:
            x_crd=eqn_1(i)
        
        if i < D[1]:
            mx_crd=eqn_3(i)
        else:
            mx_crd=eqn_4(i)
        
        points=math.floor(x_crd)
        points -= math.floor(mx_crd)
        total_points+=points
    return total_points