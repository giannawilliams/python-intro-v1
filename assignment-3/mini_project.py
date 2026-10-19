import random

weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
weekend = ['saturday', 'sunday']

daytime = ['morning', 'afternoon']
nighttime = ['evening']

weekday_activities = ['studying', 'cleaning up', 'running errands', 'practicing a hobby']
weekend_activities = ['taking a nap', 'practicing a hobby', 'attending a party', 'spending time with friends']

morning_afternoon_activities = ['making breakfast', 'meditating', 'journaling']
evening_activities = ['meditating', 'watching a tv show', 'calling family']

user_day = input("Enter a day: ")
day = user_day.lower()

user_time = input("Morning, afternoon or evening?: ")
time = user_time.lower()


if day in weekday and time in daytime:
    print(f"Suggestion: Try {random.choice(weekday_activities)} or {random.choice(morning_afternoon_activities)}")
elif day in weekday and time in nighttime:
    print(f"Suggestion: Try {random.choice(weekday_activities)} or {random.choice(evening_activities)}")
elif day in weekend and time in daytime:
    print(f"Suggestion: Try {random.choice(weekend_activities)} or {random.choice(morning_afternoon_activities)}")
elif day in weekend and time in nighttime:
    print(f"Suggestion: Try {random.choice(weekend_activities)} or {random.choice(evening_activities)}")
else:
    print("Try entering a correct date (like Monday, Tuesday, Wednesday etc.) and correct time of day (Morning, afternoon or evening).")
