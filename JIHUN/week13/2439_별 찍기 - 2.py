num = int(input())
count=1
for i in range(num):
    print(" "*(num-count) + "*"*count)
    count+=1