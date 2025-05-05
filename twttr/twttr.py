def main():
    text = input("Input: ").strip()
    print("Output:", convert(text))

def convert(text):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    new_text = []
    for i in text:
        if i not in vowels:
            new_text.append(i)
    return ''.join(new_text)

if __name__ == "__main__":
    main()
