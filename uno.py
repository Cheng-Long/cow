from email.header import decode_header
import random as rd
import json
import time

cardlist = [
'100','200','300','400','c','c','c','c','k','k','k','k',
'101','102','103','104','105','106','107','108','109','10s','10s','10p',
'101','102','103','104','105','106','107','108','109','10p','10s','10p',
'201','202','203','204','205','206','207','208','209','20s','20s','20p',
'201','202','203','204','205','206','207','208','209','20p','20s','20p',
'301','302','303','304','305','306','307','308','309','30s','30s','30p',
'301','302','303','304','305','306','307','308','309','30p','30s','30p',
'401','402','403','404','405','406','407','408','409','40s','40s','40p',
'401','402','403','404','405','406','407','408','409','40p','40s','40p'
]

empty = []
#迴轉難寫得要死 顧2迴轉改成1禁止1+2
#s = stop; p = +2; c = color change; k = king
def deal():
    global holdcard
    holdcard = []
    for x in range(7):
        my_card = rd.choice(cardlist)
        cardlist.remove(my_card) 
        holdcard.append(my_card)
    return holdcard

def pc2_deal():
    global pc2_holdcard
    pc2_holdcard = []
    for x in range(7):
        my_card = rd.choice(cardlist)
        cardlist.remove(my_card) 
        pc2_holdcard.append(my_card)

def pc3_deal():
    global pc3_holdcard
    pc3_holdcard = []
    for x in range(7):
        my_card = rd.choice(cardlist)
        cardlist.remove(my_card) 
        pc3_holdcard.append(my_card)

def pc4_deal():
    global pc4_holdcard
    pc4_holdcard = []
    for x in range(7):
        my_card = rd.choice(cardlist)
        cardlist.remove(my_card) 
        pc4_holdcard.append(my_card)


#=============================================================

def get_first_card():
    first_card = rd.choice(cardlist)
    cardlist.remove(first_card) 
    return first_card

#=============================================================

def get_new_card():
    new_card = rd.choice(cardlist)
    cardlist.remove(new_card)
    holdcard.append(new_card)

def pc2_get_new_card():
    new_card = rd.choice(cardlist)
    cardlist.remove(new_card)
    pc2_holdcard.append(new_card)

def pc3_get_new_card():
    new_card = rd.choice(cardlist)
    cardlist.remove(new_card)
    pc3_holdcard.append(new_card)

def pc4_get_new_card():
    new_card = rd.choice(cardlist)
    cardlist.remove(new_card)
    pc4_holdcard.append(new_card)

#=============================================================

my__card=deal()
pc2=pc2_deal()
pc3=pc3_deal()
pc4=pc4_deal()
topcard = get_first_card()
print("Start Card:",topcard)

s = 0
s2 = 0
s3 = 0
s4 = 0

command_list = ["stop","n","empty","cc","kk"]

while True :

    while True :
        if s == 0 :
            print("Hold:",my__card)
            play = input("Your Card>>")
            if play in my__card or play in command_list :
                if play == "stop":
                    break

                elif play == "empty" :
                    my__card = []
                    break
                elif play == "cc":
                    holdcard.append("c")
                elif play == "kk":
                    holdcard.append("k")

                elif play == "n":
                    get_new_card()
                    break

                elif play == "c":
                    print(">>Change color")
                    color = input("Your color(1/2/3/4)>>")
                    if color == "1":
                        topcard = "10c"
                    elif color == "2":
                        topcard = "20c"
                    elif color == "3":
                        topcard = "30c"
                    elif color == "4":
                        topcard = "40c"
                    my__card.remove(play)
                    cardlist.append(play)
                    print("top:",topcard)
                    break

                elif play == "k":
                    s2 = 1
                    print(">>Change color & +4")
                    color = input("Your color(1/2/3/4)>>")
                    if color == "1":
                        topcard = "10c"
                    elif color == "2":
                        topcard = "20c"
                    elif color == "3":
                        topcard = "30c"
                    elif color == "4":
                        topcard = "40c"
                    pc2_get_new_card()
                    pc2_get_new_card()
                    pc2_get_new_card()
                    pc2_get_new_card()
                    my__card.remove(play)
                    cardlist.append(play)
                    print("you -> pc2 : +4")
                    break

                elif play[0] == topcard[0] :
                    if play in my__card :
                        if play[-1] == "p":
                            topcard = play
                            my__card.remove(play)
                            cardlist.append(play)
                            s2 = 1
                            pc2_get_new_card()
                            pc2_get_new_card()
                            print("you -> pc2 : +2")
                            break
                        elif play[-1] == "s" :
                            topcard = play
                            my__card.remove(play)
                            cardlist.append(play)
                            s2 = 1
                            break
                        else :
                            topcard = play
                            my__card.remove(play)
                            cardlist.append(play)
                            s4 = 0
                            break

                elif play[-1] == topcard[-1] :
                    if play in my__card :
                        if play[-1] == "p":
                            topcard = play
                            my__card.remove(play)
                            cardlist.append(play)
                            s2 = 1
                            pc2_get_new_card()
                            pc2_get_new_card()
                            print("you -> pc2 : +2")
                            break
                        elif play[-1] == "s" :
                            topcard = play
                            my__card.remove(play)
                            cardlist.append(play)
                            s2 = 1
                            break
                        else :
                            topcard = play
                            my__card.remove(play)
                            cardlist.append(play)
                            s4 = 0
                            break

                elif play[0] != topcard[0] and play[-1] != topcard[-1] :
                    print("Plz use the ringt card")

        else :
            print(">>You get pass")
            time.sleep(1)
            break
    
    #=============================================================

    def ai2():
        n = 0 
        global s,s2, s3, s4
        global topcard
        print(pc2_holdcard)
        for x in range(len(pc2_holdcard)):
            if s2 != 0 :
                print(">> pass")
                print("top:",topcard)
                s2 = 0
                break
            elif pc2_holdcard[n][0] == topcard[0] :
                if  pc2_holdcard[n][-1] == "p" :
                    s3 = 1
                    pc3_get_new_card()
                    pc3_get_new_card()
                    topcard = pc2_holdcard[n]
                    pc2_holdcard.remove(pc2_holdcard[n])
                    cardlist.append(play)
                    print("pc2>>",topcard)
                    print("pc2 -> pc3 : +2")
                    print("top:",topcard)
                    break
                elif pc2_holdcard[n][-1] == "s" :
                    s3 = 1
                    topcard = pc2_holdcard[n]
                    pc2_holdcard.remove(pc2_holdcard[n])
                    cardlist.append(play)
                    print("pc2>>",topcard)
                    print("top:",topcard)
                    break
                else :
                    topcard = pc2_holdcard[n]
                    pc2_holdcard.remove(pc2_holdcard[n])
                    cardlist.append(play)
                    print("pc2>>",topcard)
                    print("top:",topcard)
                    s = 0 
                    break
            elif pc2_holdcard[n][-1] == topcard[-1] :
                if  pc2_holdcard[n][-1] == "p" :
                    s3 = 1
                    pc3_get_new_card()
                    pc3_get_new_card()
                    topcard = pc2_holdcard[n]
                    pc2_holdcard.remove(pc2_holdcard[n])
                    cardlist.append(play)
                    print("pc2>>",topcard)
                    print("pc2 -> pc3 : +2")
                    print("top:",topcard)
                    break
                elif pc2_holdcard[n][-1] == "s" :
                    s3 = 1
                    topcard = pc2_holdcard[n]
                    pc2_holdcard.remove(pc2_holdcard[n])
                    cardlist.append(play)
                    print("pc2>>",topcard)
                    print("top:",topcard)
                    break
                else :
                    topcard = pc2_holdcard[n]
                    pc2_holdcard.remove(pc2_holdcard[n])
                    cardlist.append(play)
                    print("pc2>>",topcard)
                    print("top:",topcard)
                    s = 0
                    break
            else :
                n +=1
                if n == len(pc2_holdcard) :
                    if "c" in pc2_holdcard :
                        print(">>Change color")
                        topcard = pc2_holdcard[0][0]
                        pc2_holdcard.remove("c")
                        cardlist.append(play)
                        print(f"color:{pc2_holdcard[0][0]}")
                        break
                    elif "k" in pc2_holdcard :
                        s3 = 1
                        print(">>+4 & Change color")
                        pc3_get_new_card()
                        pc3_get_new_card()
                        pc3_get_new_card()
                        pc3_get_new_card()
                        topcard = pc2_holdcard[0][0]
                        pc2_holdcard.remove("k")
                        cardlist.append(play)
                        print(f"color:{pc2_holdcard[0][0]}")
                        print("pc2 -> pc3 : +4")
                        break
                    pc2_get_new_card()
                    print("pc2>>'I get new card'")
                    print("top:",topcard)
                    s = 0
                    break

    def ai3():
        n = 0
        global s,s2, s3, s4
        global topcard
        print(pc3_holdcard)
        for x in range(len(pc3_holdcard)):
            if s3 != 0 :
                print(">>pass")
                print("top:",topcard)
                s3 = 0
                break
            elif pc3_holdcard[n][0] == topcard[0] :
                if  pc3_holdcard[n][-1] == "p" :
                    s4 = 1
                    pc4_get_new_card()
                    pc4_get_new_card()
                    topcard = pc3_holdcard[n]
                    pc3_holdcard.remove(pc3_holdcard[n])
                    cardlist.append(play)
                    print("pc3>>",topcard)
                    print("pc3 -> pc4 : +2")
                    print("top:",topcard)
                    break
                elif pc3_holdcard[n][-1] == "s" :
                    s4 = 1
                    topcard = pc3_holdcard[n]
                    pc3_holdcard.remove(pc3_holdcard[n])
                    cardlist.append(play)
                    print("pc3>>",topcard)
                    print("top:",topcard)
                    break
                else :
                    topcard = pc3_holdcard[n]
                    pc3_holdcard.remove(pc3_holdcard[n])
                    cardlist.append(play)
                    print("pc3>>",topcard)
                    print("top:",topcard)
                    s2 = 0
                break
            elif pc3_holdcard[n][-1] == topcard[-1] :
                if  pc3_holdcard[n][-1] == "p" :
                    s4 = 1
                    pc4_get_new_card()
                    pc4_get_new_card()
                    topcard = pc3_holdcard[n]
                    pc3_holdcard.remove(pc3_holdcard[n])
                    cardlist.append(play)
                    print("pc3>>",topcard)
                    print("pc3 -> pc4 : +2")
                    print("top:",topcard)
                    break
                elif pc3_holdcard[n][-1] == "s" :
                    s4 = 1
                    topcard = pc3_holdcard[n]
                    pc3_holdcard.remove(pc3_holdcard[n])
                    cardlist.append(play)
                    print("pc3>>",topcard)
                    print("top:",topcard)
                    break
                else :
                    topcard = pc3_holdcard[n]
                    pc3_holdcard.remove(pc3_holdcard[n])
                    cardlist.append(play)
                    print("pc3>>",topcard)
                    print("top:",topcard)
                    s2 = 0
                    break
            else :
                n +=1
                if n == len(pc3_holdcard):
                    if "c" in pc3_holdcard :
                        print(">>Change color")
                        topcard = pc3_holdcard[0][0]
                        pc3_holdcard.remove("c")
                        cardlist.append(play)
                        print(f"color:{pc3_holdcard[0][0]}")
                        break
                    elif "k" in pc3_holdcard :
                        s3 = 1
                        print(">>+4 & Change color")
                        pc4_get_new_card()
                        pc4_get_new_card()
                        pc4_get_new_card()
                        pc4_get_new_card()
                        topcard = pc3_holdcard[0][0]
                        pc3_holdcard.remove("k")
                        cardlist.append(play)
                        print(f"color:{pc3_holdcard[0][0]}")
                        print("pc3 -> pc4 : +4")
                        break
                    pc3_get_new_card()
                    print("pc3>>'I get new card'")
                    print("top:",topcard)
                    s2 = 0
                    break

    def ai4():
        n = 0
        global s,s2, s3, s4
        global topcard
        print(pc4_holdcard)
        for x in range(len(pc4_holdcard)):
            if s4 != 0 :
                print(">>pass")
                print("top:",topcard)
                s4 = 0
                break
            elif pc4_holdcard[n][0] == topcard[0] :
                if  pc4_holdcard[n][-1] == "p" :
                    s = 1
                    get_new_card()
                    get_new_card()
                    topcard = pc4_holdcard[n]
                    pc4_holdcard.remove(pc4_holdcard[n])
                    cardlist.append(play)
                    print("pc4>>",topcard)
                    print("pc4 -> you : +2")
                    print("top:",topcard)
                    break
                elif pc4_holdcard[n][-1] == "s" :
                    s = 1
                    topcard = pc4_holdcard[n]
                    pc4_holdcard.remove(pc4_holdcard[n])
                    cardlist.append(play)
                    print("pc4>>",topcard)
                    print("top:",topcard)
                    break
                else :
                    topcard = pc4_holdcard[n]
                    pc4_holdcard.remove(pc4_holdcard[n])
                    cardlist.append(play)
                    print("pc4>>",topcard)
                    print("top:",topcard)
                    s3 = 0
                    break     
            elif pc4_holdcard[n][-1] == topcard[-1] :
                if  pc4_holdcard[n][-1] == "p" :
                    s = 1
                    get_new_card()
                    get_new_card()
                    topcard = pc4_holdcard[n]
                    pc4_holdcard.remove(pc4_holdcard[n])
                    cardlist.append(play)
                    print("pc4>>",topcard)
                    print("pc4 -> you : +2")
                    print("top:",topcard)
                    break
                elif pc4_holdcard[n][-1] == "s" :
                    s = 1
                    topcard = pc4_holdcard[n]
                    pc4_holdcard.remove(pc4_holdcard[n])
                    cardlist.append(play)
                    print("pc4>>",topcard)
                    print("top:",topcard)
                    break
                else :
                    topcard = pc4_holdcard[n]
                    pc4_holdcard.remove(pc4_holdcard[n])
                    cardlist.append(play)
                    print("pc4>>",topcard)
                    print("top:",topcard)
                    s3 = 0
                    break

            else :
                n +=1
                if n == len(pc4_holdcard) :
                    if "c" in pc4_holdcard :
                        print(">>Change color")
                        topcard = pc4_holdcard[0][0]
                        pc4_holdcard.remove("c")
                        cardlist.append(play)
                        print(f"color:{pc4_holdcard[0][0]}")
                        break
                    elif "k" in pc4_holdcard :
                        s3 = 1
                        print(">>+4 & Change color")
                        get_new_card()
                        get_new_card()
                        get_new_card()
                        get_new_card()
                        topcard = pc4_holdcard[0][0]
                        pc4_holdcard.remove("k")
                        cardlist.append(play)
                        print(f"color:{pc4_holdcard[0][0]}")
                        print("pc4 -> you : +4")
                        break
                    pc4_get_new_card()
                    print("pc4>>'I get new card'")
                    print("top:",topcard)
                    s3 = 0
                    break

    #=============================================================
    if my__card == empty :
        print(">>YOU ARE THE WINNER<<")
        break
    print("========")
    ai2()
    if pc2_holdcard == empty :
        print(">>pc2 IS THE WINNER<<")
        break
    time.sleep(1)
    print("========")
    ai3()
    if pc3_holdcard == empty :
        print(">>pc3 IS THE WINNER<<")
        break
    time.sleep(1)
    print("========")
    ai4()
    if pc4_holdcard == empty :
        print(">>pc4 IS THE WINNER<<")
        break
    time.sleep(1)
    print("========")
