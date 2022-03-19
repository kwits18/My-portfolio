from Mylib import libfunc

while True:
    try:
        minRange=int(input("Please enter minimum range: "))
        maxRange=int(input("Please enter maximum range: "))
        first=int(input("Please enter your first number here: "))
        second=int(input("Please enter your second number here: "))
        myobj = libfunc(0)
        expression=str(first) + "," + str(second) + ",/"
        menu=["1: Add", "2: Subtract", "3: Multiply", "4: Divide/scalc", "5: All In One function", "6: Exit"]
        for ans in menu:
            print(ans)

        menuinp=int(input("please choose number from list: "))

    except ValueError:
        print("Please enter a number, not a letter")
      
    if myobj.isInRange(minRange, maxRange, first) and myobj.isInRange(minRange, maxRange, second):
        print("")
    else:
        print("numbers are outside of range values")
        break
    try:

        print("")
        if menuinp==1:
            print("When added, you get:", first, "+", second, "=", myobj.add(first, second))
        if menuinp==2:
            print("When subtracted, you get:", first, "-", second, "=", myobj.subtract(first, second))
        if menuinp==3:
            print("when multiplied, you get:", first, "*", second, "=", myobj.multiply(first, second))
        
    except ZeroDivisionError:
        print("cannot divide by zero")
    else:
        if menuinp==4:
            print("When divided, you get:", first, "/", second, "=", myobj.scalc(expression))

        if menuinp==5:
            res=myobj.allinone(first, second)
            print(first, "+", second, "=", res['add'])
            print(first, "-", second, "=", res['subtract'])
            print(first, "*", second, "=", res['multiply'])
            print(first, "/", second, "=", res['divide/scalc'])
            

        if menuinp==6:
            break
               
        print("")
    tryAgain=input("Do you want to restart and try again? (y/n):")
    if (tryAgain == "y"):
        continue
    else:
        break
#below is the file read and write menu
intro=["1: write a file with all included inputs", "2: read a file", "3: make an all in one file of your results"]
for ans in intro:
    print(ans)

introinp=int(input("please choose number from list: "))

#option 1 makes a file with all inputs included    
if introinp==1:
    with open("write.txt", "w") as make_file:
        print("Your range inputs: ", minRange, ",", maxRange, file=make_file)
        print("\nYour integer inputs:", first, ",", second, file=make_file)
        make_file.close()
        print("File write.txt created") 

#option 2 reads the file from the input        
if introinp==2:
    readfile=input("please enter file name. for example: write.txt : ")
    read_file=open(readfile, "r")
    print()
    print(read_file.read())
    read_file.close()

#option 3 makes a file with the all in one function results
if introinp==3:
    with open("write.txt", "w") as make_file:
        res=myobj.allinone(first, second)
        print("added: ", first, "+", second, "=", res['add'], file=make_file)
        print("subtracted: ", first, "-", second, "=", res['subtract'],file=make_file )
        print("multiplied: ", first, "*", second, "=", res['multiply'],file=make_file )
        print("divided: ", first, "/", second, "=", res['divide/scalc'],file=make_file )
        make_file.close()
        print("File write.txt created")

print("")
print("Thank you for using the calculator I made")
