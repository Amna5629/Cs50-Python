greet=input("Greeting:").lower().strip()

if greet[0:5] =="hello":
    print("$0")

elif  greet[0] == "h" and  greet[0:5] != "hello":
    print("$20")

else:
     print("$100")

