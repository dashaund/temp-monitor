import yagmail

def mainMail(email, mail):
	yag = yagmail.SMTP('l19090379@zacatepec.tecnm.mx', '55120698Aa', host='smtp.office365.com', port=587, smtp_starttls=True, smtp_ssl=False)
	yag.send(to=email, subject='Greenhouse alert', contents=mail)
