


def main():
    greet=input("Greeting:").lower().strip()
    print(value(greet))



def value(greeting):
    if greet[0:5] =="hello":
        return("$0")

    elif  greet[0] == "h" and  greet[0:5] != "hello":
        return("$20")

    else:
        return("$100")



if __name__ == "__main__":
    main()
