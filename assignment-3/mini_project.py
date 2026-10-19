import random

user_day = input("Enter a day: ")
day = user_day.lower()

user_time = input("Morning, afternoon or evening?: ")
time = user_time.lower()

week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
morning_activities = ['studying', 'cleaning up', 'running errands', 'calling family']
afternoon_activities = ['practicing a hobby', 'taking a nap', 'spending time with friends', 'cooking a new dish']
evening_activities = ['attending a party', 'meditating', 'journaling','watching a tv show']

if day in week and time == "morning":
    choices = random.sample(morning_activities, 3)
    print(f"Try the following activities: {choices}")
elif day in week and time == "afternoon":
    choices = random.sample(afternoon_activities, 3)
    print(f"Try the following activities: {choices}")
elif day in week and time == "evening":
    choices = random.sample(evening_activities, 3)
    print(f"Try the following activities: {choices}")
else:
    print("Try entering a correct date (like Monday, Tuesday, Wednesday etc.) and correct time of day (Morning, afternoon or evening).")
