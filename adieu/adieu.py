import inflect


p = inflect.engine()


names = []


print("Enter names, one per line (Press Ctrl-D to finish):")
try:
    while True:
        name = input()
        names.append(name)
except EOFError:
    pass  # This handles the Ctrl-D


message = "Adieu, adieu, to " + p.join(names)


print(message)
