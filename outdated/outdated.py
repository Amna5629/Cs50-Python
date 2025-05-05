months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def parse_date(date):
    # Try to parse date in MM/DD/YYYY format
    if "/" in date:
        try:
            m, d, y = date.split("/")
            m, d, y = int(m), int(d), int(y)
            if 1 <= m <= 12 and 1 <= d <= 31:
                return f"{y:04}-{m:02}-{d:02}"
        except ValueError:
            pass

    # Try to parse date in Month Day, Year format
    elif " " in date:
        try:
            m, d, y = date.split(" ")
            d = d.rstrip(",")  # Remove comma from day
            d = int(d)
            y = int(y)
            if m in months and 1 <= d <= 31:
                if y >= 1900:
                    month_index = months.index(m) + 1  # Convert month name to month index
                    return f"{y:04}-{month_index:02}-{d:02}"
                else:
                    return None  # Reject dates earlier than 1900
        except ValueError:
            pass

    return None

def main():
    while True:
        date = input("date: ").strip()
        formatted_date = parse_date(date)
        if formatted_date:
            print(formatted_date)
            break
        else:
            continue
if __name__ == "__main__":
    main()
