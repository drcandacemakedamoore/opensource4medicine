#program to read a bunch of files with unstructured text

import os

# the contents of a specific chosen directory are printed, feel free to modify to the directory you want 

documents= os. listdir (r"C:\Users\makeda\documents")
print (documents) 
# 

def read_text(posh, current_report):
    qoutes = open (r"C:\Users\makeda\documents\\"+current_report, encoding="utf-8")
    content_of_files = qoutes.read()
    found = False
    for line in posh:
        if line in content_of_files:
            found = True
    print (content_of_files)
    qoutes.close()
    return found


def read_list_of_bad():
    qoutes = open (r"C:\Users\makeda\documents\important1.txt", encoding="utf-8")
    result = []
    for line in qoutes:
        result.append(line.strip())
    qoutes.close()
    return result

### set a counter on report_currently_reading to start at 0, started a loop
report_number_count= len (documents)
report_currently_reading = 0
while report_currently_reading < report_number_count:

    #  a report is searched for any strings on a text important1.txt (users can make a list or hookup to GUI so users can input a list)
    result = read_list_of_bad()
    print (result)
    # indicate if there is a match in strings on important1.txt and report
    has_matches = read_text(result, documents[report_currently_reading])
    print("{} (# {}) has_matches: {}".format(documents[report_currently_reading], report_currently_reading, has_matches))

    
    
    
    # if report has matches true, then print report , and what text string matched
    
    
report_currently_reading = report_currently_reading + 1
