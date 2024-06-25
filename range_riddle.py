import random

day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

mood = ["Happy", "Sad", "Mad", "Joyful", "Energetic", "Calm", "Blissful"]

random.shuffle(mood)

for i in range(len(day)):
    print(f"On {day[i]}, you were feeling {mood[i]}.")