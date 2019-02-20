import numpy as np
import pandas as pd
import glob2
from pdf2image import convert_from_path
import tesserocr
import re

with open('extracted.txt', 'r') as myfile:
    data = myfile.read().replace(' ', '\n')


pattern1 = []
pattern1.extend(re.findall(r"(^[a-zA-Z]{3,4}\d{6,7})",data , re.MULTILINE))

pattern2 = []
pattern2.extend(re.findall(r"(^[\D]{3}[a-zA-Z0-9]{2}/{1}[a-zA-Z0-9]{3}/{1}[a-zA-Z0-9]{6})",data , re.MULTILINE))

#correct pattern1 
modified = []

for p1 in pattern1:
    if len(p1) > 10:
        modified.append(str(p1).replace(p1[3],""))
    else:
        modified.append(p1)

corrected = []

for m in modified:
    if m[3] == "O":
        corrected.append(str(m).replace(m[3],"0"))
    else:
        corrected.append(m)

full_list = corrected + pattern2

all_epics = np.asarray(full_list)
all_epics = pd.DataFrame(all_epics)

all_epics.to_csv('JamshedpurWest_epics2.csv')