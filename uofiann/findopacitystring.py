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
        found_pneumothorax = False

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
          
            # bunch of strings to define opacities or not

            sub_string_opacity_positive = ["opacity", "opacities", "Opacity", "Opacities"]
            
            sub_string_opacity_negative = ["no opacit", "No opacit", "without opacit", "no visualized opacit", "no visible opacit", "without opacit",
                                           "no focal airspace opacity","no focal air space opacit","No focal air space opacity",
                                           "no focal airspace opacities ", "No focal airspace opacities ", "No focal air space opacit",
                                           "No focal airspace consolidation, suspicious pulmonary opacity","without focal airspace opacity",
                                           "No focal consolidation, suspicious pulmonary opacity",
                                           "No focal airspace consolidation, suspicious pulmonary opacity" , "No XXXX acute findings/opacities"]
            
            # bunch of strings to define pneumothorax
            sub_string_pneumothorax_positive = ["pneumothorax", "pneumothoraces", "Pneumothorax", "Pneumothoraces"]
            sub_string_pneumothorax_negative = ["no pneumothor", "No pneumothor", "or pneumothor",  "no evidence of pneumothor",  "No evidence of pneumothor",
                                                "no focal consolidations, pneumothorax", "no pleural effusion, pneumothorax", "No pleural effusion, pneumothorax",
                                                "no visible pneumothorax", "no visualized pneumothorax", "No visible pneumothorax", "No visualized pneumothorax",
                                                "no pleural line", "without focal consolidation, pneumothorax", "pneumothorax, or "]

            def has_word_function(text, words):
                for word in words:
                    if word in text:
                        return True
                return False


            if has_word_function( texthere,sub_string_opacity_positive ) and not has_word_function(texthere, sub_string_opacity_negative):
                found_opacity = True

               



                
            if has_word_function( texthere,sub_string_pneumothorax_positive ) and not has_word_function(texthere, sub_string_pneumothorax_negative):
                found_pneumothorax = True                

        printhere.close()
     
        if found_opacity == True:
            printithere = open('nlist_of_opacities.csv','a')
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

        if found_pneumothorax == True:
            printpneumohere = open('llist_of_pneumothorax.csv','a')
            for child in store:
                print((c+"/images"+"/"+(child.get('id'))+".png" ))

                printpneumohere.write((c+"/images"+"/"+(child.get('id'))+".png"))
                printpneumohere.write(',')
                printpneumohere.write(pmc_id)
                printpneumohere.write(',')
              
                
                textstorage = tree.findall(".//MedlineCitation/Article/Abstract/AbstractText[@Label='FINDINGS']")
            

                if textstorage:
                    printpneumohere.write(textstorage[0].text or 'No findings')
                    
                else:
                    printpneumohere.write('No findings')
                printpneumohere.write("\n")  

            printpneumohere.close()
  

    file_currently_reading = file_currently_reading + 1

    

   

