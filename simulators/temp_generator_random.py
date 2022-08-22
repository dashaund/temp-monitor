##Imports##
from jinja2 import Template
import random

##Functions##
def render(doc):
 with open(doc) as f:
  rendered = Template(f.read()).render(temp=ftemp, hour=fhour, minute=fminute, day=fday, month=fmonth, year=fyear)
  f.close()
  return rendered
  
def writejson(filename, mode):
 with open(filename, mode) as f:
  f.write(output.strip())
  f.close()

##Global vars##
temp = 0
fhour = random.randint(0,23)
fminute = 0
fday = random.randint(1,28)
fmonth = random.randint(1,12)
fyear = random.randint(2000,2021)
output = ""

##Create output##
while True: #Check minutes
 if fminute > 59:
  fhour += 1
  fminute = 0
  
 if fhour > 23: #Check hours
  break

 ftemp = random.randint(15,35) #Generate random temp
 
 rendered = render('jinjatemplate') #Render template
 
 output = output + (rendered + "\n") #Add render to output
 
 fminute += 1 #Increment minutes

writejson("temps_random.json", "w") #Write to final JSON
