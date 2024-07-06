from tkinter import *
from PIL import Image,ImageTk
import random

interface = Tk()
interface.title("Rock,Paper,Scissor Game")
interface["bg"]= "#9b59b6"

Label_title = Label(text="Welcome to Python's Rock-Paper-Scissor Game",font=("Helvetica",20,"bold"),bg="orange")
Label_title.grid(row=0,column=1,columnspan=3)

# CPU GAME IMAGES
CPU_rock = ImageTk.PhotoImage(Image.open("Images\\Rock,Paper,Scissor Game\\Original Images in JPG\\CPU_Rock.jpg"))
CPU_paper = ImageTk.PhotoImage(Image.open("Images\\Rock,Paper,Scissor Game\\Original Images in JPG\\CPU_Paper.jpg"))
CPU_scissor = ImageTk.PhotoImage(Image.open("Images\\Rock,Paper,Scissor Game\\Original Images in JPG\\CPU_Scissor.jpg"))

# USER GAME IMAGES
user_rock = ImageTk.PhotoImage(Image.open("Images\\Rock,Paper,Scissor Game\\Original Images in JPG\\User_Rock.jpg"))
user_paper = ImageTk.PhotoImage(Image.open("Images\\Rock,Paper,Scissor Game\\Original Images in JPG\\User_Paper.jpg"))
user_scissor = ImageTk.PhotoImage(Image.open("Images\\Rock,Paper,Scissor Game\\Original Images in JPG\\User_Scissor.jpg"))

# SCORECARD
user_score = Label(interface,text=0,font=("",30,"bold"),bg="#eda65f",fg="black")
CPU_score = Label(interface,text=0,font=("",30,"bold"),bg="#eda65f",fg="black")
user_score.grid(row=2,column=1)
CPU_score.grid(row=2,column=3)

user_image = Label(interface, image = user_rock)
CPU_image = Label(interface, image = CPU_rock)

user_image.grid(row=2,column=0)
CPU_image.grid(row=2,column=4)

# RANDOMISATION FOR COMPUTER -

#1 List of choices
choices = ["ROCK","PAPER","SCISSOR"]


# DEFINING -

def change_pic(input):
#1 For Computer
    CPU_choice = choices[random.randint(0,2)]
    if CPU_choice == "ROCK":
        CPU_image.configure(image=CPU_rock)
    elif CPU_choice == "PAPER":
        CPU_image.configure(image=CPU_paper)
    elif CPU_choice == "SCISSOR":
        CPU_image.configure(image=CPU_scissor)    
    else:
        pass


#2 For User    
    if input == "ROCK":
        user_image.configure(image=user_rock)
    elif input == "PAPER":
        user_image.configure(image=user_paper) 
    else:
        user_image.configure(image=user_scissor)

    determine_winner(input,CPU_choice)    


# RESULT TEXTUAL REFRENCE - 
result_msg = Label(interface,font=("Helvetica",30,"bold"),text="")
result_msg.grid(row=2,column=2)


# DEFINING -
def update_result(input):
    result_msg['text']= input

# DEFINING -
def update_user_score():
     score = int(user_score["text"])
     score += 1
     user_score["text"]=str(score)  

def update_CPU_score():
     score = int(CPU_score["text"])
     score += 1
     CPU_score["text"]=str(score) 

# DETERMINING WINNER -
def determine_winner(user,CPU):   
    if user == "ROCK":
        if CPU == "PAPER":
            update_result("You Loose")
            update_CPU_score()
        elif CPU == "ROCK":
            update_result("It's a Tie")
        else:
            update_result("You Won")
            update_user_score()

    elif user == "PAPER":    
        if CPU == "SCISSOR":
            update_result("You Loose")
            update_CPU_score()
        elif CPU == "PAPER":
            update_result("It's a Tie")   
        else:
            update_result("You Won")
            update_user_score()   

    elif user == "SCISSOR":
        if CPU == "PAPER":
            update_result("You Won")
            update_user_score()
        elif CPU == "SCISSOR":
            update_result("It's a Tie")
        else:
            update_result("You Lose")
            update_CPU_score()

    else:
        pass        

# BUTTONS 
rock_button = Button(interface,text="ROCK",width=20, height=2,bg="#f50202",fg= "black",font=("Comic Sans MS",10,"bold"),padx=13,command=lambda:change_pic("ROCK"))
paper_button = Button(interface,text="PAPER",width=20, height=2,bg="#e3d002",fg= "black",font=("Comic Sans MS",10,"bold"),padx=13,command=lambda:change_pic("PAPER"))
scissor_button = Button(interface,text="SCISSOR",width=19, height=2,bg="#03f7ff",fg= "black",font=("Comic Sans MS",10,"bold"),padx=13,command=lambda:change_pic("SCISSOR"))

rock_button.grid(row=3,column=1)
paper_button.grid(row=3,column=2)
scissor_button.grid(row=3,column=3)

# TEXTUAL REFRENCES
user_identity = Label(interface, font=("",15,"bold"),text="USER")
CPU_identity = Label(interface, font=("",15,"bold"),text="COMPUTER")

user_identity.grid(row=1,column=0,pady=10)
CPU_identity.grid(row=1,column=4,pady=10)

Labe2_title = Label(text="You choose",font=("Helvetica",13,"bold"),bg="lightblue")
Labe2_title.grid(row=3,column=0,columnspan=1)
Labe3_title = Label(text="Computer Choose",font=("Helvetica",13,"bold"),bg="lightblue")
Labe3_title.grid(row=3,column=4,columnspan=3)

interface.mainloop()