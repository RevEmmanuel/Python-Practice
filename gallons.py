# If one inch of rain falls on an acre of land, how many gallons
# of water does that make?


if __name__ == '__main__':
    inches = int(input('Enter the number of inches: '))
    print("One acre of land is 66 by 660 feet which is 6_272_640 square inches.")
    cubic_inches = inches * 6_272_640
    print(inches, "inches on one acre of land is", cubic_inches, "cubic inches")
    print("One gallon of water is 231 cubic inches.")
    gallons = cubic_inches / 231
    if inches == 1:
        print("One(1) inch of rain on one acre of land is", gallons, "gallons.")
    else:
        print(inches, "inches of rain on one acre of land is", gallons, "gallons.")

    inches_int = int(input('Enter the number of inches'))
    volume = (inches_int / 12) * 43560
    gallons_int = volume * 7.48051945
    print(inches_int, "inches of rain on one acre of land is", gallons_int, "gallons.")
