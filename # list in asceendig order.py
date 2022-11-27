# list in asceendig order
numlist = [ ]
number = int(input("Enter  the  length of the list"))
for i in range(1, number +1):
  value = int(input("Please enter the number in the list %d" %i))
  numlist.append(value)

for i in range (number):
  for j in range(i+1,number):
    if (numlist[i] > numlist[j]):
       temp = numlist[i] =numlist[j]
      #  numlist[i] = numlist(j)
      #  numlist[j] = temp
print(numlist)
  