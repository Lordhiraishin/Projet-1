#coding in utf-8


#Import
import os, sys
import RichConsole

# os.system('')

def map():

#variables    
    montagne = "\x1b[41m \x1b[0m"
    jungle = "\x1b[42m \x1b[0m"
    eau = "\x1b[44m \x1b[0m"
    plage = "\x1b[43m \x1b[0m"
    event = "\x1b[45m \x1b[0m"

    m = montagne
    j = jungle
    e = eau
    p = plage
    x = event


    x1 = [m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m]
    x2 = [m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m]
    x3 = [m,m,m,m,m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,e,j,x,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,m,m,m,m,x,m]
    x4 = [m,m,m,m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,m]
    x5 = [m,m,m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,m]
    x6 = [m,m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,m,m,m]
    x7 = [m,m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,m,m,m,m]
    x8 = [m,m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,e,e,e,e,e,e,j,j,j,j,j,j,j,m,m,m,m,j,e,e,e,e,e]
    x9 = [m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,m,m,p,p,e,e,e,e]
    x10 = [m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,m,m,p,p,p,p,e,e,e,e]
    x11 = [m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,m,m,p,p,p,p,p,p,p,e]
    x12 = [m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p,p,p,p]
    x13 = [m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p,p,e]
    x14 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,e,e,e]
    x15 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p,e,e]
    x16 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p,p,p,p,p]
    x17 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p,p,p,p,p]
    x18 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p,e,e]
    x19 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p]
    x20 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p]
    x21 = [e,e,j,j,j,j,j,j,j,j,j,j,j,x,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,e,e]
    x22 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p,p,p]
    x23 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p,p,e]
    x24 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,e]
    x25 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p]
    x26 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,x,m,m,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p]
    x27 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,m,m,m,m,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,e,e]
    x28 = [e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]
    x29 = [e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]
    x30 = [e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]

    xall = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30]

    for index in xall:
        for p in index:
            print(p,end="")
        print()



if __name__ == "__main__" :
    map()



# for index in y:
#     for loop in index:
#         print(loop,end="")
#     print()