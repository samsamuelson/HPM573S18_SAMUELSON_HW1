# iterative, sum is plus i, then equal to i
def sum_it(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print sum_it(100)

# recursive, looping/refers back, double equals sign indicates choice, recursive less intensive computationally
def sum_rec(n):
    if n==1:
        return 1
    else:
        return n + sum_rec(n-1)
print(sum_rec(100))
