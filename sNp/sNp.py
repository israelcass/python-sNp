import math

def openSNP(filename):
  f = open(filename).readlines()
  N = int(filename.split('.s')[1][0])

  while 1:
    if f[0][0] == '!':
      f.pop(0)
      continue
    elif f[0][0] == '#':
      header = f[0]
      f.pop(0)
      continue
    else:
      break

  header = header.split()

  values = []
  for idx in f:
    values.append(map(float, idx.split()))

  matrix = [[0 for x in range(N)] for x in range(N)] 

  if header[3] == 'MA':
    idx = 1
    for j in range(0,N):
      for i in range(0,N):
        matrix[i][j] = [(x[idx], y[idx+1]) for x, y in zip(values, values)]
        idx = idx + N

  if header[3] == 'RI':
    idx = 1
    for j in range(0,N):
      for i in range(0,N):
        absolute = [math.sqrt(x[idx]**2 + y[idx+1]**2) for x, y in zip(values, values)]
        phase = [math.atan(y[idx]/x[idx+1])*180/math.pi for x, y in zip(values, values)]
        matrix[i][j] = [(x, y) for x, y in zip(absolute, phase)]
        idx = idx + N

  freq = [x[0] for x in values]
  return [freq, matrix]
