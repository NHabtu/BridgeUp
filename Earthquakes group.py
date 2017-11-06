import matplotlib.pyplot as plt
plt.clf()#clears the graph to making a blank slate eachtime you renew the code

QuakeFile = open("currentQuakes.txt")
print(QuakeFile)

QuakeFile.readline()

for line in QuakeFile:
    line = line.split(',')# every time you see a comma thats a new item in the line
    latitude = float(line[1])# latitude = 2nd item in line
    longitude = float(line[2])#longitude = 3rd item line
    depth = float(line[3])#depth = 4th item line
    
       if 415<depth<620:
        plt.scatter(longitude, latitude, label = "earthquakes")
        plt.plot( 415<depth<620, color = "purple", marker = ".", label="Depth between 415 and 620")
        
    if 210<depth<415:
        plt.scatter(longitude, latitude, label = "earthquakes")
        
    if depth > 415 and 620 > depth:
        plt.scatter(longitude, latitude, label = "earthquakes")
        plt.show()
        
    if depth < 415 and depth > 210:
        plt.scatter(longitude, latitude, label = "earthquakes")
        plt.show()
        
    if 0 < depth and depth < 210:
        plt.scatter(longitude, latitude, label = "earthquakes")
        plt.show()


 
image = plt.imread()
fig, ax = plt.subplots()
ax.imshow()
