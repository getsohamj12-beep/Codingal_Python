medical_cause=input("Do u have a medical case or had one(Y/N)? ").upper()
if medical_cause=="Y":
    print("Allowed")
else:
    attendance=int(input("Enter Attendance out of 100"))
    if attendance>75:
        print("Allowed")
    else:
        print("Not Allowed")
