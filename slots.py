#Dominic Brogni and Raymond Chen
#Slot Machine
#Slot machine game
#Init
import random
import time
#Functions
#Main
gamble=["♪","♪","♪","♪","♪","♪","♪","♪",
        "♪","♪","♪","♪","♪","♪","♪","♪",
        "♪","♪","♪","♪","♪","♪","♪","♪",
        "♦","♦","♦","♦","♦","♦","♦",
        "♦","♦","♦","♦","♦","♦","♦",
        "♦","♦","♦","♦","♦","♦","♦",
        "☀","☀","☀",
        "☀","☀","☀",
        "☀","☀","☀","7","7","7","🃒"] #List of all possibilities for the slot machine

leave="no"
print("-|-|-Welcome to Slawts-|-|-") #UI
while True:
    if leave=="y":
        break
    while True:
        try:
            moolah=int(input("Deposit credits (WE ACCEPT 50, 100, 500): "))
            break
        except:
            print("Non-Integer detected. Try again.")
            continue
    while True:
        play=input("Press enter to spin, or type exit to cash out. ")
        if play=="":
            moolah=moolah-10
            if moolah<10:
                print("""Insufficient funds! Insert credits to continue.
                    """)
                break
            print("")
            time.sleep(0.4)
            f=random.choice(gamble)
            s=random.choice(gamble)
            t=random.choice(gamble)
            print(f"|-{f}-|-{s}-|-{t}-|")
            time.sleep(0.8)
            if f=="🃒":
                if s==t:
                    moolah=moolah+1010
                    print(f"""  !!!!!!!!!
  !JACKPOT!
  !!!!!!!!!
+1000 credits
New Balance: {moolah}
    """) #Jackpot win
                    time.sleep(1)
                    print("STICKY WILD CARD! FREE REROLL!")
                else:
                    print("You lost...")
                    time.sleep(1)
                    print("STICKY WILD CARD! FREE REROLL!")
                s=random.choice(gamble)
                t=random.choice(gamble)
                print(f"|-{f}-|-{s}-|-{t}-|")
                if s==t:
                    moolah=moolah+1010
                    print(f"""  !!!!!!!!!
  !JACKPOT!
  !!!!!!!!!
+1000 credits
New Balance: {moolah}
    """) #Jackpot win
                    print("Wild Card has expired.")
                    print("")
                else:
                    print("You lose... Wild Card expired")
                    print("")

            if s=="🃒":
                if f==t:
                    moolah=moolah+1010
                    print(f"""  !!!!!!!!!
  !JACKPOT!
  !!!!!!!!!
+1000 credits
New Balance: {moolah}
    """) #Jackpot win
                    time.sleep(1)
                    print("STICKY WILD CARD! FREE REROLL!")
                else:
                    print("You lost...")
                    time.sleep(1)
                    print("STICKY WILD CARD! FREE REROLL!")
                f=random.choice(gamble)
                t=random.choice(gamble)
                print(f"|-{f}-|-{s}-|-{t}-|")
                if f==t:
                    moolah=moolah+1010
                    print(f"""  !!!!!!!!!
  !JACKPOT!
  !!!!!!!!!
+1000 credits
New Balance: {moolah}
    """) #Jackpot win
                    print("Wild Card has expired.")
                    print("")
                else:
                    print("You lose... Wild Card expired")
                    print("")

            if t=="🃒":
                if s==f:
                    moolah=moolah+1010
                    print(f"""  !!!!!!!!!
  !JACKPOT!
  !!!!!!!!!
+1000 credits
New Balance: {moolah}
    """) #Jackpot win
                    time.sleep(1)
                    print("STICKY WILD CARD! FREE REROLL!")
                else:
                    print("You lost...")
                    time.sleep(1)
                    print("STICKY WILD CARD! FREE REROLL!")
                s=random.choice(gamble)
                f=random.choice(gamble)
                print(f"|-{f}-|-{s}-|-{t}-|")
                if s==f:
                    moolah=moolah+1010
                    print(f"""  !!!!!!!!!
  !JACKPOT!
  !!!!!!!!!
+1000 credits
New Balance: {moolah}
    """) #Jackpot win
                    print("Wild Card has expired.")
                    print("")
                else:
                    print("You lose... Wild Card expired")
                    print("")
            elif f=="7" and f==s and s==t:
                moolah=moolah+1010
                print(f"""  !!!!!!!!!
  !JACKPOT!
  !!!!!!!!!
+1000 credits
    New Balance: {moolah}
    """) #Jackpot win
            elif f==s and s==t:
                moolah=moolah+75
                print(f""" !!YOU WIN!!
    +65 credits
    New Balance: {moolah}""")
            else:
                print(f"  You Lost.")
            print("")
            time.sleep(0.4)
        elif play.lower()=="exit":
            leave=input("But are you SURE you want to leave?(y/n): ")
            if leave=="y":
                moolah=0
                print("""
Credits returned. Walking away...
                      """)
                break
            else:
                print("I heard no")
                continue
        elif play.lower()=="1ktest":
            testmoney=0
            l=0
            w=0
            jp=0
            for i in range(1000):
                f=random.choice(gamble)
                s=random.choice(gamble)
                t=random.choice(gamble)
                if f=="7" and f==s and f==t:
                    jp=jp+1
                    testmoney=testmoney-1000
                elif f==s and s==t:
                    w=w+1
                    testmoney=testmoney-65
                else:
                    l=l+1
                    testmoney=testmoney+10
            print(f"""--1000 spin diagnostic--
    Wins: {w} #Tracks user's info
    Losses: {l}
    Jackpots: {jp}
    House profit: {testmoney}
""")
            testmoney=0
            break
