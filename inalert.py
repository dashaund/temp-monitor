from jinja2 import Template
import inputmongo
import json
import sendmail

def connect():
	dbname = "Monitor"
	collection = "alerts"
	inputmongo.initialize(dbname, collection)

def render(doc):
 with open(doc) as f:
  rendered = Template(f.read()).render(nombre=fnombre, email=femail, tmpmin=fmin, tmpmax=fmax)
  f.close()
  return rendered
  
def render2(doc):
 with open(doc) as f:
  rendered = Template(f.read()).render(name=fname, tempset=ftempset, tempread=ftempread)
  f.close()
  return rendered

def altMain(name, email, tmin, tmax):
	connect()
	inputmongo.delcontent()
	
	global fnombre
	global femail
	global fmin
	global fmax
	
	fnombre = name
	femail = email
	fmin = tmin
	fmax = tmax
	
	rendered = render("./alerts/jinjatemplate")
	inputmongo.writedb(json.loads(rendered))
	inputmongo.close()

def getAlertData():
	connect()
	alert = inputmongo.fetchAlert()
	return alert

def writeAlert(condition, name, email, tempset, tempread):
	global fname
	global ftempset
	global ftempread
	fname = name
	ftempset = tempset
	ftempread = tempread
	
	rendered = render2("./alerts/jinjatemplate2")
	sendmail.mainMail(email, rendered)
