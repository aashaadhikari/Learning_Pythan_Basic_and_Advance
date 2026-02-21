from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i]!= usertest[i]:
                error = error+1
        except :
            error = error+1  

    return error 


def speed_time(time_s, time_e, useriput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(useriput)/ time_R
    return round(speed)

while True:
    ck = input(" ready to test: yes/no: ")
    if ck == "yes":
        test=["A photograph is a self contained unit of discourse in writing dealing with a particular point or idea. ",

        "my name is seema adhikari", "Welcome to my project of python"]

        test1 = r.choice(test)

        print("  ***** Typing speed *****")

        print(test1)
        print()
        print()

        time_1 = time()
        test_input = input(" Enter : ")
        time_2 = time()

        print("Speed: ", speed_time(time_1, time_2, test_input), "w/sec")
        print("Error: ", mistake(test1, test_input))
    elif ck == "no":    
        print("thank you")
        break
    else:
        print("Wromg input")



