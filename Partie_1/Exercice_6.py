#  Fonction qui calcule la somme des termes n à n+m dans la suite de Fibonacci
def sum_fibonacci(n, m):
    fib = [0, 1]
    for i in range(2, n+m):
        fib.append(fib[i-1] + fib[i-2])
    return (sum(fib[n:n+m]))

print(sum_fibonacci(3, 5))

