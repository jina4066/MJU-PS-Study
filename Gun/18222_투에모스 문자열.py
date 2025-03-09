# Sol1.
print(bin(int(input())-1).count('1')%2)

# Sol2.
n = int(input())

def divide_and_conquer(n):
    if n == 0:
        return 0
    if n % 2:
        return 1 - divide_and_conquer(n // 2)
    else:
        return divide_and_conquer(n // 2)

print(divide_and_conquer(n - 1))

