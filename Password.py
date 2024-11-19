#MIT License
#Copyright (c) <2024> The Tilings 

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

import re

print("Password meets the requirements to be considered secure")
password = input("Enter your password:")

#The following allows us to set some boolean values that we will change whether the password meets the requirement or not.
lenght = False
capital_letter = True
lowercase_letters = True
number = True
special = True

if  8 <= len(password):
    lenght = True
    if not re.search(r"[A-Z]", password): #Find capital letters
        capital_letter = False
        print("Password must contain at least one capital letter.")
    if not re.search(r"[a-z]", password): #Find lowercase letters
        lowercase_letters = False
        print("Password must contain at least one lowercase letter.")
    if not re.search(r"\d", password): #Find some number
        number = False
        print("The password must contain at least one number.")
    if not re.search(r"[!@#\$%\^&\*\(\),\.\?\\:\{\}\|<>\[\]/]", password): #Search for special characters
        special = False
        print("The password must contain at least one special character.")
        
else:
    print("The password is too short. It must be at least 8 characters.")
    
#It will be displayed when all the above characteristics are true
if lenght and capital_letter and lowercase_letters and number and special == True: 
    print("The password is secure")
