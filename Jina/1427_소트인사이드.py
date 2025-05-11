N = int(input())

num_list = list(map(int, str(N)))
num_list.sort(reverse=True)

for num in num_list:
    print(num, end="")