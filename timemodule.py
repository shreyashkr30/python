import time
t=time.strftime('%H,%M,%S')
hour = int(time.strftime('%H'))
hour = int(input("Enter Your Time: "))
print(hour)

if (hour >= 0 and hour < 12):
    print("Good Morning Sir!!!")
elif (hour >= 12 and hour < 17):
    print("Good Evening Sir !!!")
elif (hour >= 17 and hour < 24):
    print("Good Night Sir !!!")