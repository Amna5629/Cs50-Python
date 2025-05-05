def main():
    camel_text = input("Enter camelCase text: ").strip()
    snake_case_text = convert(camel_text)
    print("Converted to snake_case:", snake_case_text)

def convert(text):
    snake_case = []
    for char in text:
        if char.isupper():
            snake_case.append('_')
            snake_case.append(char.lower())
        else:
            snake_case.append(char)

    return ''.join(snake_case)

if __name__ == "__main__":
    main()
