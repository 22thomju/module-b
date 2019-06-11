############################
#file name: convert.py     #
# Julia T                  #
# Module-B                 #
############################

def main():
    print("This program converts celsius to fahhrenhit.")
   

    for i in range(11): #table and for loop
        print("---------------------------------------------") 
        c = i * 10
        f = round(9 / 5 * c + 32, 1)
        print(str(c) + " degrees Celsius is: " + str(f) + " degrees Fahrenheit")
    for i in range (5):
        choice = input("Press the <C> key for Celsius or Press the <F> key for Fahrenheit:")
        if choice == "c":  #choice one (celcius)   
            c = 0 
            c = eval(input("What is the Celsius temperature? "))
            f = round(9 / 5 * c + 32, 1)
            print(str(c) + " degrees Celsius is: " + str(f) + " degrees Fahrenheit")
            print("---------------------------------------------") 
        elif choice == "f":   #choice 2 (fahrenheit)
            f = 0
            f = eval(input("What is the Fahrenheit temperature? ")) 
            c = (f - 32) * 5 / 9
            print(str(f) + " degrees Fahrenheit is: " + str(c) + " degrees Celsius")

    input("Press the <Enter> key to quit.")
    
main ()