print('In this programmer you can calculate the feed and inches in maters ')
print("just provide feed and inches in one line . ex: 2 feed 4 inches")
feed_inches = input("Enter Feed and Inches :")


def convert(feed_inches_par):
    parts = feed_inches_par.split(" ")
    feed = float(parts[0])
    inches = float(parts[1])
    meters = feed * 0.3048 + inches * 0.0254
    return f"{feed} feed {inches} inches is equal to {meters} meters ."


print(convert(feed_inches))
