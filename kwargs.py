# **kwargs = parameter that will pack all arguments into a dictionary; useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
    print("hello" + " " + kwargs['first'] + " " + kwargs['last'])


hello(first = "Tina", middle = 'args', last = 'mina')