def main():
    grocery_list = {}

    try:
        while True:
            item = input().strip().lower()
            if item == "":
                continue

            if item in grocery_list:
                grocery_list[item] = grocery_list[item] + 1
            else:
                grocery_list[item] = 1

    except EOFError:
        sorted_items = sorted(grocery_list.items())

        for item, count in sorted_items:
            print(f"{count} {item.upper()}")
        exit(0)



if __name__ == "__main__":
    main()
