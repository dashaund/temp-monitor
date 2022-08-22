import inputmongo
import matplotlib.pyplot as plt

dbname = "Monitor"
collection = "temps"
inputmongo.initialize(dbname, collection)

def mainHS(day, month, year):
	x = inputmongo.fetchDoc(day, month, year)
	
	temps = []
	hours = []
	c = 0
	zum = 0
	
	for document in x:
		zum = zum + document["temp"]
		c += 1
		
		if c == 60:
			temps.append(round(zum/60,1))
			c = 0
			zum = 0
	
	for i in range(0,24):
		hours.append(i)
	
	fig, ax = plt.subplots(figsize=(12,8))
	plt.plot(hours, temps)
	plt.xlabel("Hora", size=12)
	plt.ylabel("Temperatura", size=12)
	plt.title("Temperatura historica", size=15)
	for index in range(len(hours)):
	  ax.text(hours[index], temps[index], temps[index], size=12)
	plt.xticks(hours, size=12)
	plt.grid()
	plt.show()
