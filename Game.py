import random

u=0
r=1


def computer():
    ls=[0,1,2]
    ch_x=random.choice(ls)
    ch_y=random.choice(ls)
    if map[ch_x][ch_y]=="":
        map[ch_x][ch_y]=chh
    else:
        computer()
    check()

def looper(emp=0):
    emp=0
    fl=0
    for i in range(0,3):
        for j in range(0,3):
            if map[i][j] =="" :
                fl+fl+1
            elif map[i][j]!="":
                emp=emp+1
                r=emp

# def user():
#     x=""
#     y=""
#     x=pos2[0]
#     y=pos2[1]
#     if x=="a":
#         x=1
#     elif x=="b":
#         x=2
#     elif x=="c":
#         x=3
#     else:
#         print("invalid input")
#     x=int(x)-1
#     y=int(y)-1
#     map[x][y]=ch
#     print(f"{a}\n{b}\n{c}")

def check():
    #for l diagonal ,1st row and 1st colunm(3)
    if map[0][0]!="" and map[0][0]==map[1][1] and map[1][1]==map[2][2] or map[0][0]!="" and map[0][0]==map[1][0] and map[1][0]==map[2][0] or map[0][0]!="" and map[0][0]==map[0][1] and map[0][1]==map[0][2] :
        print("---------------------------------------------------------------------------------------------------------------------------------------------")
        print("Game won by ",map[0][0])
        print(f"{a}\n{b}\n{c}")
        quit()
    #for r diagonal(1)
    elif map[0][2]!="" and map[0][2]==map[1][1] and map[1][1]==map[2][0] :
        print("---------------------------------------------------------------------------------------------------------------------------------------------")
        print("Game won by ",map[0][2])
        print(f"{a}\n{b}\n{c}")
        quit()
    #for 2nd colunm(1)
    elif map[0][1]!="" and map[0][1]==map[1][1] and map[1][1]==map[2][1] :
        print("---------------------------------------------------------------------------------------------------------------------------------------------")
        print("Game won by ",map[0][1])
        print(f"{a}\n{b}\n{c}")
        quit()
    #for 3rd colunm(1)
    elif map[0][2]!="" and map[0][2]==map[1][2] and map[1][2]==map[2][2]:
        print("---------------------------------------------------------------------------------------------------------------------------------------------")
        print("Game won by ",map[0][2])
        print(f"{a}\n{b}\n{c}")
        quit()
    #for 2nd row
    elif map[1][0]!="" and map[1][0]==map[1][1] and map[1][1]==map[1][2]:
        print("---------------------------------------------------------------------------------------------------------------------------------------------")
        print("Game won by ",map[1][0])
        print(f"{a}\n{b}\n{c}")
        quit()
    #for 3rd row
    elif map[2][0]!="" and map[2][0]==map[2][1] and map[2][1]==map[2][2]:
        print("---------------------------------------------------------------------------------------------------------------------------------------------")
        print("Game won by ",map[2][0])
        print(f"{a}\n{b}\n{c}")
        quit()
    elif map[0][0]!="" and map[0][1]!="" and map[0][2]!="" and map[1][0]!="" and map[1][1]!="" and map[1][2]!="" and map[2][0]!="" and map[2][1]!="" and map[2][2]!="" :
        print("---------------------------------------------------------------------------------------------------------------------------------------------")
        print("Game Over A TIE !")
        print(f"{a}\n{b}\n{c}")
        quit()

def pl2():
    print("---------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"{a}\n{b}\n{c}")
    plpos2=(input("PLAYER 2 enter your position  (ex:A1): ")).lower()
    x=""
    y=""
    x=plpos2[0]
    y=plpos2[1]
    if x=="a":
        x=1
    elif x=="b":
        x=2
    elif x=="c":
        x=3
    else:
        print("invalid input")
    x=int(x)-1
    y=int(y)-1
    if map[x][y]=="":
        map[x][y]=chh
    else:
        print("You can't do that!")
        pl2()
    # print("---------------------------------------------------------------------------------------------------------------------------------------------")
    # print(f"{a}\n{b}\n{c}")
    check()

def put():
    print("---------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"{a}\n{b}\n{c}")
    if mul=="Y" or "YES":
        pos2=(input("Player one enter your position (ex:A1): ")).lower()
    else:
        pos2=(input("Enter your position (ex:A1): ")).lower()
    x=""
    y=""
    x=pos2[0]
    y=pos2[1]
    if x=="a":
        x=1
    elif x=="b":
        x=2
    elif x=="c":
        x=3
    else:
        print("invalid input")
    x=int(x)-1
    y=int(y)-1
    if map[x][y]=="":
        map[x][y]=ch
    else:
        print("You can't do that!")
        put()
    # print("---------------------------------------------------------------------------------------------------------------------------------------------")
    # print(f"{a}\n{b}\n{c}")
    check()


a=["","","",]
b=["","","",]
c=["","","",]

print(f"{a}\n{b}\n{c}")
mul=input("Do you want to play with a friend or not: ").upper()

if mul=="Y" or mul=="YES":
    ch=input("Player one select (O or X): ").upper()
    pos=(input("Enter your position player one (ex:A1): ")).lower()

else:
    ch=(input("Which one do you want (O or X): ")).upper()
    pos=(input("Enter your position (ex:A1): ")).lower()

map=[a,b,c]
x=pos[0]
y=pos[1]

if x=="a":
    x=1
elif x=="b":
    x=2
elif x=="c":
    x=3
else:
    print("invalid input")
x=int(x)-1
y=int(y)-1
map[x][y]=ch

#compyter x/o
if ch=="X" :
    chh="O"
else :
    chh="X"

if mul=="Y" or mul=="YES":
    pl2()
else:
    computer()
    

# print(f"{a}\n{b}\n{c}")

# if fst==1 :


while r!=0:
    if u%2==0  :
        put()
        u=u+1
        looper()
    elif u%2!=0 and mul=="Y" or mul=="YES":
        pl2()
        u=u+1
        looper()
    else:
        computer()
        u=u+1
        looper()



print(f"{a}\n{b}\n{c}")
# print(map[0][0]) it works!!!!!!!