import glob2
from pdf2image import convert_from_path
import tesserocr


#storing all the erolls in a variable
files = glob2.glob('/path/to/folder/containing/all/pdfs/*.pdf')
print(len(files))


#opening a new text file
new_file = open('extracted.txt', 'w+')

#setting a counter
i = 1


for file in files:
    
    #reading individual pdfs and converting them to image 
    print("Converting file " + "{}".format(i) + ".pdf")
    pages = convert_from_path(file, 600, first_page=2, thread_count=2)
    #note: higher the DPI better the recognition rate (default at 200 gives poor result). 
    #ignoring the first two pages which do not contain relevant information
    #increase thread_count only if machine is powerful enough to support. decrease conversion time
       
    print("writing data from file " + "{}".format(i))
    #writing the data in pages to the new text file
    for page in pages:
        new_file.writelines(tesserocr.image_to_text(page))
    
    i+=1


