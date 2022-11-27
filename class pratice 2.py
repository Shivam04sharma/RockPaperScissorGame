#rock vs paper- paper wins
#rock vs scissor- rock wins
#paper vs scissor- scissor wins
while True:
    print("#"*60)
    print("# It's a 5 round game:")
    print("-"*30)
    print('''# Press:
> S or s to start
> E or e to start''')
    print("-"*30)
    z=input("Enter the command: ")
    if z in "Ss":
        print("*"*60)
        import random
        u=0
        p=0
        d=0
        a=["rock","paper","scissor"]
        for i in range(1,6):
            print("*"*60)
            b=random.choice(a)
            print('''#rock vs paper- paper wins
#rock vs scissor- rock wins
#paper vs scissor- scissor wins''')
            print("-"*35)
            print('''@ Enter:
> 1 for rock
> 2 for scissor
>3 for paper''')
            print("-"*25)
            c=input("Enter the number: ")
            print("-"*25)
            print("# Randomly generated from pc:",b)
            if c=="1":
                print("# Your entry: rock")
            elif c=="2":
                print("# Your entry: scissor")
            elif c=="3":
                print("# Your entry: paper")
            else:
                print("Invalid Entry")
            print("-"*60)
            if c=="1":
                if b=="rock":
                    print(">>> Draw...")
                    d=d+1
                elif b=="paper":
                    print(">>> You lossed...")
                    p=p+1
                else:
                    print(">>> You won...")
                    u=u+1
            elif c=="2":
                if b=="rock":
                    print(">>> You lossed...")
                    p=p+1
                elif b=="paper":
                    print(">>> You won...")
                    u=u+1
                else:
                    print(">>> Draw...")
                    d=d+1
            elif c=="3":
                if b=="rock":
                    print(">>> You won...")
                    u=u+1
                elif b=="paper":
                    print(">>> Draw...")
                    d=d+1
                else:
                    print(">>> You lossed...")
                    p=p+1
        print("*"*60)
        print(" "*14,"-"*5,"Summary","-"*5," "*14)
        print()
        print("# you won:",u)
        print("# pc won:",p)
        print("# draw:",d)
        print()
        if u==p:
            print(">>> Match Drawn...")
        elif u>p:
            print(">>> You Won...")
        else:
            print(">>> You Lossed...")
        print()
        print("#"*60)
    elif z in "Ee":
        print("#"*60)
        break
    else:
        print("-"*60)
        print("! Invalid Input, Try Again...")