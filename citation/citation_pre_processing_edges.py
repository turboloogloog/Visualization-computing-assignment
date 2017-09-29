# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 15:50:09 2017

@author: vince
"""

from xml.dom import minidom
import csv


xmldoc = minidom.parse("gd-catations.xml")

gdpapers = xmldoc.getElementsByTagName("gdpapers")[0]

papers = gdpapers.getElementsByTagName("paper")


with open('edges.csv', 'w', newline='') as csvfile:
    fieldnames = ['Source','Target']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    i = 0
    for paper in papers:
        line = []
        
        
        p_id = paper.getElementsByTagName("id")[0].firstChild.data
        
        title = paper.getElementsByTagName("title")[0].firstChild.data
        
        
        authors = paper.getElementsByTagName("author")
        temp = []
        for s in authors:
            temp.append(str(s.firstChild.data))
        authors = temp
        
        
        institution = paper.getElementsByTagName("institution")
        temp = []
        for s in institution:
            temp.append(str(s.firstChild.data))
        institution = temp
        
    
        cites = paper.getElementsByTagName("cites")
        temp = []
        for s in cites:
            temp.append(str(s.firstChild.data))
        cites = temp
        
        citedby = paper.getElementsByTagName("citedby")
        temp = []
        for s in citedby:
            temp.append(str(s.firstChild.data))
        citedby = temp
        
        
        year = paper.getElementsByTagName("year")[0].firstChild.data
        
    
        line.append(p_id)
        i += 1
        #print(str(line).strip("['']"),",",str(authors),',',institution,',',cites,',',citedby,',',year)
        print(str(line).strip("['']"),",",title)
        
        if len(citedby) != 0:
            for c in citedby:
                try:
                    writer.writerow({'Source': str(line).strip("['']"), 'Target': c})
                except Exception as e:
                    s = str(e)
        
        

            

print(i)