def catchRest(*args):
    print(list(args))
catchRest(1, 3, 5)

def f2(*args):
    for x in args:
        arg_type = type(x)
        print(f"Type: {arg_type}")
        print(f"Value: {x}")
f2(1, 'Marcus', {'field': 'value'})
