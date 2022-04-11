sum = 0
count = 0
average = 0

while True:
  try:
    x = input("Enter a number: ")
    if (x == "done"): 
     break
    value = float(x)
    sum = value + sum
    count = count + 1
    average = sum / count
  except:
    print(" bad data Invalid input.")
print ("The sum is {},The count is {}, and the average is {}".format(sum, count, average))