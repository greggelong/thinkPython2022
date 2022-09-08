def print_twice(x):
    print(x)
    print(x) 


def do_twice(f,v):
    f(v)
    f(v)

def print_grid2():
    edge =(2*"+ - - - - "+"+")
    middle = ("|         |         |")
    print(edge)
    do_twice(print_twice,middle)
    print(edge)
    do_twice(print_twice,middle)
    print(edge)
    

print_grid2()
    