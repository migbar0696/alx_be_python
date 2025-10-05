task_variable = input("Enter your task: ")
priority_variable = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority_variable:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task_variable}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task_variable}' is a high priority task. Keep it at the top of your list.")
    case "medium":
        
        if time_bound == "yes":
            print(f"Reminder: '{task_variable}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task_variable}' is a medium priority task. Consider completing it this week.")
    case "low":
        if time_bound == "yes":
            print(f"FYI: '{task_variable}' is a low priority task, but it needs to be done today.")
        else:
            print(f"Note: '{task_variable}' is a low priority task. Consider completing it when you have free time.")