f = open("demofile.txt")
try:
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
else:
    print("Everything is fine")
