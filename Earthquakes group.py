import matplotlib.pyplot as plt
plt.clf()#clears the graff for making a blank slate eachtime you renew the code

QuakeFile = open("currentQuakes.txt")
print(QuakeFile)

QuakeFile.readline()

for line in QuakeFile:
    line = line.split(',')# every time you see a comma thats a new line
    latitude = float(line[1])# every time you see a comma thats a new line
    longitude = float(line[2])#longitude = 2nd line
    depth = float(line[3])#depth = 3rd line
    if depth<

