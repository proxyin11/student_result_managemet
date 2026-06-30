student = {}

while True:
    print("----- student management system -----    ")
    print("1. Add student")
    print("2. View student")
    print("3. check student")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    #add student
    if choice == "1":
        name = input("Enter student name: ").split()  # Get the first word as the name
        marks = float(  input("Enter student marks: ") )
        student[name[0]] = marks
        print(f"Student {name[0]} : {marks} added successfully.")
        
    #[view student]
    elif choice =="2":
        if not student :
            print("no student found")
        else:
            for name,marks in student.items():
                print(f"student {name}: {marks}")
                
    # check stuudent 
    elif choice == "3":
        name =input("Enter student name to check: ")

        if name in student:
            marks = student[name]
            
            if marks >=50:
                print(f"student {name} has passed with marks: {marks}")
            else:
                print(f"student {name} has failed with marks: {marks}")
        else:
            print(f"student {name} not found.")

    
#exit                 
    elif choice =="4":
        print ("Exiting the program...")
        break 
    else:
        print("Invalid choice. Please try again.")
        

