def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def parseM(input):
  input_list = input.split('\n')[2:]
  output_list = []

  for row in input_list:
    output_row = [int(x) for x in row.split()]
    output_list.append(output_row)

  return(output_list)


def printM(m):
  list = ['{:>2}'.format(element) for element in m]
  new_string = ' '.join(list)
  print(new_string)


def printMatrix(matrix):
  resources = len(matrix[0])
  test = ord('A')
  resourceMat = []
  for re in range(resources):
    resourceMat.append(chr(test + re))
    
  printM(resourceMat)
  for mat in matrix:
    printM(mat)


def NeedGen(Allo, Max):
  rows = len(Allo)
  cols = len(Allo[0])
  Need = [[0 for _ in range(cols)] for _ in range(rows)]
  for i, row in enumerate(Allo):
    for j, column in enumerate(row):
      Need[i][j] = Max[i][j] - Allo[i][j]
  return Need


def compare(a, b): #returns true if a < b
  counter = True
  for j, column in enumerate(a):
    if a[j] > b[j]:
      counter = False
  return counter


def isSafe(Allo, need, work):
  Finish = []
  Order = []
  for i in range(len(need)):
    Finish.append(False)

  for fin in range(len(Finish)):
    for i, row in enumerate(need):
      if Finish[i] == False:
        if compare(row, work):
          Finish[i] = True
          work = [work[j] + Allo[i][j] for j in range(len(Allo[0]))]
          Order.append(f"P{i}")
          break

  if False in Finish:
    print("The system is not in a safe state")
  else:
    print("The system is in a safe state with the sequence:")
    printM(Order)
  
  return True


def isValid(text):
  try:
    output_row = [int(x) for x in text.split()]
    return output_row
  except:
    return ["False"]


def add(allo, m):
  for i, x in enumerate(allo):
    allo[i] = x + m[i]


def sub(first, m):
  for i, x in enumerate(first):
    first[i] = x - m[i]


fileInput = read_file("input.txt")
output_list = fileInput.split('\n\n')

Allocation = parseM(output_list[0])

Max = parseM(output_list[1])

Available = parseM(output_list[2])

Need = NeedGen(Allocation, Max)

print("Allocation:")
printMatrix(Allocation)
print("")
print("Max:")
printMatrix(Max)
print("")
print("Available:")
printMatrix(Available)
print("")
print("Need:")
printMatrix(Need)
print("")
isSafe(Allocation, Need, Available[0])



print("\nSelect process you wish to send a request through")
for i in range(len(Allocation)):
  print(f"{i}. P{i}")
  
val = int(input("Enter: "))
while(val not in range(len(Allocation))):
  val = int(input("\nInvalid Input\nEnter: "))

req = isValid(input("Enter Process: "))

while req == ["False"]:
  req = isValid(input("\nInvalid Input\nEx: '1 0 3 4'\nEnter: "))

if (compare(req, Need[val])):
  if(compare(req, Available[0])):
    add(Allocation[val], req)
    sub(Need[val], req)
    sub(Available[0], req)
    print("\nAllocation:")
    printMatrix(Allocation)
    print("\nMax:")
    printMatrix(Max)
    print("\nAvailable:")
    printMatrix(Available)
    print("\nNeed:")
    printMatrix(Need)
    print("")
    isSafe(Allocation, Need, Available[0])
  else: print("The request is not valid/safe because the request is larger than the resources Available")
else: print("The request is not valid/safe because the request is larger than the Process's Needs")
