def combined_arg(*args, **kwargs):
    print(args)
    print(kwargs)


combined_arg(10,20,30,40,k=2,l=3,d=45)    