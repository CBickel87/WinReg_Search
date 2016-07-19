with open('complist.txt', 'r') as f:
    array = []
    for line in f:
        line = line.strip('\n')
        array.append(line)

print(array)
