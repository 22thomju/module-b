############################
#file name: challenge.py   #
# Julia T                  #
# Module-B                 #
############################

def main():
    favfood = ["ice cream", "ramen", "rice", "chicken"]
    for food in (favfood):
        print(food)

    x = input("What is your first name?" )
    y = input("What is your last name?" )
    print("Hello, ", x, y)

    a = input("How old are you? ")
    weeks = int(a) * 52
    print("You are at least", weeks, " weeks old." )
    months = int(a) * 12
    print("You are at least", months, " months old." )
    days = int(a) * 365
    print("You are at least", days, " days old." )

    h = input("Enter a noun: ")
    g = input("Enter a verb:" )
    f = input("Enter an adjective:" )
    d = input("Enter a place:" )
    print("The", h, "is very", f, "while", g, "when it's at", d)

    
main()
