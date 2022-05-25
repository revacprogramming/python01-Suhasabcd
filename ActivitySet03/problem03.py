def isPalindrome(s):
    return s == s[::-1]
for _ in range(int(input())):
    y=int(input())
    x=input()
    for i in range(y):
        for j in range(1,y):
            if(len(x[i:j+1])>2):
                if isPalindrome(x[i:j+1]):
                    print(i+1,x[i:j+1])
                    
            
                

           
                

