def fact(n):
     N = range(1, n+1)
     print N
     for i in range(0, n):
         if N[i]>=1:
            N[i] = N[i-1]*N[i]
         else:
             return 1 
	
     return N

print fact(5)


def fact2(n):
    if n <= 0:
	return 1
    else:
	return n*fact2(n-1)
print fact2(5)


def fact3(n):
    N = range(1, n+1)
    print N
    answer = 1
    for num in N:
	answer = answer*num
    return answer

print fact3(5)
