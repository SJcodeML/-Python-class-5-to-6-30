Minimum_height = 50


def main():

    try : 
        user_height = int(input("What is your height ?  "))

    except ValueError:
        print("Enter a valid height ... It must be number like 50 60 100 ")    
    
    
    if user_height >= Minimum_height :
        print("You're tall enough to ride!")
    else :
        print("You're not tall enough to ride, but maybe next year!")

if __name__ == "__main__":
    main()
