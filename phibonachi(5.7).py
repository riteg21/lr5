def fibonacci(n):
   
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    else:
        list_fib = [1, 1]
        while len(list_fib) < n:
            next_fib = list_fib[-1] + list_fib[-2]
            list_fib.append(next_fib)
        return list_fib


fibonacci_sequence = fibonacci(40)


print(fibonacci_sequence)