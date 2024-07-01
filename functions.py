def max_num(a,b,c):
    return max([a,b,c])

def multi_list(list):
    if(len(list)==0):
        return 0
    prod = list[0]

    if len(list)>1:
        for i in list[1:]:
            prod = prod*i
    return prod

def rev_string(string):
    return string[::-1]

def num_within(x,a,b):
    return x in range(a,b+1)

def pascal(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    for row in triangle:
        print(row)


print(max_num(1, 2, 3))        
print(multi_list([1, 2, 3, 4]))
print(rev_string("hello"))     
print(num_within(3, 2, 4))     
print(num_within(3, 1, 3))     
print(num_within(10, 2, 5))
pascal(5)