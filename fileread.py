file1 = open('myfile.txt', 'r')
count = 0

line = file1.readlines()
count = len(line)
print(count)