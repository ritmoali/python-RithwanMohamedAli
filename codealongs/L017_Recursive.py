def main():
    ...

def func_a():
    print("start of func_a()")
    func_a()

    print("End of main()")

def fun_a():
    print("End of func_a()")

def print_hello(n):
    for i in range(n):
          print("Hello")
def print_hello_recursive(n):
    print("Hello")
    if n > 1: print_hello_recursive(n-1)
    return
print_hello_recursive(4)
#main()

    
