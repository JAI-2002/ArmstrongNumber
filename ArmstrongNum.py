# Take input from the user.
n=int(input("Enter any number: "))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))

# Using if statement.
if(sum(b)==n):
    print("The number is an armstrong number. ")
else:
    print("The number isn't an arsmtrong number. ")
