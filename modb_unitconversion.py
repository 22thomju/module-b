##############################
#file name: unitconversion.py#
# Julia T                    #
# Module-B                   #
##############################

def main():
    print("This program converts Ounces to Pounds.")
   

    for i in range(11): 
        print("---------------------------------------------") 
        o = i * 10
        p = round(o * 2.2)
        print(str(o) + " Ounces is: " + str(p) + " Pounds")
    for i in range (5):
        choice = input("Press the <o> key for Ounces or Press the <p> key for Pounds:")
        if choice == "o":     
            o = 0 
            o = eval(input("What is the amount in Ounces? "))
            p = round(o / 16)
            print(str(o) + " Ounces is: " + str(p) + " Pounds ")
            print("---------------------------------------------") 
        elif choice == "p":
            p = 0
            p = eval(input("What is the amount in Pounds? ")) 
            o = round(p * 16)
            print(str(p) + " Pounds is: " + str(o) + " Ounces")

    input("Press the <Enter> key to quit.")
    
main ()
