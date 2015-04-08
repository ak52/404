data = [416, 388, 186, 273, 164, 426, 444, 232, 304, 
434, 184, 442, 337, 285, 430, 488, 409, 284, 399, 410, 
331, 438, 173, 343, 496, 345, 252, 222, 391, 134, 405, 
365, 174, 428, 420, 223, 202, 481, 303, 202, 301, 134, 
163, 163, 125, 111, 247, 276, 302, 125]

def primativeKNN(data,value):
	closer = data[0]
	for x in data:
		if(pow((x-value),2) < pow((closer-value),2)):
			closer = x
	return closer

print primativeKNN(data,-100)
print primativeKNN(data,0)
print primativeKNN(data,100)
print primativeKNN(data,200)
print primativeKNN(data,300)
print primativeKNN(data,400)
print primativeKNN(data,500)
print primativeKNN(data,302)
print primativeKNN(data,250)
print primativeKNN(data,420)
print primativeKNN(data,190)
