##Imports##
from datetime import datetime
from jinja2 import Template
import inputmongo
import random
import time
import json

ndays = 4

##Functions##
def ttime(): #Extract current time
 return str(datetime.time(datetime.now())).split(":")
 
def date(): #Extract current date
 return str(datetime.date(datetime.now())).split("-")
 
def render(doc):
 with open(doc) as f:
  rendered = Template(f.read()).render(temp=ftemp, hour=fhour, minute=fminute, day=fday, month=fmonth, year=fyear)
  f.close()
  return rendered
  
def writejson(filename, mode):
 with open(filename, mode) as f:
  f.write(output.strip())
  f.close()
  
def data():
 global ftemp
 global fhour
 global fminute
 global fday
 global fmonth
 global fyear
 global output

 try: 
  while True:
   if fminute > 59: #Check minutes
    fhour += 1
    fminute = 0
  
   if fhour > 23: #Check hours
    fday += 1
    fhour = 0
    
   if fday > fday+ndays: #Check hours
    break

   ftemp = random.randint(15,35) #Generate random temp
 
   rendered = render('jinjatemplate') #Render template
 
   output = output + (rendered + "\n") #Add render to output
  
   writejson("temps_current.json", "w") #Write to final JSON
  
   inputmongo.writedb(json.loads(rendered)) #Write to MongoDB
 
   fminute += 1 #Increment minutes
 
   time.sleep(1) #Wait 1 second
 except KeyboardInterrupt:
  print("Interrupted")

##Global vars##
extime = ttime()
exdate = date()

ftemp = 0
fhour = int(extime[0])
fminute = int(extime[1])
fday = int(exdate[2])
fmonth = int(exdate[1])
fyear = int(exdate[0])
output = ""

dbname = "Monitor"
collection = "temps"

##Create output##
inputmongo.initialize(dbname, collection)
inputmongo.delcontent()
data()
inputmongo.close()
