import matplotlib.pyplot as plt
plt.clf()

QuakeFile = open("currentQuakes.txt")
print(QuakeFile)

QuakeFile.readline()

for line in QuakeFile:
    line = line.split(',')
    latitude = float(line[1])
    longitude = float(line[2])
    depth = float(line[3])
    if 415<depth<620

