def arb_args(*args):
    for arg in args:
        print(arg)

def inner_func(a,b):
    def divide():
        return a/b
    
    def multiply():
        return a * b
    
    results = divide() + multiply()
    print(results)

def lunch_lady(name, lunch="Mystery Meat"):
    print(name, lunch)

def sum_n_product(a,b):
    return a+b, a*b

alias_arb_args = arb_args

def arb_mean(*args):
    total = 0
    for a in args:
        total += a
    print(a/len(args))

def arb_longest_string(*args):
    long = 0
    longest = ""
    for a in args:
        if len(a) >long:
            long = len(a)
            longest = a
    return longest


arb_args(1, 2, 3, "hello")  
inner_func(3, 4)           
lunch_lady("Benny Bill", "Pizza")      
lunch_lady("Lebron James")              
sum_result, product_result = sum_n_product(3, 4)
print(sum_result, product_result)    
alias_arb_args("a", "b", "c")       
arb_mean(1, 2, 3, 4, 5)              
print(arb_longest_string("apple", "banana", "cherry"))  