#Given a list of numbers and a number k, return whether any two numbers from
# the list add up to k.
ls=list(map(int, input().strip().split()))
k= int(input())
ls.sort()
for i in range(len(ls)):
    for j in range(len(ls)-1):
        if ls[i]+ls[j]==k:
            print(ls[i],ls[j])
        pass
#print(ls)