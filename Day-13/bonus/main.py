print('In this programmer you can calculate the feed and inches in maters ')
print("just provide feed and inches in one line . ex: 2 feed 4 inches")
feed_inches = input("Enter Feed and Inches :")

"""Decoupling in this function we user Decoupling to access the local Variables in to the goloble varible """


def parse(feed_inches_par):
    parts = feed_inches_par.split(" ")
    feed = float(parts[0])
    inches = float(parts[1])
    return {"feed": feed, "inches": inches}


def convert(feed, inches):
    meters = feed * 0.3048 + inches * 0.0254
    return meters


def helper(func, funcs):
    return f'{func} and {funcs} is called in this time.'


parsed = parse(feed_inches)

result = convert(parsed['feed'], parsed['inches'])
print(f"{parsed['feed']} feed and {parsed['inches']} is equal to {result} meters .")
