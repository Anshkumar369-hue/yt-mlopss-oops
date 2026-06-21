class chatbook:
    def_init_(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()


   def menu(self):
         user_input = input(""""Welcome to Chatbook !! How would you like to proceed?
                                      1.Press 1 to signup
                                      2.press 2 to signin
                                      3.press 3 to write a post 
                                      4.press 4 to message a friend
                                      5.press any other key to exit""")
         if user_input == "1":
            pass
         elif user_input == "2":
            pass
         elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()    

 def signup(self):
    email =  input("enter your email here -> ")
    pass =   input("setup your password here ->")    
    self.username = email
    self.password = pwd   
    print("you have signedup successfully !!")
    print("\n")
    self.menu()

 def signin(self): 
    if self.username=='' and self.password=='':
        print("please signup first by pressing 1 in the main menu")
    else:
        uname = input("enter your email/username here -> ")   
        pwd = input("ENter your password here -> ") 
        if self.username==uname and self.password==pwd:
            print("you have signed in successfully !!")
            self.loggedin = True
        else:
            print("please input correct credentials..")
    print("\n")
    self.menu()            


obj = chatbook()
