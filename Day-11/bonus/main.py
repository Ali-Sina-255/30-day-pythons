try:
    width = float(input("Enter rectangle width :"))
    height = float(input("Enter rectangle height :"))
    if width == height:
        exit("That's look like square. ")
    area = width * height
    print(area)
except ValueError:
    print("please Enter a Number .")

