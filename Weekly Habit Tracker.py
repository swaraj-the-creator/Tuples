habit_info = ("Reading", "Playing","Studing","Watching TV","Writing","Stargazing","Drawing")
print("Habit information: ",habit_info)

weekly_habits = (15,7,15,15,7,15,7)

print("Total days tracked:", len(habit_info))
 
print("Day 1 status:", habit_info[0])
print("Day 4 status:", habit_info[3])

first_three_days = habit_info[0:5]
print("First five days:", first_three_days)
 
weekend_days = habit_info[5:]
print("Weekend days:", weekend_days)

weekly_habits = weekly_habits + (15,)
print("After adding one more day:", weekly_habits)

completed = weekly_habits.count(15)
missed = weekly_habits.count(7)
 
print("Completed days:", completed)
print("Missed days:", missed)

done = 0
not_done = 0
 
for i in range(0, len(weekly_habits)):
    if weekly_habits[i] == 1:
        done += 1
    else:
        not_done += 1
 
if (completed > missed):
    print("Great habit progress!")
else:
    print("Try to be more consistent!")

print("")
print("===== WEEKLY HABIT TRACKER =====")
print("Habit Name:", habit_info[:8])
print("Completed:", completed)
print("Missed:", missed)
print("================================")
