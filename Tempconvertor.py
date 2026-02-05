
#prog to find temperature
#USN :1RUA25BCA0023
#Name:Chiranth M Benakal



print("1.celcius to fahrenheit conversion")
print("2.fahrenheit to celcius conversion")

choice = int(input("Enter your choice"))
temp = float(input("Enter the temperature"))

match choice:
    case 1:
        fahrenheit = (temp * 9/5)+32
        print("the fahrenheit temperature is",fahrenheit)
    case 2:
        celcius = (temp - 32)*5/9
        print("the celcius temperature is ",celcius)
    case _:
        print("Invalid")
