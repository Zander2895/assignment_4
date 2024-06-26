import random 

times = ["morning", "afternoon", "evening"]

day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

mood = ["Happy", "Sad", "Mad", "Joyful", "Energetic", "Calm", "Blissful"]

random.shuffle(day)
random.shuffle(mood)

for i in range(len(day)):
    for i in range(len(times)):
        print(f"On {day[i]} {times[i]} you were feeling {mood[i]}.")