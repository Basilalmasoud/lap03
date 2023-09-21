i = 0
my_dictionary={}
endstatment = True
while endstatment is True:
    print("please enter employee name and salary")
    emp = input("name")
    sal = input("salary")
    my_dictionary [emp]= sal
    i = i+1
    ansewr = input("do you want to continue enter y/n")
    if ansewr == "n":
        endstatment = False
print(i)
print(my_dictionary)