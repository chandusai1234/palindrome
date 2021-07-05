n=int(input())
t=n
rev=0
while(n):
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)
if(t==rev):
    print("it is a palindrome")
else:
    print("it is not a palindrome")
    

