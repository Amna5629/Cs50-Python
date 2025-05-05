import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Corrected regular expression pattern
    matches = re.search(r"^([0-9]{1,2}):00\s(AM|PM)\sto\s([0-9]{1,2}):00\s(AM|PM)$|^([0-9]{1,2})\s(AM|PM)\sto\s([0-9]{1,2})\s(AM|PM)$", s)

    if matches:

        start, time1, end, time2 = matches.groups()[0:4] if matches.groups()[0] else matches.groups()[4:]
        

        if start != "12" and time1 == "PM":
            start = str(int(start) + 12)
        elif start == "12" and time1 == "AM":
            start = "00"

        if end != "12" and time2 == "PM":
            end = str(int(end) + 12)
        elif end == "12" and time2 == "AM":
            end = "00"

        return f"{start.zfill(2)}:00 to {end.zfill(2)}:00"
    else:
        raise ValueError("Invalid time")

if __name__ == "__main__":
    main()
