task_variable = input("Enter your task: ")
priority_variable = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority_variable:
    case "high":
        if time_bound == "yes":
            print(f"Urgent Reminder:'{task_variable}' is a high priority task that must be completed today!")
        else:
            print(f"Important:'{task_variable}'is a high priority task.keep it at the top of your list.")
    case "medium":
        
        if time_bound == "yes":
            print(f"Reminder:'{task_variable}' is a medium priority task that must be completed today!")
        else:
            print(f"Important:'{task_variable}'is a medium priority task.keep it at the top of your list.")
    case "low":
        if time_bound == "yes":
            print(f"FYI:'{task_variable}' is a low priority task, but it needs to be done today.")
        else:
            print(f"NOTE:'{task_variable}' is a low priority task.Consider completing it when you have free time.")