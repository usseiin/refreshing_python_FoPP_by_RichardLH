print("Help! My Computer doesn't work!")

print("Does the computer make any sounds (fans, etc)")
choice = input("or show any lights? (y/n): ")

if choice == "n" or "N":
    choice = input("Is it plugged in? (y/n): ")
    if choice == "n" or "N":
        print("Plug it in, if the problem persist, ")
        print("please run this program  again.")
    else:
        choice = input("Is the switch in the \"n\" position? (y/n): ")
        if choice == "n" or "N":
            print("Turn it on, if the problem persists, ")
            print('please run this program again. ')
        else:
            choice = input("Does the computer have a fuse? (y/n): ")
            if choice == "n" or "N":
                choice = input("Is the outlet OK? (y/n): ")
                if choice == "n" or "N":
                    print("Check the outlet's circuit ")
                    print("breaker or fuse, Move to a")
                    print("new outlet, if necessary. ")
                    print("If the problem persists. ")
                    print("please run this program again.")
                else: 
                    print("Please consult a service technician")
            else:
                print("Check the fuse, Replace if ")
                print("necessary. If the problem ")
                print("persists, then ")
                print("please run this program again.")
else:
    print("Please consult a service technician.")
