# Using memoization to store previously computed Fibonacci numbers
# this is on another branch
fibonacci_cache = {}

def recur_fibo(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n <= 1:
        fibonacci_cache[n] = n
    else:
        fibonacci_cache[n] = recur_fibo(n - 1) + recur_fibo(n - 2)

    return fibonacci_cache[n]

def print_fibonacci_sequence(nterms):
    if nterms <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(nterms):
            print(recur_fibo(i), end=" ")

if __name__ == "__main__":
    nterms = 10
    print_fibonacci_sequence(nterms)
