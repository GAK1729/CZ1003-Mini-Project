from tkinter import *
from pramurta import *
#from pramurta import canteen 
from aditya import *
from gaurav import *






while True:

    print("\n\nMENU:\n1. Change canteen details\n2. Start Application\n3. Quit")
    ch =int(input("\nEnter a choice(1/2/3): "))

    if ch == 1:
        canteen_function()

    elif ch == 2:
        root = Tk()
        login_page(root)
        root.mainloop()

    elif ch ==3:
        break

    else:
        print("Invalid Input.")








