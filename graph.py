import matplotlib.animation as animation
import matplotlib.pyplot as plt
import inputmongo
import time
import inalert

dbname = "Monitor"
collection = "temps"
muhlist = []
finalist = []

alert = inalert.getAlertData()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

def get(i, xs, ys):
 global finalist
 global muhlist
 for i in range(2):
  stoop = inputmongo.listen()
  muhlist.extend((stoop['fullDocument']['temp'], stoop['fullDocument']['hour'], stoop['fullDocument']['minute'], stoop['fullDocument']['day'], stoop['fullDocument']['month'], stoop['fullDocument']['year']))
  finalist.append(muhlist)
  muhlist = []
  
  # Read temperature (Celsius)
  temp_c = finalist[-1][0]
  
  if (temp_c < alert["min"]):
  	inalert.writeAlert(0, alert["nombre"], alert["email"], alert["min"], temp_c)
  elif temp_c > alert["max"]:
  	inalert.writeAlert(1, alert["nombre"], alert["email"], alert["max"], temp_c)

  # Add x and y to lists
  time_c = f"{finalist[-1][1]}:{finalist[-1][2]}"
  xs.append(time_c)
  ys.append(temp_c)

  # Limit x and y lists to 20 items
  xs = xs[-10:]
  ys = ys[-10:]

  # Draw x and y lists
  ax.clear()
  ax.plot(xs, ys)

  # Format plot
  plt.xticks(rotation=45, ha='right')
  plt.subplots_adjust(bottom=0.30)
  plt.title('Temperatura del invernadero')
  plt.ylabel('deg C')
 
def mainRT():
	inputmongo.initialize(dbname, collection)

	ani = animation.FuncAnimation(fig, get, fargs=(xs, ys), interval=200)
	plt.show()
