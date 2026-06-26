
def printboard(xstate, zstate):
    zero =  {'x' if xstate[0] else ('0' if zstate[0] else 0)}
    one =  {'x' if xstate[1] else ('0' if zstate[1] else 1)}
    two =  {'x' if xstate[2] else ('0' if zstate[2] else 2)}
    three =  {'x' if xstate[3] else ('0' if zstate[3] else 3)}
    four = {'x' if xstate[4] else ('0' if zstate[4] else 4)}
    five = {'x' if xstate[5] else ('0' if zstate[5] else 5)}
    six = {'x' if xstate[6] else ('0' if zstate[6] else 6)}
    seven = {'x' if xstate[7] else ('0' if zstate[7] else 7)}
    eight = {'x' if xstate[8] else ('0' if zstate[8] else 8)}
    print(F" {zero} | {one} | {two} ")
    print(F"---|---|---")
    print(F" {three} | {four} | {five} ")
    print(F"---|---|---")
    print(F" {six} | {seven} | {eight} ")


if __name__=="__game__":
    xstate =[0,0,0,0,0,0,0,0]
    zstate =[0,0,0,0,0,0,0,0]
    turn = 1 #1 for x and 0 for o
    print("welcome to tic tac toe")
    while(True):
        printboard(zstate, zstate)
        if(turn == 1):
            print("X's chance")
            value = input("please enter the value")
            zstate[value] = 1
        else:
            print("x,s chance")
            value = int(input("please enter a value"))
            zstate[value] = 1
            
        break