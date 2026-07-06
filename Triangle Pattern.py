Given an integer n, print the Half Diamond Star Pattern using * characters as shown in the examples.

n = int(input())

for i in range(1, n + 1):
    print("* " * i)

for i in range(n - 1, 0, -1):
    print("* " * i)
