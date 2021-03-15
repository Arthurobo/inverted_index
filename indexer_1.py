# This counts the number of files in a folder
import os

path, dirs, total_files = next(os.walk(r"C:\Users\Richie\Desktop\inverted_index\zzz"))
print(len(total_files))


# This opens a specific file in the folder
# file = open((total_files)[0], encoding='utf8') # for files in a folder

file = open('file.txt', encoding='utf8')

read = file.read() 
file.seek(0) 
read 
  
# to obtain the 
# number of lines 
# in file 
line = 1
for word in read: 
    if word == '\n':
        line += 1
print("Number of lines in file is: ", line) 
  
# create a list to 
# store each line as 
# an element of list 
array = [] 
for i in range(line): 
    array.append(file.readline()) 
  
array 


# Here I am counting the number of files in a folder and also counting the number of lines in a
# particular selected file.