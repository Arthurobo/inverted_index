# from glob import glob
import glob2 as glob

# print('Named Explicitly')


for name in glob.glob(r"C:\Users\Richie\Downloads\enron(2).zip\skilling-j\inbox\*"):
    if name == False:
        print("Nothing")
    else:
        print(name)



# Here, I tried to count the number of files in every folders i downloaded, 
# but it shows me there are no files in the folders of the extracted document. Using the glob 
# Library to tell me the name of every files, but it keeps showing that there are no files in the 
# folders