while(1):
    print("press 1 for celius ")
    print("press 2 for cm to inches ")
    print("press 3 for time ")
    print("press 4 for exit ")
    ch=int(input("Enter your choice: "))

    if(ch==1):
        c=int(input("Enter celius: "))
        f=(9/5)*(c-32)
        print("temperature: ",f)
    elif(ch==2):
        cm=int(input("Enter cm: "))
        inches=cm/2.54
        print("inches: ",inches)
    elif(ch==3):
        s=int(input("enter seconds: "))
        hrs=s//3600
        m=(s%3600)//60
        se=(s%3600)%60
        print("hours: ",hrs," minutes: ",m," seconds: ",se)
    elif(ch==4):
        break
    else:
        print("invaild input...")        