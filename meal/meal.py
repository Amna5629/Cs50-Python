def main():
    time = input("What time is it? ").strip()
    time_float = convert(time)

    if 7.0 <= time_float <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_float <= 13.0:
        print("lunch time")
    elif 18.0 <= time_float <= 19.0:
        print("dinner time")

def convert(time):
    if "a.m." in time or "p.m." in time:
        time, period = time.split()
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)
        if period == "p.m." and hours != 12:
            hours = hours + 12
        elif period == "a.m." and hours == 12:
            hours = 0
    else:
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)

    total_hours = hours + minutes / 60.0
    return total_hours

if __name__ == "__main__":
    main()
