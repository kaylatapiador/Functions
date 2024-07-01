def name_args(**kwargs):
    for k in kwargs.keys():
        print(f"{k}:{kwargs[k]}")

def all_true(iter):
    return all(iter)

def one_true(iter):
    return any(iter)

def recursive_factorial(n):
    if n<=1:
        return 1
    else:
        return n*recursive_factorial(n-1)

def recursive_deduplicate(str,i=0):
    if len(str) <=1 or i==len(str)-1:
        return str
    else:
        return recursive_deduplicate(str,i+1)


def recursive_reverse(str, i=0):
    if len(str)==0:
        return ""
    elif i ==len(str)-1:
        return str[0]
    else:
        return str[-1-i] + recursive_reverse(str,i+1)

name_args(a=1, b=2, c=3) 
print(all_true([1, 2, 3, 4]))  
print(all_true([1, 0, 3, 4])) 
print(one_true([0, 0, 0, 1]))  
print(one_true([0, 0, 0, 0])) 
print(recursive_factorial(5))  
print(recursive_deduplicate("AABBCCDD"))  
print(recursive_reverse("hello"))  