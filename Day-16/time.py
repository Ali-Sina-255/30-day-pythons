import time
import glob


def cureent_time():
    new_time = time.strftime('%b %d, %Y %H:%M:%S')
    print(f"It's {new_time}")


cureent_time()

files = glob.glob('files/*.txt')

for filepath in files:
    with open(filepath, 'r') as local_file:
        print(local_file.read().upper())
