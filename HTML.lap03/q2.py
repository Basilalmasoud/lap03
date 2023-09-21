mlist = []
i = 0
while i < 5:
    print("please enter 10 numbers")
    mlist.append(int(input("enter the number ")))
    i = i + 1
    print(mlist)

max_number = mlist[0]

for number in mlist:
    if number > max_number:
        max_number = number

print("The largest number in the list is:", max_number)
