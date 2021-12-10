# def median_mode_mean(list):
# list = [5,3,6,7,8,3]
# list = [1,2,3,4,6,7]

def median(list): #calculating median
  length = 0
  for i in list:
    length += 1
  if length % 2 != 0:
    position = int((length + 1) / 2) 
    median = list[position - 1]
    print(median)
  else:
    stepOne = int(length / 2)
    stepTwo = list[stepOne - 1] + list[stepOne]
    median = stepTwo / 2
    print(f"median is : {median}")
# median([77])

def mean(list):
  numSum = 0
  length = 0
  for i in list:
    numSum = numSum + i
    length += 1
    average = numSum / length
  print(f"average is : {average}")

# mean([77])


def mode(list):
  length = 0
  count = 0
  newArray = []

  
  for i in list:
    length += 1
    
  if list != []:
    for i in range(length):
      a = list[i]
      index = i
      # print(a, index)
      for time in list:
        if time == a:
          count += 1
      newArray.append(count)
      count = 0
    DetectedElement = max(newArray)
  
    postion = newArray.index(DetectedElement)
    mode = list[postion]
    print(f"mode is : {mode}")

      
  else:
    print("please don't insert empty list. I may crash 😠")

# mode([3,3,1,4,5,2])



def median_mode_mean(list):
  median(list)
  mode(list)
  mean(list)


median_mode_mean([3,3,1,4,5,2])
