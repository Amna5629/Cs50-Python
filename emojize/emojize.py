import emoji

def emojize_input():

    user_input = input("Input: ")


    emojized_str = emoji.emojize(user_input, language='alias')

    print(emojized_str)

if __name__ == "__main__":
    emojize_input()
