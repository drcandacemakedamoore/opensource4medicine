#python program to read u of i cxr report and classify


####make a list of all the file


import os
import xml.etree.ElementTree as ET
documents = os.listdir (r"C:\Users\makeda\programming\catapop\documents\ecgen-radiology")

file_currently_reading =0
file_number_count = len(documents)
 
while file_currently_reading < file_number_count:

    filename = documents[file_currently_reading]
    
#interate the loop


    tree = ET.parse(r"C:\Users\makeda\programming\catapop\documents\ecgen-radiology\\"+filename)
    root = tree.getroot()

    c = os.getcwd ()
    store = []
    otherstorage = []
    
    is_normal = False

 
                 
                 
#if normal write path to list of normals
    for child in root:
        if child.tag == 'parentImage':
            
            print (child.get('id'))
            
            store.append (child)
            
        if child.tag == 'pmcId':
            
            print (child.get('id'))

            otherstorage.append (child.get('id'))
            
        if child.tag == 'MeSH':
                
                print(child.getchildren()[0].text)
            
                if child.getchildren()[0].text ==  'normal':
                    is_normal = True
                    

    if is_normal == True:
        printnormalhere = open('list_of_normal.csv','a')
   
        pmc_id = otherstorage[0]
        
        for child in store:
            print((c+"/images"+"/"+(child.get('id'))+".png" ))
    
            printnormalhere.write((c+"/images"+"/"+(child.get('id'))+".png"))
            printnormalhere.write(',')
            printnormalhere.write(pmc_id)
            printnormalhere.write(',')
            
            textstorage = tree.findall(".//MedlineCitation/Article/Abstract/AbstractText[@Label='FINDINGS']")
                    
            
            if textstorage:
                printnormalhere.write(textstorage[0].text or 'No findings')
            else:
                printnormalhere.write('No findings')
            printnormalhere.write("\n")  

           
        printnormalhere.close()
        
    if is_normal == False:
        printhere = open('list_of_abnormal.csv','a')
        pmc_id = otherstorage[0]
        found_opacity = False

        for child in store:
            print((c+"/images"+"/"+(child.get('id'))+".png" ))
            printhere.write((c+"/images"+"/"+(child.get('id'))+".png"))
            printhere.write(',')
            printhere.write(pmc_id)
            printhere.write(',')   

            textstorage = tree.findall(".//MedlineCitation/Article/Abstract/AbstractText[@Label='FINDINGS']")
            texthere = ''

            if textstorage:
                printhere.write(textstorage[0].text or 'No findings')
                texthere = textstorage[0].text or 'No findings'
            else:
                printhere.write('No findings')
            printhere.write("\n")  
          
          

            sub_string1_positive = "opacity"
            sub_string2_positive = "opacities"
            sub_string1_negative = "no opacit"
            
            

            if (sub_string1_positive in texthere or sub_string2_positive in texthere) and sub_string1_negative not in texthere:
                found_opacity = True

        printhere.close()
     
        if found_opacity == True:
            printithere = open('list_of_opacities.csv','a')
            for child in store:
                print((c+"/images"+"/"+(child.get('id'))+".png" ))

                printithere.write((c+"/images"+"/"+(child.get('id'))+".png"))
                printithere.write(',')
                printithere.write(pmc_id)
                printithere.write(',')
              
                
                textstorage = tree.findall(".//MedlineCitation/Article/Abstract/AbstractText[@Label='FINDINGS']")
            

                if textstorage:
                    printithere.write(textstorage[0].text or 'No findings')
                    
                else:
                    printhere.write('No findings')
                printithere.write("\n")  

            printithere.close()

    file_currently_reading = file_currently_reading + 1

    
