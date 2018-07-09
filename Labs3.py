# ====my imports======
import math
import datetime


#Programming Languages and their inventors________________
#=========================================================   
def languages():
    pro_lang = {"Java": "James Gosling", "C": "Dennis Ritchie", 
                "C++": "Bjarne Stroustrup", "Python": "Guido van Rossum",
                "PHP": "Rasmus Lerdorf"}

    lang = input("Enter the name of the Language from among these list(Java, C, C++, Python, PHP) ")
    lang = lang.lower()
    
    if lang == "java":
        return pro_lang["Java"]
        
    elif lang == "c":
      return pro_lang["C"]

    elif lang == "c++":
      return pro_lang["C++"]

    elif lang == "python":
      return pro_lang["Python"]

    elif lang == "php":
      return pro_lang["PHP"]
      
    else:
        print("Your Language does not exist in the list")


        

#converting 32 degress to radian__________________________
#=========================================================
def degreesToRadian():
    pi = math.pi
    degree = 32
    radian = degree * (pi/180)
    print("32 degrees = " + str(radian) + " radian")

#Surface Area and Volume of a spere_______________________
#=========================================================
def sphere():
    pi = math.pi
    r = int(input("Enter radius of a sphere "))
    area = 4 * pi *(r*r)
    rCube = math.pow(r, 3)
    volume = 4/3*(pi*rCube)

    print("Area of the sphere = "+ str(area) )
    print("Volume of the sphere = "+ str(volume) )

#Displaying Current date and time_________________________
#=========================================================
def currentDateTime():
    now = datetime.datetime.now()
    print (now)

#Spliting sentences into words____________________________
#=========================================================
def sentenceSplit():
    text = "This is my sentence to be splitted"
    text = text.split()

    print(text)


#Joining words to form a sentence_________________________
#=========================================================    
def joinWords():
    c=[['oh', 'yea', 'makes', 'sense'],
       ['When', 'I', 'become', 'expert', 'in', 'java,', 'I', 'will', 'build'],
       ['old', 'men', 'finally', 'date', 'sarcasmsun', 'mar', 'ist'],
       ['sarinas', 'chanted', 'peacefully', 'deny', 'hypocrisysat', 'mar', 'ist']]

    for arr in c:
        print(" ".join(arr))
    #print [ ' '.join(i) for i in c]   
    


#Asks for user age and return_____________________________
#=========================================================   
def get_age():
	age = int(input("What is your age "))
	return age

#Asks for user name and return____________________________
#=========================================================
def get_name():
	name = (input("What is your name "))
	return name

#Simple di-num calculator_________________________________
#=========================================================
def calculate(operator, num1, num2):

    operator = operator.lower()
     
    if operator == "add":
        res = num1 + num2
        print(res)
    elif operator == "subtract":
        mul = num1 - num2
        print(res)
    elif operator == "multiply":
        res = num1 * num2
        print(res)
    elif operator == "divide":
        res = num1 / num2
        print(res)
    else:
        print("Your command does not exist")

#while loop_______________________________________________
#=========================================================
def whileLoop():   
    i = 14
    while(i < 20):
        
        i = i + 2
        
#For loop_________________________________________________
#=========================================================
def forLoop():
    for i in range(12,20):
        print (i)

#Print 4 stars on a row four times________________________
#=========================================================
def print_4Stars():
    for i in range(0, 4):
        for j in range(0, 4):
            print("*",end="")
        print()
















        

