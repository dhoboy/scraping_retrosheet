import os
# run this inside pitchers/ directory
# this file pulls out regular season pitching stats from a pitcher's file
directory = os.listdir(os.getcwd())
directory = directory[1:] # first file is .DS_Store...

for file in directory:
  f = open(file)
  w = open('../pitching_data/' + file, 'w')

  data_i_want = False

  for line in f:
    l = line.strip()

    if l == "Pitching Record":
      data_i_want = True
    elif "Record" in l:
      data_i_want = False

    if data_i_want == True:
      w.write(line)

  f.close()
  w.close()

