def list_vers9_recurs1(n):
    if n==9:return [9]
    elif n<9:return 'error'
    else:
        inv=(n%10)*10+n//10
        return [n,inv]+list_vers9_recurs1(abs(n-inv))
    
n=63
print(list_vers9_recurs1(n))