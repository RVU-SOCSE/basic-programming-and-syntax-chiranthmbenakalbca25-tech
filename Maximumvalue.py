
#prog to find Maximum value
#USN :1RUA25BCA0023
#Name:Chiranth M Benakal


a = int(input("Enter the a value"))
b = int(input("Enter the b value"))
c = int(input("Enter the c value"))

if a<b and b>c:
    print("b is the largest number")
elif a<c and c>b:
    print("c is the largest number")
else:
    print("a is the largest number")
