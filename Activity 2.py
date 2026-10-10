import random
import time

def getRandomeDate(startDate, endDate):
    print(f"Printing random date between {startDate} and {endDate}!")

    randomGenerator = random.random()

    dateFormat = "%m/%d/%Y"

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endtime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endtime - startTime)

    randomDate = time.strftime(dateFormat, time.localtime(randomTime))

    return randomDate

print("Random Date = ", getRandomeDate("7/6/2013", "7/6/2026"))