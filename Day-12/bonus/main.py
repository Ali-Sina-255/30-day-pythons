def get_average():
    with open('file/data.txt', 'r') as local_file:
        data = local_file.readlines()[1:]
    values = data[1:]
    values = [float(i) for i in values]

    local_average = sum(values) / len(values)
    return local_average


average = get_average()
print(f"the average is {average}.")
