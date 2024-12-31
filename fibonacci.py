def timedecor(arg):
    def inner():
        import time
        IT=time.time()
        arg()
        FT=time.time()
        print(FT-IT)
    return inner

def fibo():
    fn=int(input('enter first number'))
    sn=int(input('enter second number'))
    n=int(input('how many numbers'))
    if n==1:
        print(fn)
    elif n==2:
        print(sn)
    else:
        print(fn,sn)
        for i in range(n-2):
            th=fn+sn
            print(th)
            fn,sn=sn,th
            
fibo()    
