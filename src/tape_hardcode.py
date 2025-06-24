def create_rules():
    rules = []
    # Count the length of the string
    rules.append(["L",1,"L",2, "RIGHT"])
    for i in range(10):
        rules.append(["0",i+2,"0",i+3,"RIGHT"])
        rules.append(["1",i+2,"1",i+3,"RIGHT"]) #sampe 12
        rules.append(["X", i+2, "X", i+3, "RIGHT"])
    # Case 0: Length of string is 0
    rules.append(["R",2,"R",2,"REJECT"])
    # REJECT all odd state
    for i in range(4):
        rules.append(["R",2*i+3,"R",2*i+3, "REJECT"]) # sampe 9
    # Case 1: Length of string is 2(ada 2 kasus doang)
    # only accepts 00 11 
    rules.append(["R",4,"R",13, "LEFT"])
    rules.append(["0",13,"0",14, "LEFT"])
    rules.append(["0",14,"0",14, "ACCEPT"])
    rules.append(["1",13,"1",15, "LEFT"])
    rules.append(["1",14,"1",14, "REJECT"])
    rules.append(["0",15,"0",15, "REJECT"])
    rules.append(["1",15,"1",15, "ACCEPT"])
    # Case 2: Length of string is 4 
    rules.append(["R", 6, "R", 16, "LEFT"]) # start
    rules.append(["0", 16, "X", 17, "LEFT"])
    rules.append(["1", 16, "X", 19, "LEFT"])
    rules.append(["X", 16, "X", 16, "LEFT"])
 
    rules.append(["0", 17, "0", 18, "LEFT"]) # pass the mid position
    rules.append(["1", 17, "1", 18, "LEFT"])
    rules.append(["1", 19, "1", 20, "LEFT"])
    rules.append(["0", 19, "0", 20, "LEFT"])
    rules.append(["X", 17, "X", 18, "LEFT"])
    rules.append(["X", 19, "X", 20, "LEFT"])
 
    rules.append(["0", 18, "X", 17, "LEFT"]) 
    rules.append(["1", 18, "X", 18, "REJECT"])
    rules.append(["0", 20, "X", 20, "REJECT"])
    rules.append(["1", 20, "X", 17, "LEFT"])
 
    rules.append(["L", 18, "L", 2, "RIGHT"]) # GO BACK RIGHT 
    rules.append(["L", 17, "L", 2, "RIGHT"]) # GO BACK RIGHT
    rules.append(["L", 16, "L", 16, "ACCEPT"]) # Halt
 
    # Case 3: Length of string is 6 
    rules.append(["R",8,"R",21, "LEFT"])
    rules.append(["0", 21, "X", 22, "LEFT"]) # 1 DIGIT
    rules.append(["1", 21, "X", 23, "LEFT"])
    rules.append(["X", 21, "X", 21, "LEFT"])
 
    rules.append(["0", 22, "0", 24, "LEFT"]) # pass the mid position (0 INFO), 2 DIGIT
    rules.append(["1", 22, "1", 24, "LEFT"])
    rules.append(["X", 22, "X", 24, "LEFT"]) # LEFT X'S
 
    rules.append(["1", 24, "1", 26, "LEFT"]) # 3 DIGIT
    rules.append(["0", 24, "0", 26, "LEFT"])
    rules.append(["X", 24, "X", 26, "LEFT"]) # LEFT X'S
 
    rules.append(["1", 26, "X", 22, "REJECT"]) #SAME 0 4TH DIGIT
    rules.append(["0", 26, "X", 22, "LEFT"])
 
    rules.append(["1", 23, "1", 25, "LEFT"]) # PASS THE MID (1 INFO) 2 DIGIT
    rules.append(["0", 23, "0", 25, "LEFT"])
    rules.append(["X", 23, "X", 25, "LEFT"]) # LEFT X'S
 
    rules.append(["1", 25, "1", 27, "LEFT"]) # 3 DIGIT
    rules.append(["0", 25, "0", 27, "LEFT"])
    rules.append(["X", 25, "X", 27, "LEFT"]) # LEFT X'S
   
    rules.append(["1", 27, "X", 23, "LEFT"]) #SAME 1 # 4TH DIGIT
    rules.append(["0", 27, "X", 23, "REJECT"])
    for i in range(22,28):
        rules.append(["L", i, "L", 2, "RIGHT"]) # GO BACK RIGHT 
   
    rules.append(["L", 21, "L", 21, "ACCEPT"]) # Halt
 
    # Case 4: Length of string is 8 (ada 16)
    rules.append(["R",10,"R",28, "LEFT"])
    rules.append(["0", 28, "X", 29, "LEFT"]) # 1 DIGIT
    rules.append(["1", 28, "X", 30, "LEFT"])
    rules.append(["X", 28, "X", 28, "LEFT"])
 
    for i in range(29,35,2):
        rules.append(["0", i, "0", i+2, "LEFT"]) # pass the mid position (0 INFO), 2 DIGIT
        rules.append(["1", i, "1", i+2, "LEFT"])
        rules.append(["X", i, "X", i+2, "LEFT"]) # LEFT X'S
 
    rules.append(["1", 35, "X", 29, "REJECT"]) #SAME 0 5TH DIGIT
    rules.append(["0", 35, "X", 29, "LEFT"])
    
    for i in range(30,36,2):
        rules.append(["0", i, "0", i+2, "LEFT"]) # pass the mid position (1 INFO), 2 DIGIT
        rules.append(["1", i, "1", i+2, "LEFT"])
        rules.append(["X", i, "X", i+2, "LEFT"]) # LEFT X'S
 
    rules.append(["1", 36, "X", 29, "LEFT"]) #SAME 1 # 5TH DIGIT
    rules.append(["0", 36, "X", 29, "REJECT"])
    for i in range(29,36):
        rules.append(["L", i, "L", 2, "RIGHT"]) # GO BACK RIGHT 
   
    rules.append(["L", 28, "L", 28, "ACCEPT"]) # Halt
    # Case 5: Length of string is 10 (ada 32)
    rules.append(["R",12,"R",37, "LEFT"])
    rules.append(["0", 37, "X", 38, "LEFT"]) # 1 DIGIT
    rules.append(["1", 37, "X", 39, "LEFT"])
    rules.append(["X", 37, "X", 37, "LEFT"])
 
    for i in range(38,46,2):
        rules.append(["0", i, "0", i+2, "LEFT"]) # pass the mid position (0 INFO), 2 DIGIT
        rules.append(["1", i, "1", i+2, "LEFT"])
        rules.append(["X", i, "X", i+2, "LEFT"]) # LEFT X'S
 
    rules.append(["1", 46, "X", 38, "REJECT"]) #SAME 0 5TH DIGIT
    rules.append(["0", 46, "X", 38, "LEFT"])
    
    for i in range(39,47,2):
        rules.append(["0", i, "0", i+2, "LEFT"]) # pass the mid position (1 INFO), 2 DIGIT
        rules.append(["1", i, "1", i+2, "LEFT"])
        rules.append(["X", i, "X", i+2, "LEFT"]) # LEFT X'S
 
    rules.append(["1", 47, "X", 39, "LEFT"]) #SAME 1 # 5TH DIGIT
    rules.append(["0", 47, "X", 39, "REJECT"])
    for i in range(38,48):
        rules.append(["L", i, "L", 2, "RIGHT"]) # GO BACK RIGHT 
   
    rules.append(["L", 37, "L", 37, "ACCEPT"]) # Halt
    return rules
    
# Versi lengkapnya
'''
def create_rules():
    rules = []
    # Hitung panjang string
    rules.append(("L", 1, "L", 2, "RIGHT"))
    
    # Loop for symbols "0", "1", "X" 
    # i=0
    rules.append(("0", 2, "0", 3, "RIGHT"))
    rules.append(("1", 2, "1", 3, "RIGHT"))
    rules.append(("X", 2, "X", 3, "RIGHT"))
    # i=1
    rules.append(("0", 3, "0", 4, "RIGHT"))
    rules.append(("1", 3, "1", 4, "RIGHT"))
    rules.append(("X", 3, "X", 4, "RIGHT"))
    # i=2
    rules.append(("0", 4, "0", 5, "RIGHT"))
    rules.append(("1", 4, "1", 5, "RIGHT"))
    rules.append(("X", 4, "X", 5, "RIGHT"))
    # i=3
    rules.append(("0", 5, "0", 6, "RIGHT"))
    rules.append(("1", 5, "1", 6, "RIGHT"))
    rules.append(("X", 5, "X", 6, "RIGHT"))
    # i=4
    rules.append(("0", 6, "0", 7, "RIGHT"))
    rules.append(("1", 6, "1", 7, "RIGHT"))
    rules.append(("X", 6, "X", 7, "RIGHT"))
    # i=5
    rules.append(("0", 7, "0", 8, "RIGHT"))
    rules.append(("1", 7, "1", 8, "RIGHT"))
    rules.append(("X", 7, "X", 8, "RIGHT"))
    # i=6
    rules.append(("0", 8, "0", 9, "RIGHT"))
    rules.append(("1", 8, "1", 9, "RIGHT"))
    rules.append(("X", 8, "X", 9, "RIGHT"))
    # i=7
    rules.append(("0", 9, "0", 10, "RIGHT"))
    rules.append(("1", 9, "1", 10, "RIGHT"))
    rules.append(("X", 9, "X", 10, "RIGHT"))
    # i=8
    rules.append(("0", 10, "0", 11, "RIGHT"))
    rules.append(("1", 10, "1", 11, "RIGHT"))
    rules.append(("X", 10, "X", 11, "RIGHT"))
    # i=9
    rules.append(("0", 11, "0", 12, "RIGHT"))
    rules.append(("1", 11, "1", 12, "RIGHT"))
    rules.append(("X", 11, "X", 12, "RIGHT"))
 
    # Case 0: Panjang string 0
    rules.append(("R", 2, "R", 2, "REJECT"))
    
    # REJECT semua states ganjil
    rules.append(("R", 3, "R", 3, "REJECT"))  # i=0
    rules.append(("R", 5, "R", 5, "REJECT"))  # i=1
    rules.append(("R", 7, "R", 7, "REJECT"))  # i=2
    rules.append(("R", 9, "R", 9, "REJECT"))  # i=3
 
    # Case 1: Panjang string 2
    rules.append(("R", 4, "R", 13, "LEFT"))
    rules.append(("0", 13, "0", 14, "LEFT"))
    rules.append(("0", 14, "0", 14, "ACCEPT"))
    rules.append(("1", 13, "1", 15, "LEFT"))
    rules.append(("1", 14, "1", 14, "REJECT"))
    rules.append(("0", 15, "0", 15, "REJECT"))
    rules.append(("1", 15, "1", 15, "ACCEPT"))
 
    # Case 2: Panjang string 4
    rules.append(("R", 6, "R", 16, "LEFT"))
    rules.append(("0", 16, "X", 17, "LEFT"))
    rules.append(("1", 16, "X", 19, "LEFT"))
    rules.append(("X", 16, "X", 16, "LEFT"))
    rules.append(("0", 17, "0", 18, "LEFT"))
    rules.append(("1", 17, "1", 18, "LEFT"))
    rules.append(("1", 19, "1", 20, "LEFT"))
    rules.append(("0", 19, "0", 20, "LEFT"))
    rules.append(("X", 17, "X", 18, "LEFT"))
    rules.append(("X", 19, "X", 20, "LEFT"))
    rules.append(("0", 18, "X", 17, "LEFT"))
    rules.append(("1", 18, "X", 18, "REJECT"))
    rules.append(("0", 20, "X", 20, "REJECT"))
    rules.append(("1", 20, "X", 17, "LEFT"))
    rules.append(("L", 18, "L", 2, "RIGHT"))
    rules.append(("L", 17, "L", 2, "RIGHT"))
    rules.append(("L", 16, "L", 16, "ACCEPT"))
 
    # Case 3: Panjang string 6
    rules.append(("R", 8, "R", 21, "LEFT"))
    rules.append(("0", 21, "X", 22, "LEFT"))
    rules.append(("1", 21, "X", 23, "LEFT"))
    rules.append(("X", 21, "X", 21, "LEFT"))
    rules.append(("0", 22, "0", 24, "LEFT"))
    rules.append(("1", 22, "1", 24, "LEFT"))
    rules.append(("X", 22, "X", 24, "LEFT"))
    rules.append(("1", 24, "1", 26, "LEFT"))
    rules.append(("0", 24, "0", 26, "LEFT"))
    rules.append(("X", 24, "X", 26, "LEFT"))
    rules.append(("1", 26, "X", 22, "REJECT"))
    rules.append(("0", 26, "X", 22, "LEFT"))
    rules.append(("1", 23, "1", 25, "LEFT"))
    rules.append(("0", 23, "0", 25, "LEFT"))
    rules.append(("X", 23, "X", 25, "LEFT"))
    rules.append(("1", 25, "1", 27, "LEFT"))
    rules.append(("0", 25, "0", 27, "LEFT"))
    rules.append(("X", 25, "X", 27, "LEFT"))
    rules.append(("1", 27, "X", 23, "LEFT"))
    rules.append(("0", 27, "X", 23, "REJECT"))
    rules.append(("L", 21, "L", 21, "ACCEPT"))
    rules.append(("L", 22, "L", 2, "RIGHT"))
    rules.append(("L", 23, "L", 2, "RIGHT"))
    rules.append(("L", 24, "L", 2, "RIGHT"))
    rules.append(("L", 25, "L", 2, "RIGHT"))
    rules.append(("L", 26, "L", 2, "RIGHT"))
    rules.append(("L", 27, "L", 2, "RIGHT"))
 
    # Case 4: Panjang string 8
    rules.append(("R", 10, "R", 28, "LEFT"))
    rules.append(("0", 28, "X", 29, "LEFT"))
    rules.append(("1", 28, "X", 30, "LEFT"))
    rules.append(("X", 28, "X", 28, "LEFT"))
    rules.append(("0", 29, "0", 31, "LEFT"))
    rules.append(("1", 29, "1", 31, "LEFT"))
    rules.append(("X", 29, "X", 31, "LEFT"))
    rules.append(("0", 31, "0", 33, "LEFT"))
    rules.append(("1", 31, "1", 33, "LEFT"))
    rules.append(("X", 31, "X", 33, "LEFT"))
    rules.append(("0", 33, "0", 35, "LEFT"))
    rules.append(("1", 33, "1", 35, "LEFT"))
    rules.append(("X", 33, "X", 35, "LEFT"))
    rules.append(("0", 30, "0", 32, "LEFT"))
    rules.append(("1", 30, "1", 32, "LEFT"))
    rules.append(("X", 30, "X", 32, "LEFT"))
    rules.append(("0", 32, "0", 34, "LEFT"))
    rules.append(("1", 32, "1", 34, "LEFT"))
    rules.append(("X", 32, "X", 34, "LEFT"))
    rules.append(("0", 34, "0", 36, "LEFT"))
    rules.append(("1", 34, "1", 36, "LEFT"))
    rules.append(("X", 34, "X", 36, "LEFT"))
    rules.append(("1", 35, "X", 29, "REJECT"))
    rules.append(("0", 35, "X", 29, "LEFT"))
    rules.append(("1", 36, "X", 29, "LEFT"))
    rules.append(("0", 36, "X", 29, "REJECT"))
    rules.append(("L", 29, "L", 2, "RIGHT"))
    rules.append(("L", 30, "L", 2, "RIGHT"))
    rules.append(("L", 31, "L", 2, "RIGHT"))
    rules.append(("L", 32, "L", 2, "RIGHT"))
    rules.append(("L", 33, "L", 2, "RIGHT"))
    rules.append(("L", 34, "L", 2, "RIGHT"))
    rules.append(("L", 35, "L", 2, "RIGHT"))
    rules.append(("L", 36, "L", 2, "RIGHT"))
    rules.append(("L", 28, "L", 28, "ACCEPT"))
 
    # Case 5: panjang string 10
    rules.append(("R", 12, "R", 37, "LEFT"))
    rules.append(("0", 37, "X", 38, "LEFT"))
    rules.append(("1", 37, "X", 39, "LEFT"))
    rules.append(("X", 37, "X", 37, "LEFT"))
    rules.append(("0", 38, "0", 40, "LEFT"))
    rules.append(("1", 38, "1", 40, "LEFT"))
    rules.append(("X", 38, "X", 40, "LEFT"))
    rules.append(("0", 40, "0", 42, "LEFT"))
    rules.append(("1", 40, "1", 42, "LEFT"))
    rules.append(("X", 40, "X", 42, "LEFT"))
    rules.append(("0", 42, "0", 44, "LEFT"))
    rules.append(("1", 42, "1", 44, "LEFT"))
    rules.append(("X", 42, "X", 44, "LEFT"))
    rules.append(("0", 44, "0", 46, "LEFT"))
    rules.append(("1", 44, "1", 46, "LEFT"))
    rules.append(("X", 44, "X", 46, "LEFT"))
    rules.append(("0", 39, "0", 41, "LEFT"))
    rules.append(("1", 39, "1", 41, "LEFT"))
    rules.append(("X", 39, "X", 41, "LEFT"))
    rules.append(("0", 41, "0", 43, "LEFT"))
    rules.append(("1", 41, "1", 43, "LEFT"))
    rules.append(("X", 41, "X", 43, "LEFT"))
    rules.append(("0", 43, "0", 45, "LEFT"))
    rules.append(("1", 43, "1", 45, "LEFT"))
    rules.append(("X", 43, "X", 45, "LEFT"))
    rules.append(("0", 45, "0", 47, "LEFT"))
    rules.append(("1", 45, "1", 47, "LEFT"))
    rules.append(("X", 45, "X", 47, "LEFT"))
    rules.append(("1", 46, "X", 38, "REJECT"))
    rules.append(("0", 46, "X", 38, "LEFT"))
    rules.append(("1", 47, "X", 39, "LEFT"))
    rules.append(("0", 47, "X", 39, "REJECT"))
    rules.append(("L", 38, "L", 2, "RIGHT"))
    rules.append(("L", 39, "L", 2, "RIGHT"))
    rules.append(("L", 40, "L", 2, "RIGHT"))
    rules.append(("L", 41, "L", 2, "RIGHT"))
    rules.append(("L", 42, "L", 2, "RIGHT"))
    rules.append(("L", 43, "L", 2, "RIGHT"))
    rules.append(("L", 44, "L", 2, "RIGHT"))
    rules.append(("L", 45, "L", 2, "RIGHT"))
    rules.append(("L", 46, "L", 2, "RIGHT"))
    rules.append(("L", 47, "L", 2, "RIGHT"))
    rules.append(("L", 37, "L", 37, "ACCEPT"))
 
    return rules
'''