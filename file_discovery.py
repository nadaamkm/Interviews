"""
Author: Nadaa Moharram
Purpose: Analog Devices Interview
Reviewer: Chris Ampenberger
Date: 09/15/2022
"""
import os

def file_analysis(directory, *ext):
    """
    This function will identify the number of files with .ext extension, 
    locate all the files and subdirectories, total number of lines and average number 
    of lines per file 
    """
    #Check if user inputed an extension
    if not ext:
        ext=".txt"
    count_files=0
    count_lines=[]
    #Walk through directory and files
    for root, dirs, files in os.walk(path):
        #For each file, check the extension
        for file in files:
            if(file.endswith(ext)):
                print(os.path.join(root,file))
                with open(os.path.join(root,file)) as f:
                    x= len(f.readlines()) #Count the number of lines in the file
                    count_lines.append(x)
                    print('Total lines:', x)
                    count_files+=1
    #Check if the number of files is zero
    if count_files==0:
        average =0
    else:
        average=sum(count_lines)/count_files

    print("\n===========")
    print("Number of files found:  ", count_files)
    print("Total number of lines:  ", sum(count_lines))
    print("Average lines per file:  ", "{:.2f}".format(average))

path =r"C:\Users\mohar\Desktop\venv"
extension = ".csv"
file_analysis(path, extension)

               

