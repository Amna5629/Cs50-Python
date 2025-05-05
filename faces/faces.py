
def convert(text):
    new_text=text.replace(":)","🙂")
    new_text=new_text.replace(":(","🙁")
    print(new_text)


def main():
    text=input("")
    convert(text)


main()
