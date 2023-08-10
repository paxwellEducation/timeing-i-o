import timeit
import os

# Prepare a large amount of data
data = 'x' * 10**9  # 1GB of data

# I/O-bound operation: Writing to a file
start = timeit.default_timer()
with open('largefile.txt', 'w') as f:
    f.write(data)
end = timeit.default_timer()
print(f"Time taken for I/O-bound operation: {end - start} seconds")

# Clean up the large file
os.remove('largefile.txt')

# CPU-bound operation: Calculating a large Fibonacci number
fibb = [0] * 1000
def fib(n):
    if fibb[n] != 0:
        return fibb[n]
    if n == 0:
        fibb[n] = 0
        return 0
    if n == 1:
        fibb[n] = 1
        return 1
    fibb[n] = fib(n-1) + fib(n-2)
    return fibb[n]

start = timeit.default_timer()
fib(200)
end = timeit.default_timer()
print(f"Time taken for CPU-bound operation: {end - start} seconds")
