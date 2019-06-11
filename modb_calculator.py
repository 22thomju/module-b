############################
#file name: calculator.py   #
# Julia T                  #
# Module-B                 #
############################

def main():

    #options to choose from
    print("This program is a calculator.")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: ")) #number of choice

  
    for i in range (100):
        if (choice>=1 and choice<=4):
            print("Enter two numbers:")
            num1 = int(input())
            num2 = int(input())
            if choice==1: #first choice
                res = num1 + num2 
                print("Result = ", res) 
                
            elif choice == 2: #second choice
                res = num1 - num2
                print("Result = ", res) 

            elif choice == 3: #third choice
                res = num1 * num2 
                print("Result = ", res)

            else: #fourth choice 
    	        res = num1 / num2 
    	        print("Result = ", res)

        elif choice == 5: #fifth choice
            exit()
            input("Press the <Enter> key to quit.")   

        else:
            print("Wrong input..!!")
            
main ()
