mport glob2
from pdf2image import convert_from_path
from pdf2image.exceptions import PDFPageCountError, PDFSyntaxError
import tesserocr
import os
import time


# defining globals
ac_name = str.title(input('Enter name of constituency: '))
path = os.path.normpath('/home/pdag-admin/Documents/Data/erolls/{}'.format(ac_name))


def eroll_data_extractor(path):
    if os.path.exists(path):
        files = glob2.glob('{}/*.pdf'.format(path))
        print('Files to extract from: {}'.format(len(files)))
        temp_file = open('temp.txt', 'w+')
        for file in files:
            fname = ((file.rsplit('/', 1))[1]).split('.', 1)[0]
            print("extracting file {}.pdf".format(fname))
            start_time = time.time()
            try:
                pages = convert_from_path(file, 600, first_page=2, thread_count=8)
                print('writing data from file {}.pdf'.format(fname))
                for page in pages:
                    temp_file.writelines(tesserocr.image_to_text(page))
                end_time = time.time() - start_time
                print(end_time)
            except PDFPageCountError:
                print('File {}.pdf is corrupted'.format(fname))
    else:
        print('files do not exist. try again')
        eroll_data_extractor(path)


def main():
    eroll_data_extractor(path)


if __name__ == '__main__':
    main()
