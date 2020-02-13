import shelve


# Class Definition

class canteen():
    
    
    def __init__(self,name=None,tags=None,start_hrs=None,end_hrs=None,rating=0):
        self.name=name
        self.tags=tags
        self.start_hrs=start_hrs
        self.end_hrs=end_hrs
        self.rating=rating
        

    def get_time(self,a,b):
        from datetime import datetime
        sh=a[:2]
        sm=a[3:]
        eh=b[:2]
        em=b[3:]
        Day = datetime.now().day
        Month = datetime.now().month
        Year = datetime.now().year
        sd=datetime(Year,Month,Day,int(sh),int(sm),0,0)
        ed=datetime(Year,Month,Day,int(eh),int(em),0,0)
        return sd,ed
        
        
        
    def update_items(self):

        while True:
            print('\nEnter your option:')
            print('1: Update tags')
            print('2: Update the starting and ending hours')
            print('3: Logout')
            choice=int(input())

            if choice==1:
                print('\n')
                while True:
                    print('Press 1 to add a new tag:')
                    print('Press 2 to delete an existing tag')
                    option=int(input())
                    if option==1:
                        while True:
                            new_tag=input('Please enter the new tag:')
                            check=input('Are you sure that you want to continue?(y/n):')
                            if check=='y' or check=='Y' or check=='Yes' or check=='YES':
                                self.tags.append(new_tag)
                                print('\nNew list of tags:')
                                for i in self.tags:
                                    print(i,'\n')
                                break
                            else:
                                continue
                        break    

                        

                    elif option==2:
                        while True:
                            del_item=input('Please enter the item you want to delete:')
                            if del_item in self.tags:
                                self.tags.remove(del_item)
                                print('List of food items excluding the deleted food item:')
                                for i in self.tags:
                                    print(i)
                                break
                            else:
                                print('Please re-enter:')
                                continue
                        break    
                    else:
                        print('Please enter correctly!')
                        continue
                    
                    

            elif choice==2:
                while True:
                    open_hrs=input('Please enter the opening hours:')
                    close_hrs=input('Please enter the closing hours:')
                    check=input('Are you sure that you want to continue?(y/n):')
                    if check=='y' or check=='Y' or check=='Yes' or check=='YES':
                        self.start_hrs=open_hrs
                        self.end_hrs=close_hrs
                        self.display_details()
                        break
                    else:
                        print('Please enter correctly!')
                        
               
            elif choice==3:
                break
                  
            else:
                print('Please enter correctly!')


    
                
    def display_details(self):
        print('\n')
        print("Canteen Name: "'{}\n'.format(self.name))    
        print('Opening time: ',self.start_hrs,'\n')
        print('Closing time: ',self.end_hrs)
        print('\n')
        print('Ratings: ',self.rating,'\n')
        print('Tags: ', self.tags, "\n\n")



#Seperate Functions


def add_canteen(name,tags,start_hrs,end_hrs,rating):   #Adds a new canteen
    a = shelve.open("database\canteens")
    c = canteen(name,tags,start_hrs,end_hrs,rating)
    a[name]= c
    a.close()

        
def edit_canteen(c):  #Stores all the changes made to the details of the canteen

    a = shelve.open("database\canteens")
    a[c.name]=c
    a.close()


def get_canteen(name):               #Gets the canteen object
    a = shelve.open("database\canteens")
    if name not in a.keys():
        return False
    else:
        return a[name]
    

def all():   #Displays the details of all the canteens
    a = shelve.open("database\canteens")
    for i in a.values():
         i.display_details()
    a.close()

def suggest_canteens(pref):  #Function for suggesting the appropriate canteens
    from datetime import datetime

    l=[]
    p=pref.lower()
    t=datetime.now()

    fil = shelve.open("database\canteens")
    

    
    c= canteen()
    for c in fil.values():
            
        if p in c.tags:
            beg,last=c.get_time(c.start_hrs,c.end_hrs)        
            if beg<t<last:
                l.append(c.name)
    fil.close()
    return l
    
def particular_canteen(name):   #Returns the particulars of a canteen in the form of a dictionary
    c = get_canteen(name)
    return {"name": c.name, "tags": c.tags, "start_hrs": c.start_hrs,"end_hrs":c.end_hrs,"ratings":c.rating}



def get_user_location():     #Function to get user's location
    import pygame
    import time
    
    introScreenImage = pygame.image.load("Pictures\Campus.png")
    screen = pygame.display.set_mode((1200,1000))
    screen.blit(introScreenImage,(0,0))
    pygame.display.flip() 
    pygame.init()

    run=True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                mx,my=pygame.mouse.get_pos()
                pygame.quit()
                return(mx,my)
                #run=False
                
        pygame.display.update()


        

                




def canteen_function():     #Main Canteen Function
    while True:
        uname = input("\nEnter canteen name: ")
        if get_canteen(uname):
            c = get_canteen(uname)
            c.display_details()
            c.update_items()
            c.display_details()

            edit_canteen(c)
            break
                    
        else:
            print("Invalid canteen name")




