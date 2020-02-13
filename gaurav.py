# =============================================================================
# CODES COMPILATION GAURAV
# =============================================================================

import pygame
import copy
import time
import string
from pramurta import get_user_location

def password_strength(password):
    '''
    Generates a password
    Checks Validity of password
    Checks Password strength
    '''
    upper  = 0
    lower = 0
    number = 0
    #print("Your passowrd needs to have atleast 1 number, 1 Lowercase letter, and 1 Uppercase letter\n\
            #Your password needs to have atleast 6 characters")
   
    #new_password = input ("Please enter new password \t:")
    
    for char in list(password):
    
        if char in list(string.ascii_lowercase):
            lower = lower + 1
        elif char in list(string.ascii_uppercase):
            upper = upper + 1
        elif char in ['0', '1', '2', '3', '4', '5', '6', '8', '9']:
            number = number +1 
    
    if upper == 0 or lower == 0 or number == 0 or len(password)<6:
        return False

    else:
        return True
        
       
    
def create_new_account(username,password, login_file, ret_login_file): # returns 1: Account Created, 2: Username already exit, 3:Password not string
    '''
    Creates a New Account for the user
    Gnerates the Usernamer
    '''
    
    #print ("\nCreate an account. \n It's free and always will be. ")
   

   # while True:
     #   new_username = input ("Please enter unique user name \t:")

    userpass_database = ret_login_file()
    
    if username in userpass_database:
        
        return 2

    else:

        if(not password_strength(password)):
            return 3


        else:

            login_file(username, password)
            return 1




def check_username_password(user_name,password, ret_login_file): #returns 1: Correct credentials, 2: invalid username, 3: invalid password
    '''
    Once the username and password has been created, the user can login using this function
    '''
    userpass_database = ret_login_file()
    
    if user_name not in userpass_database:
        return 2

    elif password != (userpass_database[user_name]):
        return 3
    
    else:
        return 1

    
        
def get_distance(t1, t2):
    '''
    Returns the distance in meters between thw two coordinates
    Distance is rounded off to 2 decimal places
    t1 and t2 are tuples representing the coordinates
    '''
    ans =(100/60.3)*((t1[0]-t2[0])**2+(t1[1]-t2[1])**2)**(1/2)
    return (round(ans, 2))




# Dictionary mapping Nodes to Coordinates 
nodes_dict = {"A":(857, 248), "B":(797, 242), "C":(741, 245), "D":(706, 247), "E":(645, 253), "F":(589, 223), "G":(532, 160), "H":(408, 165), "I":(371, 228), "J":(340, 303), "K":(391, 367), "L":(365, 402), "M":(320, 445), "N":(267, 545), "O":(216, 607), "P":(158, 668), "Q":(130, 702), "R":(139, 787), "S":(274, 876), "T":(368, 888), "U":(459, 804), "V":(545, 819), "W":(569, 840), "X":(631, 913), "Y":(684, 930), "Z":(766, 932), "AA":(835, 945), "BB":(879, 947), "CC":(911, 920), "ZZ":(1023, 833), "DD":(1108, 731), "EE":(1135, 705), "FF":(1157, 677), "GG":(1197, 608), "HH":(1231, 475), "II":(1232, 437), "JJ":(1227, 388), "KK":(1209, 340), "LL":(1171, 311), "MM":(1115, 294), "NN":(1062, 282), "OO":(973, 265),"PP":(943, 259),"QQ":(896, 253), "A1":(853, 271), "B1":(791, 286), "B2":(820, 289), "B3":(867, 301), "B4":(726, 296), "CD":(724, 271), "E1":(656, 301), "E2":(661, 330), "E21":(729, 331), "E3":(651, 363), "E31":(722, 359), "E4":(646, 389), "EF":(645, 451), "E5":(607, 495), "E6":(572, 529), "K1":(450, 402), "K2":(478, 407), "K3":(538, 424), "K4":(592, 439), "K5":(714, 470), "K6":(797, 494), "KII":(822, 561), "K7":(822, 619), "K8":(839, 640), "K81":(933, 613), "K82":(951, 645), "K9":(846, 682), "K91":(896, 702), "K92":(919, 733), "K10":(813, 722), "K11":(778, 762), "KZ":(780, 818), "N1":(326, 567), "P1":(171, 681), "P11":(189, 666), "P12":(218, 682), "P13":(274, 683), "P2":(199, 709), "P3":(228, 713), "P31":(210, 745), "PS":(279, 714), "P4":(324, 713), "S1":(267, 819), "S2":(286, 787), "U1":(428, 768), "U11":(452, 699), "U2":(394, 753), "U3":(353, 762), "U4":(354, 607), "UII":(392, 644), "W1":(584, 815), "W11":(550, 782), "W12":(621, 692), "W2":(653, 740), "W3":(707, 753), "W4":(733, 805), "W5":(697, 857), "W6":(655, 849), "W7":(662, 778), "W8":(700, 792), "WZ":(726, 725), "Z1":(773, 890), "Z11":(792, 902), "Z2":(741, 718), "CC1":(887, 897), "CC2":(855, 901), "CC3":(837, 865), "DD1":(1060, 686), "DD2":(1031, 637), "EE1":(1097, 668), "EE2":(1080, 650), "II1":(1177, 430), "II2":(1101, 442), "II21":(1103, 399), "II22":(1117, 380), "II3":(966, 492),"II31":(960, 470), "II311":(916, 491), "II32":(960, 449), "II4":(900, 554), "II41":(952, 585), "II42":(988, 592), "II43":(1073, 533), "II44":(1121, 585), "II5":(705, 554), "II6":(646, 625), "II7":(574, 647), "II8":(512, 628), "II81":(465, 568), "II9":(443, 630), "II91":(402, 589), "MM1":(1112, 317), "MM2":(1156, 351)}

# Graph in function form
graph_f = {"A":{'QQ':get_distance(nodes_dict["A"], nodes_dict["QQ"]),'B':get_distance(nodes_dict["A"], nodes_dict["B"]),'A1':get_distance(nodes_dict["A"], nodes_dict["A1"])}, "B":{'C':get_distance(nodes_dict["C"], nodes_dict["B"]),'B1':get_distance(nodes_dict["B1"], nodes_dict["B"]), 'A':get_distance(nodes_dict["A"], nodes_dict["B"])}, 'C':{'B':get_distance(nodes_dict["B"], nodes_dict["C"]),'CD':get_distance(nodes_dict["B"], nodes_dict["CD"]), 'D':get_distance(nodes_dict["D"], nodes_dict["B"])}, "D":{'E':get_distance(nodes_dict["D"], nodes_dict["E"]),'CD':get_distance(nodes_dict["D"], nodes_dict["CD"]), 'C':get_distance(nodes_dict["D"], nodes_dict["C"])}, "E":{'F':get_distance(nodes_dict["E"], nodes_dict["F"]),'E1':get_distance(nodes_dict["E"], nodes_dict["E1"]), 'D':get_distance(nodes_dict["E"], nodes_dict["D"])}, "F":{'G':get_distance(nodes_dict["F"], nodes_dict["G"]),'E':get_distance(nodes_dict["F"], nodes_dict["E"])}, "G":{'H':get_distance(nodes_dict["G"], nodes_dict["H"]),'F':get_distance(nodes_dict["G"], nodes_dict["F"]), 'D':get_distance(nodes_dict["G"], nodes_dict["D"])}, "H":{'I':get_distance(nodes_dict["H"], nodes_dict["I"]), 'G':get_distance(nodes_dict["H"], nodes_dict["G"])}, "I":{'J':get_distance(nodes_dict["I"], nodes_dict["J"]),'H':get_distance(nodes_dict["I"], nodes_dict["H"])}, "J":{'I':get_distance(nodes_dict["J"], nodes_dict["I"]),'K':get_distance(nodes_dict["J"], nodes_dict["K"])}, "K":{'J':get_distance(nodes_dict["K"], nodes_dict["J"]),'K1':get_distance(nodes_dict["K"], nodes_dict["K1"]), 'L':get_distance(nodes_dict["K"], nodes_dict["L"])}, "L":{'K':get_distance(nodes_dict["L"], nodes_dict["K"]),'M':get_distance(nodes_dict["L"], nodes_dict["M"])}, "M":{'L':get_distance(nodes_dict["M"], nodes_dict["L"]),'N':get_distance(nodes_dict["M"], nodes_dict["N"])}, "N":{'M':get_distance(nodes_dict["N"], nodes_dict["M"]),'N1':get_distance(nodes_dict["N"], nodes_dict["N1"]), 'O':get_distance(nodes_dict["N"], nodes_dict["O"])}, "O":{'N':get_distance(nodes_dict["O"], nodes_dict["N"]),'P':get_distance(nodes_dict["O"], nodes_dict["P"])}, "P":{'O':get_distance(nodes_dict["P"], nodes_dict["O"]),'P1':get_distance(nodes_dict["P"], nodes_dict["P1"]), 'Q':get_distance(nodes_dict["P"], nodes_dict["Q"])}, "Q":{'P':get_distance(nodes_dict["Q"], nodes_dict["P"]),'R':get_distance(nodes_dict["Q"], nodes_dict["R"])}, "R":{'Q':get_distance(nodes_dict["R"], nodes_dict["Q"]),'S':get_distance(nodes_dict["R"], nodes_dict["S"])}, "S":{'R':get_distance(nodes_dict["S"], nodes_dict["R"]),'S1':get_distance(nodes_dict["S"], nodes_dict["S1"]), 'T':get_distance(nodes_dict["S"], nodes_dict["T"])}, "T":{'S':get_distance(nodes_dict["T"], nodes_dict["S"]),'U':get_distance(nodes_dict["T"], nodes_dict["U"])}, "U":{'T':get_distance(nodes_dict["U"], nodes_dict["T"]),'U1':get_distance(nodes_dict["U"], nodes_dict["U1"]), 'V':get_distance(nodes_dict["U"], nodes_dict["V"])}, "V":{'U':get_distance(nodes_dict["V"], nodes_dict["U"]),'W':get_distance(nodes_dict["V"], nodes_dict["W"])}, "W":{'V':get_distance(nodes_dict["W"], nodes_dict["V"]),'W1':get_distance(nodes_dict["W"], nodes_dict["W1"]), 'X':get_distance(nodes_dict["W"], nodes_dict["X"])}, "X":{'W':get_distance(nodes_dict["X"], nodes_dict["W"]),'Y':get_distance(nodes_dict["X"], nodes_dict["Y"])}, "Y":{'X':get_distance(nodes_dict["Y"], nodes_dict["X"]),'Z':get_distance(nodes_dict["Y"], nodes_dict["Z"])}, "Z":{'Y':get_distance(nodes_dict["Z"], nodes_dict["Y"]),'Z1':get_distance(nodes_dict["Z"], nodes_dict["Z1"]), 'AA':get_distance(nodes_dict["Z"], nodes_dict["AA"])}, "AA":{'Z':get_distance(nodes_dict["AA"], nodes_dict["Z"]),'BB':get_distance(nodes_dict["AA"], nodes_dict["BB"])}, "BB":{'AA':get_distance(nodes_dict["BB"], nodes_dict["AA"]),'CC':get_distance(nodes_dict["BB"], nodes_dict["CC"])}, "CC":{'BB':get_distance(nodes_dict["CC"], nodes_dict["BB"]),'CC1':get_distance(nodes_dict["CC"], nodes_dict["CC1"]), 'ZZ':get_distance(nodes_dict["CC"], nodes_dict["ZZ"])}, "ZZ":{'CC':get_distance(nodes_dict["ZZ"], nodes_dict["CC"]),'DD':get_distance(nodes_dict["ZZ"], nodes_dict["DD"])}, "DD":{'ZZ':get_distance(nodes_dict["DD"], nodes_dict["ZZ"]),'DD1':get_distance(nodes_dict["DD"], nodes_dict["DD1"]), 'EE':get_distance(nodes_dict["DD"], nodes_dict["EE"])}, "EE":{'DD':get_distance(nodes_dict["EE"], nodes_dict["DD"]),'EE1':get_distance(nodes_dict["EE"], nodes_dict["EE1"]), 'FF':get_distance(nodes_dict["EE"], nodes_dict["FF"])}, "FF":{'EE':get_distance(nodes_dict["FF"], nodes_dict["EE"]),'GG':get_distance(nodes_dict["FF"], nodes_dict["GG"])}, "GG":{'FF':get_distance(nodes_dict["GG"], nodes_dict["FF"]),'HH':get_distance(nodes_dict["GG"], nodes_dict["HH"])}, "HH":{'GG':get_distance(nodes_dict["HH"], nodes_dict["GG"]),'II':get_distance(nodes_dict["HH"], nodes_dict["II"])}, "II":{'HH':get_distance(nodes_dict["II"], nodes_dict["HH"]),'II1':get_distance(nodes_dict["II"], nodes_dict["II1"]), 'JJ':get_distance(nodes_dict["II"], nodes_dict["JJ"])}, "JJ":{'II':get_distance(nodes_dict["JJ"], nodes_dict["II"]),'KK':get_distance(nodes_dict["JJ"], nodes_dict["KK"])}, "KK":{'JJ':get_distance(nodes_dict["KK"], nodes_dict["JJ"]),'LL':get_distance(nodes_dict["KK"], nodes_dict["LL"])}, "LL":{'KK':get_distance(nodes_dict["LL"], nodes_dict["KK"]),'MM':get_distance(nodes_dict["LL"], nodes_dict["MM"])}, "MM":{'LL':get_distance(nodes_dict["MM"], nodes_dict["LL"]),'MM1':get_distance(nodes_dict["MM"], nodes_dict["MM1"]), 'NN':get_distance(nodes_dict["MM"], nodes_dict["NN"])}, "NN":{'MM':get_distance(nodes_dict["NN"], nodes_dict["MM"]),'OO':get_distance(nodes_dict["NN"], nodes_dict["OO"])}, "OO":{'NN':get_distance(nodes_dict["OO"], nodes_dict["NN"]),'PP':get_distance(nodes_dict["OO"], nodes_dict["PP"])},"PP":{'OO':get_distance(nodes_dict["PP"], nodes_dict["OO"]),'QQ':get_distance(nodes_dict["PP"], nodes_dict["QQ"])},"QQ":{'PP':get_distance(nodes_dict["QQ"], nodes_dict["PP"]),'A':get_distance(nodes_dict["QQ"], nodes_dict["A"])}, "A1":{'A':get_distance(nodes_dict["A1"], nodes_dict["A"]), 'B2':get_distance(nodes_dict["A1"], nodes_dict["B2"]), 'B3':get_distance(nodes_dict["A1"], nodes_dict["B3"])}, "B1":{'B':get_distance(nodes_dict["B1"], nodes_dict["B"]),'B4':get_distance(nodes_dict["B1"], nodes_dict["B4"]), 'B2':get_distance(nodes_dict["B1"], nodes_dict["B2"])}, "B2":{'B1':get_distance(nodes_dict["B2"], nodes_dict["B1"]),'B3':get_distance(nodes_dict["B2"], nodes_dict["B3"]), 'A1':get_distance(nodes_dict["B2"], nodes_dict["A1"])}, "B3":{'B2':get_distance(nodes_dict["B3"], nodes_dict["B2"]), 'A1':get_distance(nodes_dict["B3"], nodes_dict["A1"])}, "B4":{'B1':get_distance(nodes_dict["B4"], nodes_dict["B1"]),'CD':get_distance(nodes_dict["B4"], nodes_dict["CD"]), 'E1':get_distance(nodes_dict["B4"], nodes_dict["E1"]), 'E21':get_distance(nodes_dict["B4"], nodes_dict["E21"])}, "CD":{'C':get_distance(nodes_dict["CD"], nodes_dict["C"]),'D':get_distance(nodes_dict["CD"], nodes_dict["D"]), 'B4':get_distance(nodes_dict["CD"], nodes_dict["B4"])}, "E1":{'E':get_distance(nodes_dict["E1"], nodes_dict["E"]),'E2':get_distance(nodes_dict["E1"], nodes_dict["E2"])}, "E2":{'E1':get_distance(nodes_dict["E2"], nodes_dict["E1"]),'E21':get_distance(nodes_dict["E2"], nodes_dict["E21"]), 'E3':get_distance(nodes_dict["E2"], nodes_dict["E3"])}, "E21":{'E2':get_distance(nodes_dict["E21"], nodes_dict["E2"]),'B4':get_distance(nodes_dict["E21"], nodes_dict["B4"]), 'E31':get_distance(nodes_dict["E21"], nodes_dict["E31"])}, "E3":{'E2':get_distance(nodes_dict["E3"], nodes_dict["E2"]),'E31':get_distance(nodes_dict["E3"], nodes_dict["E31"]), 'E4':get_distance(nodes_dict["E3"], nodes_dict["E4"])}, "E31":{'E3':get_distance(nodes_dict["E31"], nodes_dict["E3"]),'E21':get_distance(nodes_dict["E31"], nodes_dict["E21"])}, "E4":{'E3':get_distance(nodes_dict["E4"], nodes_dict["E3"]),'EF':get_distance(nodes_dict["E4"], nodes_dict["EF"]), 'K4':get_distance(nodes_dict["E4"], nodes_dict["K4"])}, "EF":{'E4':get_distance(nodes_dict["EF"], nodes_dict["E4"]),'K5':get_distance(nodes_dict["EF"], nodes_dict["K5"]), 'E5':get_distance(nodes_dict["EF"], nodes_dict["E5"]), 'K4':get_distance(nodes_dict["EF"], nodes_dict["K4"])}, "E5":{'EF':get_distance(nodes_dict["E5"], nodes_dict["EF"]),'E6':get_distance(nodes_dict["E5"], nodes_dict["E6"])}, "E6":{'E5':get_distance(nodes_dict["E6"], nodes_dict["E5"])}, "K1":{'K':get_distance(nodes_dict["K1"], nodes_dict["K"]),'K2':get_distance(nodes_dict["K1"], nodes_dict["K2"])}, "K2":{'K1':get_distance(nodes_dict["K2"], nodes_dict["K1"]),'K3':get_distance(nodes_dict["K2"], nodes_dict["K3"])}, "K3":{'K2':get_distance(nodes_dict["K3"], nodes_dict["K2"]),'K4':get_distance(nodes_dict["K3"], nodes_dict["K4"]),'II81': get_distance(nodes_dict["K3"], nodes_dict["II81"]),'II91':get_distance(nodes_dict["K3"], nodes_dict["II91"])}, "K4":{'K3':get_distance(nodes_dict["K4"], nodes_dict["K3"]),'EF':get_distance(nodes_dict["K4"], nodes_dict["EF"])}, "K5":{'EF':get_distance(nodes_dict["K5"], nodes_dict["EF"]),'K6':get_distance(nodes_dict["K5"], nodes_dict["K6"])}, "K6":{'K5':get_distance(nodes_dict["K6"], nodes_dict["K5"]),'KII':get_distance(nodes_dict["K6"], nodes_dict["KII"])}, "KII":{'K6':get_distance(nodes_dict["KII"], nodes_dict["K6"]),'II4':get_distance(nodes_dict["KII"], nodes_dict["II4"]), 'K7':get_distance(nodes_dict["KII"], nodes_dict["K7"]), 'II5':get_distance(nodes_dict["KII"], nodes_dict["II5"])}, "K7":{'KII':get_distance(nodes_dict["K7"], nodes_dict["KII"]),'K8':get_distance(nodes_dict["K7"], nodes_dict["K8"])}, "K8":{'K7':get_distance(nodes_dict["K8"], nodes_dict["K7"]),'K81':get_distance(nodes_dict["K8"], nodes_dict["K81"]), 'K9':get_distance(nodes_dict["K8"], nodes_dict["K9"]), 'Z2':get_distance(nodes_dict["K8"], nodes_dict["Z2"])}, "K81":{'K8':get_distance(nodes_dict["K81"], nodes_dict["K8"]),'K82':get_distance(nodes_dict["K81"], nodes_dict["K82"])}, "K82":{'K81':get_distance(nodes_dict["K82"], nodes_dict["K81"])}, "K9":{'K8':get_distance(nodes_dict["K9"], nodes_dict["K8"]),'K91':get_distance(nodes_dict["K9"], nodes_dict["K91"]), 'K10':get_distance(nodes_dict["K9"], nodes_dict["K10"])}, "K91":{'K9':get_distance(nodes_dict["K91"], nodes_dict["K9"]),'K92':get_distance(nodes_dict["K91"], nodes_dict["K92"])}, "K92":{'K91':get_distance(nodes_dict["K92"], nodes_dict["K91"])}, "K10":{'K9':get_distance(nodes_dict["K10"], nodes_dict["K9"]),'K11':get_distance(nodes_dict["K10"], nodes_dict["K11"])}, "K11":{'K10':get_distance(nodes_dict["K11"], nodes_dict["K10"]),'Z2':get_distance(nodes_dict["K11"], nodes_dict["Z2"]), 'KZ':get_distance(nodes_dict["K11"], nodes_dict["KZ"])}, "KZ":{'Z2':get_distance(nodes_dict["KZ"], nodes_dict["Z2"]),'K11':get_distance(nodes_dict["KZ"], nodes_dict["K11"]), 'Z1':get_distance(nodes_dict["KZ"], nodes_dict["Z1"])}, "N1":{'N':get_distance(nodes_dict["N1"], nodes_dict["N"]), 'II91':get_distance(nodes_dict["N1"], nodes_dict["II91"])}, "P1":{'P':get_distance(nodes_dict["P1"], nodes_dict["P"]),'P11':get_distance(nodes_dict["P1"], nodes_dict["P11"]), 'P2':get_distance(nodes_dict["P1"], nodes_dict["P2"])}, "P11":{'P1':get_distance(nodes_dict["P11"], nodes_dict["P1"]),'P12':get_distance(nodes_dict["P11"], nodes_dict["P12"])}, "P12":{'P11':get_distance(nodes_dict["P12"], nodes_dict["P11"]),'P2':get_distance(nodes_dict["P12"], nodes_dict["P2"]), 'P3':get_distance(nodes_dict["P12"], nodes_dict["P3"]), 'P13':get_distance(nodes_dict["P12"], nodes_dict["P13"])}, "P13":{'P12':get_distance(nodes_dict["P13"], nodes_dict["P12"]), 'PS':get_distance(nodes_dict["P13"], nodes_dict["PS"])}, "P2":{'P1':get_distance(nodes_dict["P2"], nodes_dict["P1"]),'P3':get_distance(nodes_dict["P2"], nodes_dict["P3"])}, "P3":{'P2':get_distance(nodes_dict["P3"], nodes_dict["P2"]),'P12':get_distance(nodes_dict["P3"], nodes_dict["P12"]), 'P31':get_distance(nodes_dict["P3"], nodes_dict["P31"]), 'PS':get_distance(nodes_dict["P3"], nodes_dict["PS"])}, "P31":{'P3':get_distance(nodes_dict["P31"], nodes_dict["P3"])}, "PS":{'P3':get_distance(nodes_dict["PS"], nodes_dict["P3"]), 'P13':get_distance(nodes_dict["PS"], nodes_dict["P13"]), 'S2':get_distance(nodes_dict["PS"], nodes_dict["S2"]), 'P4':get_distance(nodes_dict["PS"], nodes_dict["P4"])}, "P4":{'PS':get_distance(nodes_dict["P4"], nodes_dict["PS"]), 'U2':get_distance(nodes_dict["P4"], nodes_dict["U2"])}, "S1":{'S':get_distance(nodes_dict["S1"], nodes_dict["S"]), 'S2':get_distance(nodes_dict["S1"], nodes_dict["S2"])}, "S2":{'S1':get_distance(nodes_dict["S2"], nodes_dict["S1"]), 'PS':get_distance(nodes_dict["S2"], nodes_dict["PS"])}, "U1":{'U':get_distance(nodes_dict["U1"], nodes_dict["U"]), 'U2':get_distance(nodes_dict["U1"], nodes_dict["U2"]), 'U11':get_distance(nodes_dict["U1"], nodes_dict["U11"])}, "U11":{'U1':get_distance(nodes_dict["U11"], nodes_dict["U1"])}, "U2":{'U1':get_distance(nodes_dict["U2"], nodes_dict["U1"]), 'P4':get_distance(nodes_dict["U2"], nodes_dict["P4"]), 'UII':get_distance(nodes_dict["U2"], nodes_dict["UII"])}, "UII":{'U2':get_distance(nodes_dict["UII"], nodes_dict["U2"]), 'II9':get_distance(nodes_dict["U11"], nodes_dict["II9"])}, "W1":{'W':get_distance(nodes_dict["W1"], nodes_dict["W"]), 'W11':get_distance(nodes_dict["W1"], nodes_dict["W11"]), 'W2':get_distance(nodes_dict["W1"], nodes_dict["W2"])}, "W11":{'W1':get_distance(nodes_dict["W11"], nodes_dict["W1"]), 'W12':get_distance(nodes_dict["W11"], nodes_dict["W12"])}, "W12":{'W11':get_distance(nodes_dict["W12"], nodes_dict["W11"]), 'WZ':get_distance(nodes_dict["W12"], nodes_dict["WZ"])}, "W2":{'W1':get_distance(nodes_dict["W2"], nodes_dict["W1"]), 'W3':0}, "W3":{'W2':get_distance(nodes_dict["W3"], nodes_dict["W2"]), 'WZ':get_distance(nodes_dict["W3"], nodes_dict["WZ"]), 'W4':get_distance(nodes_dict["W3"], nodes_dict["W4"])}, "W4":{'W3':get_distance(nodes_dict["W4"], nodes_dict["W3"]), 'W5':get_distance(nodes_dict["W4"], nodes_dict["W5"])}, "W5":{'W4':get_distance(nodes_dict["W5"], nodes_dict["W4"]), 'W6':get_distance(nodes_dict["W5"], nodes_dict["W6"])}, "W6":{'W5':get_distance(nodes_dict["W6"], nodes_dict["W5"]), 'W7':get_distance(nodes_dict["W6"], nodes_dict["W7"])}, "W7":{'W6':get_distance(nodes_dict["W7"], nodes_dict["W6"]), 'W8':get_distance(nodes_dict["W7"], nodes_dict["W8"])}, "W8":{'W7':get_distance(nodes_dict["W8"], nodes_dict["W7"])}, "WZ":{'W12':get_distance(nodes_dict["WZ"], nodes_dict["W12"]), 'W3':get_distance(nodes_dict["WZ"], nodes_dict["W3"]),'Z2':get_distance(nodes_dict["WZ"], nodes_dict["Z2"])}, "Z1":{'Z':get_distance(nodes_dict["Z1"], nodes_dict["Z"]), 'KZ':get_distance(nodes_dict["Z1"], nodes_dict["KZ"]), 'Z11':get_distance(nodes_dict["Z1"], nodes_dict["Z11"])}, "Z11":{'Z1':get_distance(nodes_dict["Z11"], nodes_dict["Z1"]), 'CC3':get_distance(nodes_dict["Z11"], nodes_dict["CC3"])}, "Z2":{'KZ':get_distance(nodes_dict["Z2"], nodes_dict["KZ"]), 'K11':get_distance(nodes_dict["Z2"], nodes_dict["K11"]),'WZ':get_distance(nodes_dict["Z2"], nodes_dict["WZ"]), 'K8':get_distance(nodes_dict["Z2"], nodes_dict["K8"])}, "CC1":{'CC':get_distance(nodes_dict["CC1"], nodes_dict["CC"]), 'CC2':get_distance(nodes_dict["CC1"], nodes_dict["CC2"])}, "CC2":{'CC1':get_distance(nodes_dict["CC2"], nodes_dict["CC1"]), 'Z11':get_distance(nodes_dict["CC2"], nodes_dict["Z11"]), 'CC3':get_distance(nodes_dict["CC2"], nodes_dict["CC3"])}, "CC3":{'CC2':get_distance(nodes_dict["CC3"], nodes_dict["CC2"]), 'Z11':get_distance(nodes_dict["CC3"], nodes_dict["Z11"])}, "DD1":{'DD':get_distance(nodes_dict["DD1"], nodes_dict["DD"]), 'EE2':get_distance(nodes_dict["DD1"], nodes_dict["EE2"]), 'DD2':get_distance(nodes_dict["DD1"], nodes_dict["DD2"])}, "DD2":{'DD1':get_distance(nodes_dict["DD2"], nodes_dict["DD1"]), 'EE2':get_distance(nodes_dict["DD2"], nodes_dict["EE2"]), 'II42':get_distance(nodes_dict["DD2"], nodes_dict["II42"])}, "EE1":{'EE':get_distance(nodes_dict["EE1"], nodes_dict["EE"]), 'EE2':get_distance(nodes_dict["EE1"], nodes_dict["EE2"])}, "EE2":{'EE1':get_distance(nodes_dict["EE2"], nodes_dict["EE1"]), 'DD1':get_distance(nodes_dict["EE2"], nodes_dict["DD1"])}, "II1":{'II':get_distance(nodes_dict["II1"], nodes_dict["II"]), 'II2':get_distance(nodes_dict["II1"], nodes_dict["II2"])}, "II2":{'II1':get_distance(nodes_dict["II2"], nodes_dict["II1"]), 'II3':get_distance(nodes_dict["II2"], nodes_dict["II3"]), 'II21':get_distance(nodes_dict["II2"], nodes_dict["II21"])}, "II21":{'II2':get_distance(nodes_dict["II21"], nodes_dict["II2"]), 'II22':get_distance(nodes_dict["II21"], nodes_dict["II22"])}, "II22":{'II21':get_distance(nodes_dict["II22"], nodes_dict["II21"]), 'MM2':get_distance(nodes_dict["II22"], nodes_dict["MM2"])}, "II3":{'II2':get_distance(nodes_dict["II3"], nodes_dict["II2"]), 'II31':get_distance(nodes_dict["II3"], nodes_dict["II31"]), 'II4':0},"II31":{'II3':get_distance(nodes_dict["II31"], nodes_dict["II3"]), 'II311':get_distance(nodes_dict["II31"], nodes_dict["II311"]), 'II32':get_distance(nodes_dict["II31"], nodes_dict["II32"])}, "II311":{'II31':get_distance(nodes_dict["II311"], nodes_dict["II31"]), 'II4':get_distance(nodes_dict["II311"], nodes_dict["II4"])}, "II32":{'II31':get_distance(nodes_dict["II32"], nodes_dict["II31"])}, "II4":{'II3':get_distance(nodes_dict["II4"], nodes_dict["II3"]), 'II311':get_distance(nodes_dict["II4"], nodes_dict["II311"]), 'KII':get_distance(nodes_dict["II4"], nodes_dict["KII"]), 'II41':get_distance(nodes_dict["II4"], nodes_dict["II41"])}, "II41":{'II4':get_distance(nodes_dict["II41"], nodes_dict["II4"]), 'II42':get_distance(nodes_dict["II41"], nodes_dict["II42"])}, "II42":{'II41':get_distance(nodes_dict["II42"], nodes_dict["II41"]), 'DD2':get_distance(nodes_dict["II42"], nodes_dict["DD2"]), 'II43':get_distance(nodes_dict["II42"], nodes_dict["II43"])}, "II43":{'II42':get_distance(nodes_dict["II43"], nodes_dict["II42"]), 'II44':get_distance(nodes_dict["II43"], nodes_dict["II44"])}, "II44":{'II43':get_distance(nodes_dict["II44"], nodes_dict["II43"])}, "II5":{'KII':get_distance(nodes_dict["II5"], nodes_dict["KII"]), 'II6':get_distance(nodes_dict["II5"], nodes_dict["II6"])}, "II6":{'II5':get_distance(nodes_dict["II6"], nodes_dict["II5"]), 'II7':get_distance(nodes_dict["II6"], nodes_dict["II7"])}, "II7":{'II6':get_distance(nodes_dict["II7"], nodes_dict["II6"]), 'II8':get_distance(nodes_dict["II7"], nodes_dict["II8"])}, "II8":{'II7':get_distance(nodes_dict["II8"], nodes_dict["II7"]), 'II9':get_distance(nodes_dict["II8"], nodes_dict["II9"]), 'II81':get_distance(nodes_dict["II8"], nodes_dict["II81"])}, "II81":{'II8':get_distance(nodes_dict["II81"], nodes_dict["II8"]), 'K3':get_distance(nodes_dict["II81"], nodes_dict["K3"])}, "II9":{'II8':get_distance(nodes_dict["II9"], nodes_dict["II8"]), 'UII':get_distance(nodes_dict["II9"], nodes_dict["UII"]), 'II91':get_distance(nodes_dict["II9"], nodes_dict["II91"])}, "II91":{'II9':get_distance(nodes_dict["II91"], nodes_dict["II9"]), 'N1':get_distance(nodes_dict["II91"], nodes_dict["N1"])}, "MM1":{'MM':get_distance(nodes_dict["MM1"], nodes_dict["MM"]), 'MM2':get_distance(nodes_dict["MM1"], nodes_dict["MM2"])}, "MM2":{'MM1':get_distance(nodes_dict["MM2"], nodes_dict["MM1"]), 'II22':get_distance(nodes_dict["MM2"], nodes_dict["II22"])}}

# Graph in pygame Units
graph_pu = {'A': {'QQ': 39.32, 'B': 60.3, 'A1': 23.35}, 'B': {'C': 56.08, 'B1': 44.41, 'A': 60.3}, 'C': {'B': 56.08, 'CD': 78.55, 'D': 91.14}, 'D': {'E': 61.29, 'CD': 30.0, 'C': 35.06}, 'E': {'F': 63.53, 'E1': 49.24, 'D': 61.29}, 'F': {'G': 84.96, 'E': 63.53}, 'G': {'H': 124.1, 'F': 84.96, 'D': 194.54}, 'H': {'I': 73.06, 'G': 124.1}, 'I': {'J': 81.15, 'H': 73.06}, 'J': {'I': 81.15, 'K': 81.84}, 'K': {'J': 81.84, 'K1': 68.6, 'L': 43.6}, 'L': {'K': 43.6, 'M': 62.24}, 'M': {'L': 62.24, 'N': 113.18}, 'N': {'M': 113.18, 'N1': 62.97, 'O': 80.28}, 'O': {'N': 80.28, 'P': 84.17}, 'P': {'O': 84.17, 'P1': 18.38, 'Q': 44.05}, 'Q': {'P': 44.05, 'R': 85.48}, 'R': {'Q': 85.48, 'S': 161.7}, 'S': {'R': 161.7, 'S1': 57.43, 'T': 94.76}, 'T': {'S': 94.76, 'U': 123.84}, 'U': {'T': 123.84, 'U1': 47.51, 'V': 87.3}, 'V': {'U': 87.3, 'W': 31.89}, 'W': {'V': 31.89, 'W1': 29.15, 'X': 95.78}, 'X': {'W': 95.78, 'Y': 55.66}, 'Y': {'X': 55.66, 'Z': 82.02}, 'Z': {'Y': 82.02, 'Z1': 42.58, 'AA': 70.21}, 'AA': {'Z': 70.21, 'BB': 44.05}, 'BB': {'AA': 44.05, 'CC': 41.87}, 'CC': {'BB': 41.87, 'CC1': 33.24, 'ZZ': 141.82}, 'ZZ': {'CC': 141.82, 'DD': 132.77}, 'DD': {'ZZ': 132.77, 'DD1': 65.8, 'EE': 37.48}, 'EE': {'DD': 37.48, 'EE1': 53.04, 'FF': 35.61}, 'FF': {'EE': 35.61, 'GG': 79.76}, 'GG': {'FF': 79.76, 'HH': 137.28}, 'HH': {'GG': 137.28, 'II': 38.01}, 'II': {'HH': 38.01, 'II1': 55.44, 'JJ': 49.25}, 'JJ': {'II': 49.25, 'KK': 51.26}, 'KK': {'JJ': 51.26, 'LL': 47.8}, 'LL': {'KK': 47.8, 'MM': 58.52}, 'MM': {'LL': 58.52, 'MM1': 23.19, 'NN': 54.34}, 'NN': {'MM': 54.34, 'OO': 90.61}, 'OO': {'NN': 90.61, 'PP': 30.59}, 'PP': {'OO': 30.59, 'QQ': 47.38}, 'QQ': {'PP': 47.38, 'A': 39.32}, 'A1': {'A': 23.35, 'B2': 37.59, 'B3': 33.11}, 'B1': {'B': 44.41, 'B4': 65.76, 'B2': 29.15}, 'B2': {'B1': 29.15, 'B3': 48.51, 'A1': 37.59}, 'B3': {'B2': 48.51, 'A1': 33.11}, 'B4': {'B1': 65.76, 'CD': 25.08, 'E1': 70.18, 'E21': 35.13}, 'CD': {'C': 31.06, 'D': 30.0, 'B4': 25.08}, 'E1': {'E': 49.24, 'E2': 29.43}, 'E2': {'E1': 29.43, 'E21': 68.01, 'E3': 34.48}, 'E21': {'E2': 68.01, 'B4': 35.13, 'E31': 28.86}, 'E3': {'E2': 34.48, 'E31': 71.11, 'E4': 26.48}, 'E31': {'E3': 71.11, 'E21': 28.86}, 'E4': {'E3': 26.48, 'EF': 62.01, 'K4': 73.59}, 'EF': {'E4': 62.01, 'K5': 71.57, 'E5': 58.14, 'K4': 54.34}, 'E5': {'EF': 58.14, 'E6': 48.8}, 'E6': {'E5': 48.8}, 'K1': {'K': 68.6, 'K2': 28.44}, 'K2': {'K1': 28.44, 'K3': 62.36}, 'K3': {'K2': 62.36, 'K4': 56.04, 'II81': 161.45, 'II91': 213.82}, 'K4': {'K3': 56.04, 'EF': 54.34}, 'K5': {'EF': 71.57, 'K6': 86.4}, 'K6': {'K5': 86.4, 'KII': 71.51}, 'KII': {'K6': 71.51, 'II4': 78.31, 'K7': 58.0, 'II5': 117.21}, 'K7': {'KII': 58.0, 'K8': 27.02}, 'K8': {'K7': 27.02, 'K81': 97.8, 'K9': 42.58, 'Z2': 125.25}, 'K81': {'K8': 97.8, 'K82': 36.72}, 'K82': {'K81': 36.72}, 'K9': {'K8': 42.58, 'K91': 53.85, 'K10': 51.86}, 'K91': {'K9': 53.85, 'K92': 38.6}, 'K92': {'K91': 38.6}, 'K10': {'K9': 51.86, 'K11': 53.15}, 'K11': {'K10': 53.15, 'Z2': 57.49, 'KZ': 56.04}, 'KZ': {'Z2': 107.34, 'K11': 56.04, 'Z1': 72.34}, 'N1': {'N': 62.97, 'II91': 79.12}, 'P1': {'P': 18.38, 'P11': 23.43, 'P2': 39.6}, 'P11': {'P1': 23.43, 'P12': 33.12}, 'P12': {'P11': 33.12, 'P2': 33.02, 'P3': 32.57, 'P13': 56.01}, 'P13': {'P12': 56.01, 'PS': 31.4}, 'P2': {'P1': 39.6, 'P3': 29.27}, 'P3': {'P2': 29.27, 'P12': 32.57, 'P31': 36.72, 'PS': 51.01}, 'P31': {'P3': 36.72}, 'PS': {'P3': 51.01, 'P13': 31.4, 'S2': 73.33, 'P4': 45.01}, 'P4': {'PS': 45.01, 'U2': 80.62}, 'S1': {'S': 57.43, 'S2': 37.22}, 'S2': {'S1': 37.22, 'PS': 73.33}, 'U1': {'U': 47.51, 'U2': 37.16, 'U11': 73.05}, 'U11': {'U1': 73.05}, 'U2': {'U1': 37.16, 'P4': 80.62, 'UII': 109.02}, 'UII': {'U2': 109.02, 'II9': 69.58}, 'W1': {'W': 29.15, 'W11': 47.38, 'W2': 101.91}, 'W11': {'W1': 47.38, 'W12': 114.63}, 'W12': {'W11': 114.63, 'WZ': 110.06}, 'W2': {'W1': 101.91, 'W3': 0}, 'W3': {'W2': 55.54, 'WZ': 33.84, 'W4': 58.14}, 'W4': {'W3': 58.14, 'W5': 63.25}, 'W5': {'W4': 63.25, 'W6': 42.76}, 'W6': {'W5': 42.76, 'W7': 71.34}, 'W7': {'W6': 71.34, 'W8': 40.5}, 'W8': {'W7': 40.5}, 'WZ': {'W12': 110.06, 'W3': 33.84, 'Z2': 16.55}, 'Z1': {'Z': 42.58, 'KZ': 72.34, 'Z11': 22.47}, 'Z11': {'Z1': 22.47, 'CC3': 58.26}, 'Z2': {'KZ': 107.34, 'K11': 57.49, 'WZ': 16.55, 'K8': 125.25}, 'CC1': {'CC': 33.24, 'CC2': 32.25}, 'CC2': {'CC1': 32.25, 'Z11': 63.01, 'CC3': 40.25}, 'CC3': {'CC2': 40.25, 'Z11': 58.26}, 'DD1': {'DD': 65.8, 'EE2': 41.18, 'DD2': 56.94}, 'DD2': {'DD1': 56.94, 'EE2': 50.7, 'II42': 62.24}, 'EE1': {'EE': 53.04, 'EE2': 24.76}, 'EE2': {'EE1': 24.76, 'DD1': 41.18}, 'II1': {'II': 55.44, 'II2': 76.94}, 'II2': {'II1': 76.94, 'II3': 143.96, 'II21': 43.05}, 'II21': {'II2': 43.05, 'II22': 23.6}, 'II22': {'II21': 23.6, 'MM2': 48.6}, 'II3': {'II2': 143.96, 'II31': 22.8, 'II4': 0}, 'II31': {'II3': 22.8, 'II311': 48.75, 'II32': 21.0}, 'II311': {'II31': 48.75, 'II4': 65.0}, 'II32': {'II31': 21.0}, 'II4': {'II3': 90.55, 'II311': 65.0, 'KII': 78.31, 'II41': 60.54}, 'II41': {'II4': 60.54, 'II42': 36.67}, 'II42': {'II41': 36.67, 'DD2': 62.24, 'II43': 103.47}, 'II43': {'II42': 103.47, 'II44': 70.77}, 'II44': {'II43': 70.77}, 'II5': {'KII': 117.21, 'II6': 92.31}, 'II6': {'II5': 92.31, 'II7': 75.29}, 'II7': {'II6': 75.29, 'II8': 64.85}, 'II8': {'II7': 64.85, 'II9': 69.03, 'II81': 76.22}, 'II81': {'II8': 76.22, 'K3': 161.45}, 'II9': {'II8': 69.03, 'UII': 52.89, 'II91': 57.98}, 'II91': {'II9': 57.98, 'N1': 79.12}, 'MM1': {'MM': 23.19, 'MM2': 55.61}, 'MM2': {'MM1': 55.61, 'II22': 48.6}} 

# Graph in meters
graph_m = {'A': {'QQ': 65.21, 'B': 100.0, 'A1': 38.72}, 'B': {'C': 93.0, 'B1': 73.64, 'A': 100.0}, 'C': {'B': 93.0, 'CD': 130.26, 'D': 151.14}, 'D': {'E': 101.65, 'CD': 49.75, 'C': 58.14}, 'E': {'F': 105.36, 'E1': 81.67, 'D': 101.65}, 'F': {'G': 140.89, 'E': 105.36}, 'G': {'H': 205.81, 'F': 140.89, 'D': 322.62}, 'H': {'I': 121.16, 'G': 205.81}, 'I': {'J': 134.58, 'H': 121.16}, 'J': {'I': 134.58, 'K': 135.71}, 'K': {'J': 135.71, 'K1': 113.76, 'L': 72.31}, 'L': {'K': 72.31, 'M': 103.22}, 'M': {'L': 103.22, 'N': 187.69}, 'N': {'M': 187.69, 'N1': 104.42, 'O': 133.14}, 'O': {'N': 133.14, 'P': 139.59}, 'P': {'O': 139.59, 'P1': 30.49, 'Q': 73.04}, 'Q': {'P': 73.04, 'R': 141.75}, 'R': {'Q': 141.75, 'S': 268.15}, 'S': {'R': 268.15, 'S1': 95.24, 'T': 157.15}, 'T': {'S': 157.15, 'U': 205.38}, 'U': {'T': 205.38, 'U1': 78.79, 'V': 144.77}, 'V': {'U': 144.77, 'W': 52.89}, 'W': {'V': 52.89, 'W1': 48.35, 'X': 158.83}, 'X': {'W': 158.83, 'Y': 92.3}, 'Y': {'X': 92.3, 'Z': 136.03}, 'Z': {'Y': 136.03, 'Z1': 70.61, 'AA': 116.44}, 'AA': {'Z': 116.44, 'BB': 73.04}, 'BB': {'AA': 73.04, 'CC': 69.43}, 'CC': {'BB': 69.43, 'CC1': 55.13, 'ZZ': 235.19}, 'ZZ': {'CC': 235.19, 'DD': 220.19}, 'DD': {'ZZ': 220.19, 'DD1': 109.11, 'EE': 62.16}, 'EE': {'DD': 62.16, 'EE1': 87.96, 'FF': 59.05}, 'FF': {'EE': 59.05, 'GG': 132.27}, 'GG': {'FF': 132.27, 'HH': 227.66}, 'HH': {'GG': 227.66, 'II': 63.04}, 'II': {'HH': 63.04, 'II1': 91.95, 'JJ': 81.68}, 'JJ': {'II': 81.68, 'KK': 85.01}, 'KK': {'JJ': 85.01, 'LL': 79.27}, 'LL': {'KK': 79.27, 'MM': 97.05}, 'MM': {'LL': 97.05, 'MM1': 38.47, 'NN': 90.12}, 'NN': {'MM': 90.12, 'OO': 150.26}, 'OO': {'NN': 150.26, 'PP': 50.74}, 'PP': {'OO': 50.74, 'QQ': 78.58}, 'QQ': {'PP': 78.58, 'A': 65.21}, 'A1': {'A': 38.72, 'B2': 62.34, 'B3': 54.9}, 'B1': {'B': 73.64, 'B4': 109.06, 'B2': 48.35}, 'B2': {'B1': 48.35, 'B3': 80.44, 'A1': 62.34}, 'B3': {'B2': 80.44, 'A1': 54.9}, 'B4': {'B1': 109.06, 'CD': 41.59, 'E1': 116.38, 'E21': 58.26}, 'CD': {'C': 51.52, 'D': 49.75, 'B4': 41.59}, 'E1': {'E': 81.67, 'E2': 48.8}, 'E2': {'E1': 48.8, 'E21': 112.78, 'E3': 57.18}, 'E21': {'E2': 112.78, 'B4': 58.26, 'E31': 47.86}, 'E3': {'E2': 57.18, 'E31': 117.93, 'E4': 43.91}, 'E31': {'E3': 117.93, 'E21': 47.86}, 'E4': {'E3': 43.91, 'EF': 102.83, 'K4': 122.05}, 'EF': {'E4': 102.83, 'K5': 118.69, 'E5': 96.41, 'K4': 90.12}, 'E5': {'EF': 96.41, 'E6': 80.92}, 'E6': {'E5': 80.92}, 'K1': {'K': 113.76, 'K2': 47.17}, 'K2': {'K1': 47.17, 'K3': 103.42}, 'K3': {'K2': 103.42, 'K4': 92.94, 'II81': 267.74, 'II91': 354.6}, 'K4': {'K3': 92.94, 'EF': 90.12}, 'K5': {'EF': 118.69, 'K6': 143.28}, 'K6': {'K5': 143.28, 'KII': 118.59}, 'KII': {'K6': 118.59, 'II4': 129.87, 'K7': 96.19, 'II5': 194.38}, 'K7': {'KII': 96.19, 'K8': 44.81}, 'K8': {'K7': 44.81, 'K81': 162.19, 'K9': 70.61, 'Z2': 207.71}, 'K81': {'K8': 162.19, 'K82': 60.89}, 'K82': {'K81': 60.89}, 'K9': {'K8': 70.61, 'K91': 89.31, 'K10': 86.0}, 'K91': {'K9': 89.31, 'K92': 64.01}, 'K92': {'K91': 64.01}, 'K10': {'K9': 86.0, 'K11': 88.14}, 'K11': {'K10': 88.14, 'Z2': 95.34, 'KZ': 92.93}, 'KZ': {'Z2': 178.0, 'K11': 92.93, 'Z1': 119.97}, 'N1': {'N': 104.42, 'II91': 131.21}, 'P1': {'P': 30.49, 'P11': 38.86, 'P2': 65.67}, 'P11': {'P1': 38.86, 'P12': 54.93}, 'P12': {'P11': 54.93, 'P2': 54.75, 'P3': 54.02, 'P13': 92.88}, 'P13': {'P12': 92.88, 'PS': 52.07}, 'P2': {'P1': 65.67, 'P3': 48.55}, 'P3': {'P2': 48.55, 'P12': 54.02, 'P31': 60.89, 'PS': 84.59}, 'P31': {'P3': 60.89}, 'PS': {'P3': 84.59, 'P13': 52.07, 'S2': 121.62, 'P4': 74.65}, 'P4': {'PS': 74.65, 'U2': 133.7}, 'S1': {'S': 95.24, 'S2': 61.72}, 'S2': {'S1': 61.72, 'PS': 121.62}, 'U1': {'U': 78.79, 'U2': 61.63, 'U11': 121.15}, 'U11': {'U1': 121.15}, 'U4': {'U3': 257.05, 'II91': 85.01}, 'U3': {'P4': 94.43, 'U2': 69.61, 'U4': 257.05}, 'U2': {'U3': 69.61, 'U1': 61.63, 'P4': 133.7, 'UII': 180.79}, 'UII': {'U2': 180.79, 'II9': 115.4}, 'W1': {'W': 48.35, 'W11': 78.58, 'W2': 169.01}, 'W11': {'W1': 78.58, 'W12': 190.11}, 'W12': {'W11': 190.11, 'WZ': 182.53}, 'W2': {'W1': 169.01, 'W3': 0}, 'W3': {'W2': 92.11, 'WZ': 56.12, 'W4': 96.41}, 'W4': {'W3': 96.41, 'W5': 104.88}, 'W5': {'W4': 104.88, 'W6': 70.9}, 'W6': {'W5': 70.9, 'W7': 118.32}, 'W7': {'W6': 118.32, 'W8': 67.16}, 'W8': {'W7': 67.16}, 'WZ': {'W12': 182.53, 'W3': 56.12, 'Z2': 27.45}, 'Z1': {'Z': 70.61, 'KZ': 119.97, 'Z11': 37.27}, 'Z11': {'Z1': 37.27, 'CC3': 96.61}, 'Z2': {'KZ': 178.0, 'K11': 95.34, 'WZ': 27.45, 'K8': 207.71}, 'CC1': {'CC': 55.13, 'CC2': 53.48}, 'CC2': {'CC1': 53.48, 'Z11': 104.49, 'CC3': 66.75}, 'CC3': {'CC2': 66.75, 'Z11': 96.61}, 'DD1': {'DD': 109.11, 'EE2': 68.3, 'DD2': 94.43}, 'DD2': {'DD1': 94.43, 'EE2': 84.07, 'II42': 103.22}, 'EE1': {'EE': 87.96, 'EE2': 41.06}, 'EE2': {'EE1': 41.06, 'DD1': 68.3}, 'II1': {'II': 91.95, 'II2': 127.6}, 'II2': {'II1': 127.6, 'II3': 238.74, 'II21': 71.39}, 'II21': {'II2': 71.39, 'II22': 39.14}, 'II22': {'II21': 39.14, 'MM2': 80.6}, 'II3': {'II2': 238.74, 'II31': 37.82, 'II4': 0}, 'II31': {'II3': 37.82, 'II311': 80.85, 'II32': 34.83}, 'II311': {'II31': 80.85, 'II4': 107.79}, 'II32': {'II31': 34.83}, 'II4': {'II3': 150.17, 'II311': 107.79, 'KII': 129.87, 'II41': 100.4}, 'II41': {'II4': 100.4, 'II42': 60.82}, 'II42': {'II41': 60.82, 'DD2': 103.22, 'II43': 171.59}, 'II43': {'II42': 171.59, 'II44': 117.36}, 'II44': {'II43': 117.36}, 'II5': {'KII': 194.38, 'II6': 153.09}, 'II6': {'II5': 153.09, 'II7': 124.85}, 'II7': {'II6': 124.85, 'II8': 107.54}, 'II8': {'II7': 107.54, 'II9': 114.48, 'II81': 126.4}, 'II81': {'II8': 126.4, 'K3': 267.74}, 'II9': {'II8': 114.48, 'UII': 87.71, 'II91': 96.16}, 'II91': {'U4': 85.01, 'II9': 96.16, 'N1': 131.21}, 'MM1': {'MM': 38.47, 'MM2': 92.22}, 'MM2': {'MM1': 92.22, 'II22': 80.6}}
 
# Dictionary mapping Canteen name  to Canteen Node 
canteen_nodes = {"Food Court 1": "WZ", "Food Court 2": "K7", "Food Court 9": "II32", "Food Court 11": "II22","Food Court 13": "CD",  "Food Court 14": "A1", "Food Court 16": "E2","Ananda Kitchen": "II1","Foodgle Food Court": "NN", "North Hill Food Court": "HH",  "Pioneer Food Court": "CC3", "Quad Cafe": "N1","North Spine Plaza": "K3","Bakery Cuisine": "K3",  "Each A Cup": "K3",  "Grande Cibo": "K3",  "KFC": "K3", "Long John Silver's": "K3",  "McDonalds": "K3",  "Mr.Bean": "K3",  "North Spine Food Court": "K3",  "Paik's Bibim": "K3",  "Peach_Garden_Chinese_Restaurant": "K3", "Pen & INC": "K3",   "Pizza Hut Express": "K3",  "Starbucks Coffee": "K3",  "Subway": "K3", "The House Steam Boat Restaurant": "K3", "The Sandwich Guys": "K3", "The Soup Spoon Union": "K3", "Koufu": "U3"}

bar = copy.deepcopy(graph_m)

    
def canteen_coordinates(Canteen_name):
    '''
    Return the coordinates of the canteen
    input is the string of the canteen name.
    input string is case sensitive
    '''
    return (nodes_dict[canteen_nodes[Canteen_name]])
    
def get_exact_distance(t1, t2):
    '''
    Returns the exact distance in meters between thw two coordinates
    t1 and t2 are tuples representing the coordinates
    '''
    ans =(100/60.3)*((t1[0]-t2[0])**2+(t1[1]-t2[1])**2)**(1/2)
    return ans


def nearest_node(input_node):
    '''
    input is the user location coordinate
    returns a tuple containing the nearest node, nearest coordinate, and distance to that coordinate
    '''
    nearest_node_distance = 999999999999999
    for node, cor in nodes_dict.items():
        distance = get_exact_distance(cor, input_node)
        if distance < nearest_node_distance:
            nearest_node = node
            nearest_coordinate = cor
            nearest_node_distance = distance
    near =(nearest_node, nearest_coordinate, round(nearest_node_distance, 2))
    return near

def dijkstra_str(graph,start,goal):
    '''
    prints the shortest distance from start to goal, and the path taken using the dijkstra's algorithm
    '''
    graph = copy.deepcopy(bar)
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0    
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]) + 'm')
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    print('And the path is ' + str(path) )

def dijkstra(graph,start,goal):
    '''
    Returns a tuple of the shortest distance from start to goal, and the path taken using the dijkstra's algorithm
    Shortest distance is a float
    The path is a list
    '''
    graph = copy.deepcopy(bar)
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode) 
    if shortest_distance[goal] != infinity:
        float_distance = float(shortest_distance[goal])
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    tupl = (float_distance, path)
    return tupl

def total_distance(input_node, goal):
    '''
    Returns the total distance, from the user position to the final destination
    '''
    node_coordinates_distance = nearest_node(input_node)
    ShortestDistance_path = dijkstra(graph_m, node_coordinates_distance[0], goal)
    total_distance = round(node_coordinates_distance[2] + ShortestDistance_path[0], 2)
    return total_distance


def sorted_distances(input_node, can_list):
    '''
    input the user location and the list of canteen names
    Return the dictionary of canteen names and distane from user location in a sorted order (assending)
    Returned dictionary has the ranks(integers from 1 onwards) as keys, and the values are a tuple of the form (canteen name, distance)
    '''
    work = []
    emp_li = []
    for can in can_list:
        goal = canteen_nodes[can]
        work.append(goal)
    for can_node in work:
        tut = total_distance(input_node, can_node)
        emp_li.append(tut)
    can_distance = dict(zip(can_list, emp_li))
    sor = sorted(can_distance.values()) #sor is the sorted distances
    sorted_tuple = []
    for check in sor:
        for cant, dista in can_distance.items():
            if check == dista:
                sorted_tuple.append((cant, check))
                del can_distance[cant]
                break
    name = []
    for num in range(1, len(sorted_tuple)+1):
        name.append(num)
    final = dict(zip(name, sorted_tuple))
    return final

def nodes_to_coordinates(start, goal):
    path_nodes = dijkstra(graph_m, start, goal)[1]
    #print (path_nodes)
    path_coordinates = []
    for node in path_nodes:
        path_coordinates.append(nodes_dict[node])
    return (path_coordinates)

def show_path(input_node, can_name):
    '''
    Displays the path from the user location to the destination in the NTU Map
    '''
    red = (0, 255, 255)
    def display_map():
        introScreenImage = pygame.image.load("Pictures\Campus.png")
        screen = pygame.display.set_mode((10000,9000))
        screen.blit(introScreenImage,(0,0))
        start = nearest_node(input_node)[0]
        goal = canteen_nodes[can_name]
        path_coordinates = nodes_to_coordinates(start,goal)
        coor_list = []
        for coor in path_coordinates:
            coor_list.append([coor[0], coor[1]])
        coor_list.insert(0, [input_node[0], input_node[1]])
        for part in coor_list:
            if part == coor_list[0]:
                first = part
                continue
            else:
                second = part 
                pygame.draw.line(screen, red, first, second, 5)
                first = second
        pygame.display.flip() 
     #main program
    pygame.init()
    display_map()
    run=True
    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                mx,my=pygame.mouse.get_pos()
                pygame.quit()
                return(mx,my)
                run=False                
        pygame.display.update()





    
