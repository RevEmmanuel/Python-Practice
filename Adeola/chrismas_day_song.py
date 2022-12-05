def xmas_day_song():
    day = int(input('Enter the day of xmas:-> '))
    day_song = ""
    match day:
        case 1:
            day_song = "First Day"
        case 2:
            day_song = "Second Day"
        case 3:
            day_song = "Third Day"
        case 4:
            day_song = "Fourth Day"
        case 5:
            day_song = "Fifth Day"
        case 6:
            day_song = "Sixth Day"
        case 7:
            day_song = "Seventh Day"
        case 8:
            day_song = "Eighth Day"
        case 9:
            day_song = "Ninth Day"
        case 10:
            day_song = "Tenth Day"
        case 11:
            day_song = "Eleventh Day"
        case 12:
            day_song = "Twelve Day"
    print(f'On the {day_song} day of christmas my true love said to me,', end=' ')
    for i in range(day, 1, -1):
        match i:
            case 12:
                print("Twelve drummers drumming \n")
            case 11:
                print("Eleven pipers piping \n")
            case 10:
                print("Ten lords a-leaping \n")
            case 9:
                print("nine ladies dancing \n")
            case 8:
                print("Eight maids a-milking \n")
            case 7:
                print("Seven swans a-swimming \n")
            case 6:
                print("Six geese a-laying \n")
            case 5:
                print("Five gold rings, \n")
            case 4:
                print("Four calling birds, \n")
            case 3:
                print("Three French hens,\n")
            case 2:
                print("Two turtle doves,\n")
            case 1:
                print("And a partridge in a pear tree")


if __name__ == '__main__':
    xmas_day_song()
