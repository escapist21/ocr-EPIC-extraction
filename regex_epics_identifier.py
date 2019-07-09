import numpy as np
import pandas as pd
import re
from ocr_extraction import ac_name

# reading the previous text file generated in the previous step and storing it
with open('temp.txt', 'r') as fp:
    data = fp.read().replace(' ', '\n')


def pattern_identifier(data):
    pattern1 = []
    pattern1.extend(re.findall(r"(^[a-zA-Z]{3,4}\d{6,7})", data, re.MULTILINE))

    pattern2 = []
    pattern2.extend(re.findall(r"(^[\D]{3}[a-zA-Z0-9]{2}/{1}[a-zA-Z0-9]{3}/{1}[a-zA-Z0-9]{6})", data, re.MULTILINE))

    return pattern1, pattern2


def pattern_cleaner(pattern1):
    modified = []
    for p in pattern1:
        if len(p) > 10:
            modified.append(str(p).replace(p[3], ""))
        else:
            modified.append(p)

    corrected = []
    for m in modified:
        if m[3] == "O" or m[3] == "o":
            corrected.append(str(m).replace(m[3],"0"))
        else:
            corrected.append(m)

    return corrected


def final_list_generator(corrected, pattern2, ac_name):
    full_list = corrected+pattern2

    all_epics = np.asarray(full_list)
    all_epics = pd.DataFrame(all_epics)

    all_epics.to_csv('{}_epics.csv'.format(ac_name))


def main():
    pattern1, pattern2 = pattern_identifier(data=data)
    corrected = pattern_cleaner(pattern1)
    final_list_generator(corrected, pattern2, ac_name)


if __name__ == '__main__':
    main()
