import csv

def __main__():
    with open("data.txt", "r", encoding="utf-8") as f:
        data = list(csv.reader(f, delimiter='\t'))
    
    counter = 0
    i = 1
    while i < len(data):
        if data[i] > data[i-1]:
            counter += 1
        i += 1
    print(counter)

if __name__ == '__main__':
    __main__()