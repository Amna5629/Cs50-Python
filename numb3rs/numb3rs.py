import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    response = re.match(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)

    if response:
        numbers = response.groups()
        for num in numbers:
            if int(num) < 0 or int(num) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
