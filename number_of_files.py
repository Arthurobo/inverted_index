import os

path, dirs, files = next(os.walk(r"C:\Users\Richie\Desktop\inverted_index\skilling-j\inbox\genie"))
file_count = len(files)
print (file_count)



# Here, I tried to count the number of files in every folders i downloaded, 
# but it shows me there are no files in the folders of the extracted document.