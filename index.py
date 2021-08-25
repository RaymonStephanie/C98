fr = open("test.txt", mode="r")
fr2 = open("test2.txt", mode="r")

def readData(f, f2) :
  return [ f.read(), f2.read() ]

def swap() :
  f = open("test.txt", mode="w")
  f2 = open("test2.txt", mode="w")
  f.write(data[1])
  f2.write(data[0])
  return

data = readData(fr, fr2)
print("First file : " + str(data[0] + " " + "Second file : " + str(data[1])))
swap()

fr = open("test.txt", mode="r")
fr2 = open("test2.txt", mode="r")
tdata = readData(fr,fr2)
print("First file : " + str(tdata[0]) + " " + "Second file : " + str(tdata[1]))
