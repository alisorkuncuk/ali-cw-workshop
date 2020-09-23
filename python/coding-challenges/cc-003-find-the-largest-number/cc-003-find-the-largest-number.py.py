NumberList = []

for i in range(1, 6):

    print("Please write your", i, "st/nd number as an integer or float value to add list: ")

    number = float(input())

    NumberList.append(number)

NumberList = sorted(NumberList)

print("The largest number that you entered to list is:", NumberList[4])