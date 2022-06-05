
#write code to prevent errors
def main(): #creat get_int function to minimize code
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            # adding return here shortens code instead of using x as variable
            return int(input(prompt))
        except ValueError:
            pass #just repeat loop and pass on the error

#call main 
main()

