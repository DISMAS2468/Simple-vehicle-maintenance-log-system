maintenance_logs = []

def add_log():
    vehicle = input("Enter vehicle name: ")
    service = input("Enter service performed: ")
    maintenance_logs.append({"vehicle": vehicle, "service": service})
    print("Maintenance record added")

def view_logs():
    if not maintenance_logs:
        print("No maintenance records available")
    else:
        for log in maintenance_logs:
            print("Vehicle:", log["vehicle"], "| Service:", log["service"])

def main():
    while True:
        print("1. Add Maintenance Log")
        print("2. View Logs")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_log()
        elif choice == "2":
            view_logs()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
