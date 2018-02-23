a=input("enter the year:")
if ((a%400==0 and a%100==0) or (a%4==0)):
    print ( "is a leap year")
else:
    print ("is not leap year")
