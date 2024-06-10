contents = ['All carrots are to be sliced longitudinally', 'the carrots were reportedly sliced',
            'the slice process was well present']
file_names = ['doc.txt', 'report.txt', 'presentation.txt']

for content, file_name in zip(contents, file_names):
    file = open(f"file/{file_name}", 'w')
    file.write(content)
