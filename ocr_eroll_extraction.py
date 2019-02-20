import numpy as np
import pandas as pd
import glob2
from pdf2image import convert_from_path
import tesserocr
import re

#storing all the erolls in a variable
files = glob2.glob('/home/pdag-admin/Documents/Data/erolls/Jamshedpur West/*.pdf')
print(len(files))

#converting all the pdfs to images
i = 302

#opening a new text file
new_file = open('extracted.txt', 'w+')

for file in files:
    print("Converting file " + "{}".format(i) + ".pdf")
    pages = convert_from_path(file, 600, first_page=2, thread_count=2)
       
    print("writing data from file " + "{}".format(i))
    #writing the data in pages to the new text file
    for page in pages:
        new_file.writelines(tesserocr.image_to_text(page))
    
    i+=1


