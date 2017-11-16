x = range(0,10)
print x
print x[-1]
x[-1]=999
#dir(x)

print "---------------"

y=tuple(x)
print(y)
# y[-1]=998

colors = ['yellow', 'magenta', 'lavender']
for (i, name) in enumerate(colors):
    print i, name

pairs = [(1, 10), (2, 20), (3, 30), (4, 40)]
for (low, high) in pairs:
    print low + high

countries = ["uk", "usa", "uk", "uae"]
dir(countries)
#help(countries.count) 
countries.count("uk")

#with open("example_data/weather.csv", "r") as reader:
path="example_data"
with open(path + "/weather.csv", "r") as reader:
   data = reader.read()
   print data

#with open("weather.csv") as reader:
with open(path + "/weather.csv", "r") as reader:
     header = reader.readline() #   We will ignore this
     rain = []
     for line in reader.readlines():
	  r = line.strip().split(",")[-1]
	  r = float(r)         
	  rain.append(r)
        
     print rain
with open("myrain.txt", "w") as writer:
     for r in rain:
         writer.write(str(r) + "\n")


