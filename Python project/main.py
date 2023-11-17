from tkinter import *

root = Tk()
root.geometry("350x550")
root.title("Tic Tac Toe")
root.resizable(0,0)
frame1= Frame(root)
frame1.pack()
titlelable= Label(frame1, text="Tic Tac Toe", font=("Arial",27), bg="khaki1",width=16)
titlelable.grid(row=0,column=0)

optionframe=Frame(root,bg="grey")
optionframe.pack()

frame2= Frame(root,bg="yellow")
frame2.pack()


board= {1:" ",2:" ",3:" ",
        4:" ",5:" ",6:" ",
        7:" ",8:" ",9:" "}

def checkwin(player):
    
    #rows check
    if board[1]==board[2] and board[2]==board[3] and board[3]==player:
        return True
    elif board[4]==board[5] and board[5]==board[6] and board[6]==player:
        return True
    elif board[7]==board[8] and board[8]==board[9] and board[9]==player:
        return True 
    
    #column check
    elif board[1]==board[4] and board[4]==board[7] and board[7]==player:
        return True 
    elif board[2]==board[5] and board[5]==board[8] and board[8]==player:
        return True 
    elif board[3]==board[6] and board[6]==board[9] and board[9]==player:
        return True 
    
    #diagonal check
    elif board[1]==board[5] and board[5]==board[9] and board[9]==player:
        return True 
    elif board[3]==board[5] and board[5]==board[7] and board[7]==player:
        return True
    else:
        return False
    
def checkdraw():
    for i in board.keys():
        if board[i]==" ":
            return False
    return True
turn = "X"
game_end=False
mode="singleplayer"

def changemodetosp():
    global mode
    mode="singleplayer"
    spButton["bg"]="light sea green"
    mpButton["bg"]="grey"
    
def changemodetomp():
    global mode
    mode="multiplayer"
    mpButton["bg"]="light sea green"
    spButton["bg"]="grey"


def updateboard():
    for key in board.keys():
        button_list[key-1]["text"]=board[key]


def restartgame():
    global game_end
    game_end=False
    for button in button_list:
        button["text"]= " "
    
    for i in board.keys():
        board[i]=" " 
        
    titlelable= Label(frame1, text="Tic Tac Toe", font=("Arial",25), bg="khaki1",width=20)
    titlelable.grid(row=0,column=0)


def minimax(board, ismaximizing):
    
    if checkwin("O"):
        return 1
    
    if checkwin("X"):
        return -1
    
    if checkdraw():
        return 0
    
    if ismaximizing:
        bestscore=-100
        
        for key in board.keys():
            if board[key]==" ":
                board[key]="O"
                score =minimax(board,False)
                board[key]=" "
                if score>bestscore:
                    bestscore=score
                    
        return bestscore
    
    else:
        bestscore=100
        
        for key in board.keys():
            if board[key]==" ":
                board[key]="X"
                score =minimax(board,True)
                board[key]=" "
                if score<bestscore:
                    bestscore=score
                    
        return bestscore
    

def playcomputer():
    bestscore=-100
    bestmove=0
    
    for key in board.keys():
        if board[key]==" ":
            board[key]="O"
            score =minimax(board,False)
            board[key]=" "
            if score>bestscore:
                bestscore=score
                bestmove=key
    board[bestmove]="O"
            
            
def play(event):
    global turn,game_end
    
    if game_end:
        return
    button=event.widget
    buttonno=str(button)
    clicked=buttonno[-1]
    if clicked=='n':
        clicked=1
    else:
        clicked=int(clicked)
    print(clicked)
    
    
    if button["text"]==" ":
        
        if turn == "X":
            board[clicked]=turn
            if checkwin(turn):
                winlabel=Label(frame1, text=f"{turn}, wins the game",bg="khaki1",font=('Arial',25))
                winlabel.grid(row=0,column=0,columnspan=3)
                game_end = True
            turn="O"
            
            updateboard()
            
            if mode=="singleplayer":
            
                playcomputer()
            
                if checkwin(turn):
                    winlabel=Label(frame1, text=f"{turn}, wins the game",bg="khaki1",font=('Arial',25))
                    winlabel.grid(row=0,column=0,columnspan=3)
                    game_end = True
                
                
                turn="X"
            
                updateboard()
            
            
            
        else:
            button["text"]="O"
            board[clicked]=turn
            updateboard()
            if checkwin(turn):
                winlabel=Label(frame1, text=f"{turn}, wins the game",bg="khaki1",font=('Arial',25))
                winlabel.grid(row=0,column=0,columnspan=3)
                game_end = True
            turn="X"
        
        
        
        if checkdraw():
            drawlabel=Label(frame1, text=f"Game Draw",bg="orange", font=("Arial",25),width=20)
            drawlabel.grid(row=0,column=0,columnspan=3)
            
    print(board)
    

#############################  TIC TAC TOE UI   ################################

spButton = Button(optionframe,text="Singleplayer", width=14 ,height=1, font=("Arial",15),bg="grey",relief=RAISED,borderwidth=5,command=changemodetosp)
spButton.grid(row=0,column=0,columnspan=1,sticky=NW)

mpButton = Button(optionframe,text="Multiplayer", width=14 ,height=1, font=("Arial",15),bg="grey",relief=RAISED,borderwidth=5,command=changemodetomp)
mpButton.grid(row=0,column=1,columnspan=1,sticky=NW)


#Board setup   
#first row
button1=Button(frame2, text=" ",width=4,height=2, font=("Arial",30),bg="cyan", relief=RAISED,borderwidth=5)
button1.grid(row=0,column=0)
button1.bind("<Button-1>",play)

button2=Button(frame2, text= " ",width=4,height=2, font=("Arial",30),bg="cyan", relief=RAISED,borderwidth=5)
button2.grid(row=0,column=1)
button2.bind("<Button-1>",play)

button3=Button(frame2, text= " ",width=4,height=2, font=("Arial",30),bg ="cyan", relief=RAISED,borderwidth=5)
button3.grid(row=0,column=2)
button3.bind("<Button-1>",play)

#second Row
button4=Button(frame2, text= " ",width=4,height=2, font=("Arial",30),bg="cyan", relief=RAISED,borderwidth=5)
button4.grid(row=1,column=0)
button4.bind("<Button-1>",play)

button5=Button(frame2, text= " ",width=4,height=2, font=("Arial",30),bg="cyan", relief=RAISED,borderwidth=5)
button5.grid(row=1,column=1)
button5.bind("<Button-1>",play)

button6=Button(frame2, text= " ",width=4,height=2, font=("Arial",30),bg="cyan", relief=RAISED,borderwidth=5)
button6.grid(row=1,column=2)
button6.bind("<Button-1>",play)

#third row

button7=Button(frame2, text= " ",width=4,height=2, font=("Arial",30),bg="cyan", relief=RAISED,borderwidth=5)
button7.grid(row=2,column=0)
button7.bind("<Button-1>",play)

button8=Button(frame2, text= " ",width=4,height=2, font=("Arial",30),bg="cyan", relief=RAISED,borderwidth=5)
button8.grid(row=2,column=1)
button8.bind("<Button-1>",play)

button9=Button(frame2, text= " ",width=4,height=2, font=("Arial",30),bg="cyan", relief=RAISED,borderwidth=5)
button9.grid(row=2,column=2)
button9.bind("<Button-1>",play)

restartButton = Button(frame2,text="Restart Game", width=19 ,height=1, font=("Arial",20),bg="red",relief=RAISED,borderwidth=5,command=restartgame)
restartButton.grid(row=4,column=0,columnspan=3)

button_list=[button1,button2,button3,button4,button5,button6,button7,button8,button9]

root.mainloop()