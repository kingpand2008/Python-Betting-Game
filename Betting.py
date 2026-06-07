import random
def spin(LC):
    print("*" * 50)
    print("Ready Spin")
    print("*" * 50)
    L=["🍍","🔔","🍓"]
    for i in range(3):
        LC.append(random.choice(L))
def payout(bet,LC):
    global bal
    print("*" * 50)
    print("SPINNING SPINNING...............")
    print(" | ".join(LC))
    print("Type '0' to stop:")
    if LC[0]==LC[1]==LC[2]:
        print("You Won")
        bal+=bet*3
    else:
        print("You Lost")
    print("*" * 50)
print("*"*50)
print("Welcome to Betting Game")
print("*"*50)
bal=int(input("Enter your Bank Balance: "))
c=input("Start?(yes/no):").lower()
if c=="yes":

    while bal>0:
        LC=[]
        print("*" * 50)
        try:
            bet=int(input("Enter your Bet: "))
            if bet>bal:
                print("Insufficient Balance")
            elif bet<0:
                print("Invalid Bet")
            elif bet==0:
                break
            else:
                bal-=bet
                spin(LC)
                payout(bet,LC)
                print("Your Balance is: ",bal)

        except ValueError:
            print("Please enter a number")
            continue
    print("No Money , Thank You")





