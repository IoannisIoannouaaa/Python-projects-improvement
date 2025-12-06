def main():
    time = input('What time is it? ')
    s_time = convert(time)
    if 7 <= s_time <= 8:
        print("breakfast time")

    elif 12 <= s_time <= 13:
        print("lunch time")

    elif 18 <= s_time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + minutes / 60

if __name__ == "__main__":
    main()