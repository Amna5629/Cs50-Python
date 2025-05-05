while True:
    try:
        fuel = input("Fraction (X/Y): ")
        x, y = fuel.split("/")

        if not (x.isdigit() and y.isdigit()):
            continue

        x = int(x)
        y = int(y)

        if x > y or y == 0:
            continue

        percentage = (x / y) * 100

        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{round(percentage)}%")

        break
    
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
