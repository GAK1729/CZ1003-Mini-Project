from tkinter import *
from tkinter import messagebox
import shelve

from pramurta import *
from pramurta import canteen 
from gaurav import *


      
#----------------------------------------------------------------------------------------
#                                       USER INTERFACE
#----------------------------------------------------------------------------------------




    #-------------------------------------------------------------------------------------
    #               LOGIN PAGE
    #-------------------------------------------------------------------------------------


def login_page(root):

    for widget in root.grid_slaves():
        widget.grid_remove()


    root.title("CANTEEN RECOMMENDATION")
    Label(root, justify=CENTER,text="Welcome to NTU CANTEEN RECOMMENDATION SYSTEM",font=("roman",30),bg = "lightblue").grid(row=0,column=0,columnspan=6,sticky=N+S+W+E)
    Label(root, justify =CENTER, text= "LOGIN PAGE", font =("Arial Rounded MT Bold", 30), bg="cyan3").grid(row =1, column = 0, columnspan = 6, sticky=N+S+E+W)
    Label(root, bg ="cyan").grid(row=2, column=0, rowspan=5, columnspan=6, sticky=N+S+W+E)


     # Grid sepcifications for displaying widgets

    root.grid_columnconfigure(0,weight =1)
    root.grid_columnconfigure(1,weight =1)
    root.grid_columnconfigure(2,weight =1)
    root.grid_columnconfigure(3,weight =1)
    root.grid_columnconfigure(4,weight =1)
    root.grid_columnconfigure(5,weight =1)



    root.grid_rowconfigure(0,weight =3)
    root.grid_rowconfigure(1,weight =2)
    root.grid_rowconfigure(2,weight =1) 
    root.grid_rowconfigure(3,weight =1)
    root.grid_rowconfigure(4,weight =1)
    root.grid_rowconfigure(5,weight =1)
    root.grid_rowconfigure(6,weight =1)


    username = StringVar() #To store username

    Label(root, text="User Name", bg="aquamarine", font= 20, relief = "ridge").grid(row=4,column=2,sticky=N+S+E+W)
    Entry(root, bd =5, textvariable = username).grid(row=4,column=3)


    password = StringVar() # To store password

    Label(root, text="Password", bg="aquamarine", font =20 , relief = "ridge").grid(row=5,column=2,sticky=N+S+E+W)
    Entry(root, bd =5,textvariable = password).grid(row=5,column=3)


    def hide_pass(n): # to show * while typing password
        if n == 1:
             Entry(root, bd =5,textvariable = password).grid(row=5,column=3)
        elif n == 2:
            Entry(root, bd =5,show="*" ,textvariable = password).grid(row=5,column=3)

    
    account_var = IntVar() #1:New Account, 2:Existing Account
    Radiobutton(root,text="NEW ACCOUNT", font = 30, bg = "green2",padx=30,pady=30,relief ="ridge",variable = account_var, value = 1,command = lambda: hide_pass(1)).grid(row=2, column=2)
    Radiobutton(root, text = "EXISTING USER", font = 30 , bg="yellow",padx=30,pady=30,relief = "ridge",variable = account_var, value = 2, command = lambda: hide_pass(2)).grid(row=2, column=3)
 

 

    def press_enter(username, password, account_var):                               #Command to run on pressing enter
                                                                                    #Checks if all fields are filled
                                                                                    #Creates new account if valid credentials
                                                                        
        if username == "" or password == "" or account_var == 0:
            messagebox.showerror("ERROR","Please fill and select all the fields")
            
        elif account_var == 1:              
            ret = create_new_account(username,password, login_file, ret_login_file)  # ret =1: Correct Credentials, 2:Existing Username, 3:Weak Password
            if ret ==1:
                messagebox.showinfo("SUCCESS","NEW USER ACCOUNT CREATED")
            elif ret == 2:
                messagebox.showerror("Error","That User name has already been taken. Please try again.")
            elif ret == 3:
                messagebox.showerror("Error","Your passowrd should have at least 6 characters including atleast 1 number, 1 Lowercase letter, and 1 Uppercase letter.")
                
                
           
        elif account_var == 2:

            var = check_username_password(username, password, ret_login_file)  # var =1:Correct Username & Password, 2:Invalid Username, 3:Invalid Password
                                                                               # if correct credentials, directs to userpage
            if var == 1:
                user_page(root, username, get_user_location, suggest_canteens, particular_canteen)
            elif var == 2:
                messagebox.showerror("ERROR","Invalid Username. Please try again")
            elif var == 3:
                messagebox.showerror("ERROR","Invalid Password. Please try again")
    



    Button(root, text="ENTER",pady=10,padx=50,bg="green3", command = lambda: press_enter(username.get(), password.get(), account_var.get())).grid(row=6,column=2, columnspan=2)





        #--------------------------------------------------------------------------------------
        #                       USER PAGE
        #--------------------------------------------------------------------------------------

def user_page(root, username, get_user_location, suggest_canteens, particular_canteen):

    for widget in root.grid_slaves():
        widget.grid_remove()

      
    root.title("CANTEEN RECOMMENDATION")
    Label(root, justify=CENTER, text="Welcome   "+username, font =("Arial Rounded MT Bold", 30), bg="cyan3").grid(row =0, column = 0, columnspan = 5, sticky=N+S+E+W)
    Label(root, bg="lightsalmon").grid(row =0, column = 5,sticky=N+S+W+E)
    Button(root, text="LOG OUT",bg="RED",padx=10,pady=10,relief= "ridge",font=("Arial Rounded MT Bold",20),command = lambda: login_page(root)).grid(row=0,column=5)

    #Logout button directs to login page

        
    Label(root, justify=CENTER, text= "STEP 1: ENTER YOUR LOCATION", font =("Elephant"), bg="green3").grid(row=1, column=0, rowspan=2,columnspan=2,sticky=N+S+E+W)
    Label(root, justify=CENTER, text= "STEP 2: ENTER YOUR PREFERENCE", font =("Elephant"), bg="yellow").grid(row=3, column=0, rowspan=2,columnspan=2, sticky=N+S+E+W)
    Label(root, justify=CENTER, text= "STEP 3: SELECT A CANTEEN", font =("Elephant"), bg="lightskyblue1").grid(row=5, column=0, rowspan=3,columnspan=2, sticky=N+S+E+W)


    Label(root, bg="green2").grid(row=1,column=2, rowspan=2, columnspan=2, sticky=N+S+E+W)
    Label(root, bg="yellow2").grid(row=3,column=2,rowspan=2,  columnspan=2, sticky=N+S+E+W)
    Label(root, bg="lightskyblue").grid(row=5,column=2,rowspan=3,  columnspan=2, sticky=N+S+E+W)


    Label(root, justify=LEFT, text="Click on the following button and click on your current location on the map",font=("Broadway",15),bg="green2").grid(row=1,column=2, columnspan=2, sticky=N+S+E+W)
    Label(root, justify=LEFT, text="Enter a keyword in the following box(Eg: Veg, Continental, Burger, Waffle)",font=("Broadway",15),bg="yellow2").grid(row=3,column=2, columnspan=2, sticky=N+S+E+W)
    

    data=["",""]    # To store user's location and preference
                    #Index 0: User's Current Location. Index 1: List of canteen's with user's preference


    Button(root, text="MY LOCATION",padx=5,pady=5,relief= "ridge",font=("Arial Rounded MT Bold",20),command = lambda: enter_location(pref_but, data)).grid(row=2,column=2, columnspan=2)


    preference = StringVar()
    Entry(root, bd =5, font=20,textvariable = preference).grid(row=4,column=2)

    can_dist={}     # Dictionary to store canteens sorted by distance
    
    pref_but=Button(root, text="ENTER",pady=5,padx=5, relief ="ridge",font=("Arial Rounded MT Bold",20), state= DISABLED, command = lambda: enter_preference(preference.get(), data))
    pref_but.grid(row=4,column=3)


    
    # Grid sepcifications for displaying widgets                                                                                                                                                            
     
    root.grid_columnconfigure(0,weight =1)
    root.grid_columnconfigure(1,weight =1)
    root.grid_columnconfigure(2,weight =1)
    root.grid_columnconfigure(3,weight =1)
    root.grid_columnconfigure(4,weight =1)
    root.grid_columnconfigure(5,weight =1)
    



    root.grid_rowconfigure(0,weight =4)
    root.grid_rowconfigure(1,weight =1)
    root.grid_rowconfigure(2,weight =1) 
    root.grid_rowconfigure(3,weight =1)
    root.grid_rowconfigure(4,weight =1)
    root.grid_rowconfigure(5,weight =1)
    root.grid_rowconfigure(6,weight =1)
    root.grid_rowconfigure(7,weight =1)
    
        


    

        
#------------------------------------------------------------------------------------
#       FUNCTIONS TO BE EXECUTED ON PRESSING BUTTONS
#------------------------------------------------------------------------------------



    def enter_location(pref_but, data):           #Function to run on pressing my location\
                                                  #Gets user location and appends data
                                                  #Activates the Enter Button        
        data[0] = ""
        data[0]=(get_user_location())
        pref_but.configure(state=ACTIVE)
            

       
    def enter_preference(preference, data):     #Funtion to run on pressing enter
                                                #Gets Canteens based on user's preferences and appends data
                                                #Displays list of canteens and distances 
        data[1] = ""
        data[1] = (suggest_canteens(preference))
               
        can_dist = sorted_distances(data[0], data[1])  # Stores canteen names sorted by distance
        Label(root, bg="lightskyblue").grid(row=5,column=2,rowspan=3,  columnspan=2, sticky=N+S+E+W)
        Label(root, justify=LEFT, text="Based on preference, following is the list of canteens\nDouble click a canteen name to view details.",font=("Broadway",15), bg="lightskyblue").grid(row=5,column=2, columnspan=2, sticky=N+S+E+W)
        Label(root, justify = CENTER, text = "Canteen Name",padx=10,relief="ridge", font =10).grid(row=6, column = 2, sticky=N+S+E+W)
        Label(root, justify = CENTER, text = "Distance from your current location(in meters)", relief="ridge",font =10).grid(row =6, column = 3, sticky =N+S+W+E)

        listbox_can = Listbox(root, font=10, height = 7)
        listbox_dist = Listbox(root, font =10, height = 7)
            
        for i,j in can_dist.items():
            listbox_can.insert(END,str(i)+".   "+j[0])
            listbox_dist.insert(END, str(i)+".   "+str(j[1]))    
            
        listbox_can.grid(row=7,column=2,sticky=N+S+W+E)
        listbox_dist.grid(row=7,column=3,sticky=N+S+W+E)


        listbox_can.bind("<Double-Button-1>", select_can)
                

         
       
        

    def select_can(event):    # Function to run on double clicking a canteen, event stores the canteen name
                              # Dislays the canteen details of the selected canteen   

        w=event.widget

        if w.curselection()[0] > 8:
            value=w.get(w.curselection()[0])[6:]

        else:
            value=w.get(w.curselection()[0])[5:]

            
        can_data = particular_canteen(value)          # The canteen selected by the user

            
        tags=""
        for i in can_data["tags"]:
            tags = tags+", "+i
                
        tags=tags[1:]
            

        scroll_bar = Scrollbar(root, orient = HORIZONTAL)

        tag_list = Listbox(root,bg = "orange", xscrollcommand = scroll_bar.set, height = 2, font = 10)
        tag_list.insert(END,"TAGS")
        tag_list.insert(END, tags)

               
              

        Label(root, justify = CENTER, text = value, relief="ridge",font=("Arial Rounded MT Bold",20), bg = "orangered").grid(row =1, column = 4, columnspan=2, rowspan=2, sticky=N+S+E+W)
        Label(root, text = "Opening Hrs: "+can_data["start_hrs"]+" - "+ can_data["end_hrs"], font = 10, bg = "orange").grid(row=3, column = 4, columnspan=2, sticky=N+S+W+E)
        Label(root, text = "Rating: "+str(can_data["ratings"]), font = 10, bg = "orange").grid(row=4, column = 4, columnspan=2, sticky=N+S+W+E)


        tag_list.grid(row=5, column =4, columnspan = 2, sticky = N+E+W)
        scroll_bar.config(command = tag_list.xview)
        scroll_bar.grid(row=5, column =4, columnspan=2, sticky=S+W+E)

            


        Button(root, text="SHOW ROUTE",bg="green1",padx=10,pady=5,relief= "ridge",font=("Arial Rounded MT Bold",20), command = lambda: show_path(data[0],value)).grid(row=6,column=4, columnspan=2)



            
        img = PhotoImage(file="Pictures\\"+value+".ppm")      
        pic= Label(root, image=img)
        pic.image=img
        pic.grid(row=7, column=4, columnspan=2)
          
        
#------------------------------------------------------------------------
#                LOGIN FILE
#------------------------------------------------------------------------

def login_file(username,password):          # File to store username and password
    fil = shelve.open("database\login")
    fil[username] = password
    fil.close()

def ret_login_file():                       #opens the binary file containing username and password
                                            #returns  a dictionary containing existing usernames and passwords

    fil = shelve.open("database\Login")

    dic={}
    for username, data in fil.items():
        dic[username] = data

    fil.close()

    return dic


        
