def sum(n):
    return n*(n+1)/2

sum(5)
print(sum(5))

def array(a):
    sum=0
    for i in a:
        sum=sum+i
    return sum
a=[1,2,3,4,5,6,7,8,9,10]
array(a)
print(array(a))