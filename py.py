lst = [3, 4, 3,111,112,212, 12, 6, 7, 2]


def lengthList(lst):
    length = 0
    for i in lst:
        length += 1
    return length

# print(f"length : {lengthList(lst)}")

def MaxList(lst):
    biggestValue = lst[0]
    for currentValue in lst:
        if currentValue >= biggestValue:
            biggestValue = currentValue
    return biggestValue

# print(f"biggestValue : {MaxList(lst)}")

def median(lst): 
    length = lengthList(lst)
    if length % 2 != 0:
        position = int((length + 1) / 2) 
        median = lst[position - 1]
    else:
        stepOne = int(length / 2)
        stepTwo = lst[stepOne - 1] + lst[stepOne]
        median = stepTwo / 2
    return median

# print(f"median : {median(lst)}")

def mean(lst):
    numSum = 0
    length = lengthList(lst)
    for i in lst:
        numSum = numSum + i
        mean = numSum / length
    return mean

# print(f"mean : {mean(lst)} ")

def mode(lst):
    count = 0
    newList = []
    length = lengthList(lst)
    for index in range(length):
        a = lst[index]
        for number in lst:
            if number == a:
                count += 1
        newList.append(count)
        count = 0
    detectedElement = MaxList(newList)
    position = newList.index(detectedElement)
    mode = lst[position]
    return mode

# print(f"Mode : {mode(lst)} ")

def median_mode_mean(lst):
    if not lst:
        print("you inserted empty list")
    else:
        print(f"median : {median(lst)}, mean : {mean(lst)}, Mode : {mode(lst)} ")

median_mode_mean(lst)

