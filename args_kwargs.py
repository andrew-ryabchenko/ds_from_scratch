def f(*args, **kwargs):
    print(args)
    print(kwargs)


f(1,2,3,4,5,key=5,count=3)