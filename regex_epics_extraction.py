#importing necessary libraries
import numpy as np
import pandas as pd
import re

#reading the final txt file generated in previous step
with open('extracted.txt', 'r') as myfile:
    data = myfile.read().replace(' ', '\n')

#catching EPIC nos that fit the first pattern. refer to README
pattern1 = []
pattern1.extend(re.findall(r"(^[a-zA-Z]{3,4}\d{6,7})",data , re.MULTILINE))

#catching EPIC nos that fit the second pattern. refer to README
pattern2 = []
pattern2.extend(re.findall(r"(^[\D]{3}[a-zA-Z0-9]{2}/{1}[a-zA-Z0-9]{3}/{1}[a-zA-Z0-9]{6})",data , re.MULTILINE))


#few EPIC nos fitiing pattern 1 were observed to have errors like having an extra character at position 3
#and 0 being recognised as 'O' or 'o'

#correct pattern1 
modified = []

for p in pattern1:
    if len(p) > 10:
        modified.append(str(p).replace(p1[3],""))
    else:
        modified.append(p)

corrected = []

for m in modified:
    if (m[3] == "O" OR m[3] == "o"):
        corrected.append(str(m).replace(m[3],"0"))
    else:
        corrected.append(m)

#creating a final list with both the patterns
full_list = corrected + pattern2

#converting list to an array and converting to new Data Frame
all_epics = np.asarray(full_list)
all_epics = pd.DataFrame(all_epics)

#writing the Data Frame to a csv file
all_epics.to_csv('all_epics.csv')
