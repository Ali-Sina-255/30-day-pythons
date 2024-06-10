filename = ["1.doc", '1.report', '1.presentation']

result = [filename.replace('.', '-') + '.txt' for filename in filename]
print(result)
