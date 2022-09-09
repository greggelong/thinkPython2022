def do_twice(f,v):
    f(v)
    f(v)

def print_one(x):
    print(x)

def print_twice(x):
    print(x)
    print(x)    

def do_four(f,v):
    do_twice(f,v)
    do_twice(f,v)

do_twice(print_twice,"spam")

do_four(print_one,"greg")