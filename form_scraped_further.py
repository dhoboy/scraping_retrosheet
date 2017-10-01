import os
# run this inside pitching_data/ directory
# this file forms pitching records into csv's
directory = os.listdir(os.getcwd()) # regex: [ \t]+
directory = directory[1:] # first file is .DS_Store...

for file in directory:
  f = open(file, 'r')
  w = open('../pitching_csvs/' + file + '.csv', 'w')

  data = f.readlines()
  data = data[1:len(data)-2]

  headers = data[0:1]
  headers = "".join(headers).split()
  headers = headers[0:len(headers)-2]

  data = data[1:]

  w.write(",".join(headers))
  w.write("\n")

  for line in data:
    l = line.split()
    l = l[0:2] + l[5:len(l)-3]
    if (l[0:1] != "Total".split() and l[1:2] != "TOT".split()):
      w.write(",".join(l))
      w.write("\n")

  f.close()
  w.close()
