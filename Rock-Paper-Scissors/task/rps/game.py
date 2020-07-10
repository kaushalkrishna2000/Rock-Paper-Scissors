from random import randint
def check(n):
    a=['ROCK','PAPER',"SCISSORS"]
    op=randint(0,2)
    op1=a[op]
    n=n.upper()
    n1=n.lower()
    if(n==op1):
        print("There is a draw ("+n1+")");return 0
    else:
        if(n=='ROCK' and op1=='SCISSORS'):
            print('Well done. Computer chose scissors and failed');return 1
        if(n=='ROCK' and op1=='PAPER'):
            print("Sorry, but computer chose paper");return -1
        if(n=='SCISSORS' and op1=='ROCK'):
            print("Sorry, but computer chose rock");return -1
        if(n=='SCISSORS' and op1=='PAPER'):
            print("Well done. Computer chose paper and failed");return 1
        if(n=='PAPER' and op1=='ROCK'):
            print('Well done. Computer chose rock and failed');return 1
        if(n=='PAPER' and op1=='SCISSORS'):
            print("Sorry, but computer chose scissors");return -1

def rater(name):

    try:
        with open('rating.txt') as f:
            lines = [line.rstrip() for line in f]
        for i in range(len(lines)):
            if(name in lines[i]):
                a=lines[i].split()
                return int(a[1])
    except FileNotFoundError as e:
        return 0

    return 0

def check1(n,l):
    op = randint(0, len(option)-1)
    op1 = l[op]
    l1=[]
    ch=l.index(n)

    if(ch==0):l1=l[ch:]
    elif(ch==len(l)-1):l1=l[0:ch]
    else:
        l1=l[ch+1:]+l[0:ch]

    loss=l1[0:len(l1)//2]
    win=l1[len(l1)//2:]

    if(n==op1):
        print("There is a draw ("+n+")");return 0

    if(op1 in loss):
        print("Sorry, but computer chose "+op1);return -1

    if(op1 in win):
        print('Well done. Computer chose '+op1+' and failed');return 1

def option1():
    ini=['rock','paper','scissors']
    n=input()
    if(n==''):
        return ini
    else:
        return n.split(",")

play=0;f=0

name=input("Enter your name:")
print("Hello, "+name)
#input options for playing pressing Enter will go to default options
#i.e. ['ROCK','PAPER',"SCISSORS"]
option=option1()

print("Okay, let's start")
while(True):
    n=input()
    if(n=='!exit'):
        print("Bye!")
        break
    elif(n in option):
        if(len(option)==3):
            l=check(n)
        else:
            l=check1(n,option)

        if(l==0):
            play+=50
        elif(l>0):
            play+=100
    elif(n=="!rating"):
        if(f==0):
            play+=rater(name);
            f=1
        print("Your rating: "+str(play))
    else:
        print("Invalid input")
