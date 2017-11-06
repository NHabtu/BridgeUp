import matplotlib.pyplot as plt
plt.clf()

QuakeFile = open("currentQuakes.txt")
print(QuakeFile)

for line in QuakeFile:
    line = line.split(',')
    latitude.append(float(line[1]))
    longitude.append(float(line)[2))
    depth.append(float(line)[3])))
    If depth is < 
    print ("depth is less than 
plt.plot(latitude, longitude)

