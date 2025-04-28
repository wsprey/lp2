#HELP DESK SYSTEM
def help_desk_expert_system():
    print("Welcome to the Help Desk Expert System")
    print("Please answer the following questions with 'yes' or 'no'.\n")

    internet = input("Is your internet connection working? ").lower()
    if internet == "no":
        wifi = input("Is your Wi-Fi turned on? ").lower()
        if wifi == "no":
            print("\nAdvice: Please turn on your Wi-Fi.")
        else:
            modem = input("Is your modem/router powered on? ").lower()
            if modem == "no":
                print("\nAdvice: Please power on your modem/router.")
            else:
                print("\nAdvice: Try restarting your modem/router.")
    else:
        speed = input("Is your computer running slow? ").lower()
        if speed == "yes":
            disk = input("Is your hard disk almost full? ").lower()
            if disk == "yes":
                print("\nAdvice: Free up some space on your hard disk.")
            else:
                antivirus = input("Do you have an antivirus installed and updated? ").lower()
                if antivirus == "no":
                    print("\nAdvice: Install or update your antivirus software.")
                else:
                    print("\nAdvice: Try restarting your computer or closing unnecessary programs.")
        else:
            print("\nAdvice: Your system seems fine. For any other issues, contact IT support.")

# Run the system
help_desk_expert_system()


#HOSPITAL SYSTEM
def hospital_expert_system():
    print("Welcome to the Medical Expert System")
    print("Please answer with 'yes' or 'no'.\n")

    fever = input("Do you have a fever? ").lower()
    if fever == "yes":
        cough = input("Do you also have a cough? ").lower()
        if cough == "yes":
            print("\nAdvice: You might have the flu. Visit a doctor if symptoms persist.")
        else:
            print("\nAdvice: Monitor your temperature and stay hydrated.")
    else:
        headache = input("Do you have a headache? ").lower()
        if headache == "yes":
            print("\nAdvice: Rest, drink water, and avoid screen time.")
        else:
            print("\nAdvice: You seem healthy!")

# Run the system
hospital_expert_system()

#IM SYSTEM
def information_management_expert_system():
    print("Welcome to the Information Management Expert System")
    print("Please answer with 'yes' or 'no'.\n")

    files = input("Do you have too many unorganized files? ").lower()
    if files == "yes":
        important = input("Are these files important? ").lower()
        if important == "yes":
            print("\nAdvice: Create folders based on categories like Documents, Photos, and Videos.")
        else:
            print("\nAdvice: Delete unwanted files to free up space.")
    else:
        print("\nAdvice: Your files seem well organized!")

# Run the system
information_management_expert_system()


#EMPLOYEE MANAGEMENT
def employee_evaluation_expert_system():
    print("Welcome to the Employee Performance Evaluation Expert System")
    print("Please answer with 'yes' or 'no'.\n")

    targets = input("Did the employee meet their targets? ").lower()
    if targets == "yes":
        teamwork = input("Does the employee work well in a team? ").lower()
        if teamwork == "yes":
            print("\nEvaluation: Excellent Performance!")
        else:
            print("\nEvaluation: Good, but needs to improve teamwork.")
    else:
        punctuality = input("Is the employee punctual? ").lower()
        if punctuality == "yes":
            print("\nEvaluation: Needs slight improvement in work delivery.")
        else:
            print("\nEvaluation: Needs improvement in punctuality and work quality.")

# Run the system
employee_evaluation_expert_system()

