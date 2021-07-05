n=int(input())
even=0
odd=0
while(n):
    r=n%10
    if(r%2==0):
        even=even*10+r
    if(r%2 != 0):
        odd=odd*10+r
    n=n//10    
print("even nubers are:",even,"and its square is:",even*even)    
print("odd numbers are:",odd,"and its square is:",odd*odd)        
  
    
