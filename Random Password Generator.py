#program to create a Random Password Generator
import random
import string
print("Hlo! Welcome To Our Random Password Generator")
def Generate():
    
    length=int(input("Enter the Length of Password you want:"))
    if length>=12:
        lower_data=string.ascii_lowercase
        upper_data=string.ascii_uppercase
        digit_data=string.digits
        symbols_data=string.punctuation
        combination=lower_data+upper_data+digit_data+symbols_data
        key=random.sample(combination,length)
        password="".join(key)
        print(password)
        Generate()
        
    else:
        print("Password Length Should Atlest 12 Characters")
        Generate()
Generate()
