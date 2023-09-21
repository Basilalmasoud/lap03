num = int(input("enter a number that you would like to see its multiplication table(to 10)"))
i = 1
while i <= 10:
    strNum = str(num)
    strI = str(i)
    print(strI + " X " + strNum + " = " + (str(i * num)))
    i = i + 1
