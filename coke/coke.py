def main():
    total = 0
    due = 50

    while due > 0:
        print(f"Amount Due: {due}")
        coin = input("Insert Coin: ").strip()

        if coin in ["5", "10", "25"]:
            total= total + int(coin)
            due = 50 - total
        else:
            print(f"Amount Due: {due}")

    print("Change Owed:", total - 50)

if __name__ == "__main__":
    main()
