from math import pi
def factorial():
    if x == 0 or x ==1:
        return 1
    else:
        return x * factorial(x-1)
    

    
step=lambda x,i: ((-1)**i)*(x**(2*i+1)) /factorial(2*i+1)
def sine_x(x,n):
    x=float(input("Enter x in degrees to be convert into radian "))
    
    n=int(input("Enter n for function"))
    x=x*pi/180
    total=0
    for i in range(n+1):
        total +=step(x,i)
    return total
    
    
def harmonic_sum(n):
    """ This functşon prints out the harmonic summation"""
    global total
    if n==1:
        return 1
    harmonic_sum(n-1)
    total+=1/n
    
    
       
