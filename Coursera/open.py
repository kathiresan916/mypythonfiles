# "C:\Users\HP\Desktop\My Knowledge Python\Job Description.txt"
open_filename = '/Users/HP/Desktop/My Knowledge Python/Job Description.txt'
file_name = open(open_filename, 'r')
line = file_name.readline()
while line != '\n':
    print(line)
    line = file_name.readline()


# print(file_name.read())
