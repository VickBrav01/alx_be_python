# task = input("Enter your task:")
# priority = input("Priority (high/medium/low):").lower()
# time_bond = input("Is it time-bound? (yes/no):").lower()

# match (priority,time_bond):
#     case ("high", "yes"):
#         print(f"Reminder: ''{task}'' is a high priority task that requires immediate attention today!")
#     case ("high", "no"):
#         print(f"Note: '{task}' is a high priority task, but it's not time-bound. Plan to address it soon.")
#     case ("medium", "yes"):
#         print(f"Reminder: '{task}' is a medium priority task that needs to be completed soon!")
#     case ("medium", "no"):
#         print(f"Note: '{task}' is a medium priority task. You can schedule it for later.")
#     case ("low", "yes"):
#         print(f"Alert: '{task}' is a low priority task, but it is time-bound. Don’t forget to complete it!")
#     case ("low", "no"):
#         print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
#     case _:
#         print("Task priority and time-bound status do not match specific cases.")
    
# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Plan to address it soon."
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " and needs to be completed soon!"
        else:
            reminder += ". You can schedule it for later."
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
        if time_bound == "yes":
            reminder += " but it is time-bound. Don’t forget to complete it!"
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        reminder = "Task priority does not match specific cases."

# Provide a Customized Reminder
print(reminder)
