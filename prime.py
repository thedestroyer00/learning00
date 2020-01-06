# check the number is prime or not: 

def prime(a):
    isprime = 0
    for i in range(2,a):
        if(a%i == 0):
            isprime += 1
            
    if(isprime == 0):
        print(a, "is a prime number")
        
    else:
        print(a, "is not a prime number")
    

n = int(input("Enter the number to be checked :"))
prime(n)
