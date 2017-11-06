import matplotlib.pyplot as plt
plt.clf()#clears the graph to making a blank slate eachtime you renew the code
import matplotlib.image as mpimg

QuakeFile = open("currentQuakes.txt")
print(QuakeFile)

QuakeFile.readline()

for line in QuakeFile:
    line = line.split(',')# every time you see a comma thats a new item in the line
    latitude = float(line[1])# latitude = 2nd item in line
    longitude = float(line[2])#longitude = 3rd item line
    depth = float(line[3])#depth = 4th item line
    
 
        
    if depth > 415 and 620 > depth:
        plt.scatter(longitude, latitude, label = "earthquakes")
        image = mpimg.imread ("world_map.pdf")
        plt.imshow(image, extent=[-200,200,-60,80])
        plt.show()
        
    if depth < 415 and depth > 210:
        plt.scatter(longitude, latitude, label = "earthquakes")
        image = mpimg.imread ("world_map.pdf")
        plt.imshow(image, extent=[-200,200,-60,80])
        plt.show()
        
    if 0 < depth and depth < 210:
        plt.scatter(longitude, latitude, label = "earthquakes")
        image = mpimg.imread ("world_map.pdf")
        plt.imshow(image, extent=[-200,200,-60,80)
        plt.show()


 
image = plt.imread()
fig, ax = plt.subplots()
ax.imshow()
