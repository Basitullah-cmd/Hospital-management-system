import os

def show_menu():
    print("\n=========================================================")
    print("|------------   Hospital Management System   -----------|")
    print("|                                                       |")
    print("|                  1. Doctor Portal                     |")
    print("|                  2. Pharmacy Management               |")
    print("|                  3. Billing System                    |")
    print("|                  4. Exit                              |")
    print("|                                                       |")
    print("=========================================================")
    return int(input("\nEnter your choice: "))

def doctor_portal():
    while True:
        print("\n===========================================================")
        print("|---------------------  Doctor Portal  -------------------|")
        print("|                                                         |")
        print("|                  1. Add Patient                         |")
        print("|                  2. View Patients                       |")
        print("|                  3. Write Prescription                  |")
        print("|                  4. Back to Main Menu                   |")
        print("|                                                         |")
        print("===========================================================")
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            add_patient()
        elif choice == 2:
            view_patients()
        elif choice == 3:
            write_prescription()
        elif choice == 4:
            break
        else:
            print("Invalid choice, please try again.")

def add_patient():
    patient_id = input("Enter Patient ID: ")
    patient_name = input("Enter Patient Name: ")
    history = input("Enter Medical History: ")

    with open("patients.txt", "a") as file:
        file.write(f"=================================\n")
        file.write(f"Patient ID      : {patient_id}\n")
        file.write(f"Name            : {patient_name}\n")
        file.write(f"Medical History : {history}\n")
        file.write(f"=================================\n")
    print("New patient added.")

def view_patients():
    if not os.path.exists("patients.txt"):
        print("No patients found in the system.")
        return

    with open("patients.txt", "r") as file:
        print("\n\t\t----- List of Patients -----\n")
        print(file.read())

def write_prescription():
    patient_id = input("Enter Patient ID: ")
    medicine_name = input("Enter Medicine Name: ")
    quantity = input("Enter Quantity: ")

    filename = f"{patient_id}_prescription.txt"
    with open(filename, "a") as file:
        file.write(f"=================================\n")
        file.write(f"Prescription for Patient ID: {patient_id}\n")
        file.write(f"---------------------------------\n")
        file.write(f"Medicine Name: {medicine_name}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"=================================\n")
    print(f"Prescription saved for Patient ID: {patient_id}")

def pharmacy_management():
    while True:
        print("\n==========================================================")
        print("|-----------------  Pharmacy Management  ----------------|")
        print("|                                                        |")
        print("|                  1. Add Medicine                       |")
        print("|                  2. View Stock                         |")
        print("|                  3. Back to Main Menu                  |")
        print("|                                                        |")
        print("==========================================================")
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            add_medicine()
        elif choice == 2:
            view_stock()
        elif choice == 3:
            break
        else:
            print("Invalid choice, please try again.")

def add_medicine():
    name = input("Enter Medicine Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price/unit: "))

    with open("medicines.txt", "a") as file:
        file.write(f"=================================\n")
        file.write(f"Medicine Name : {name}\n")
        file.write(f"Quantity      : {quantity}\n")
        file.write(f"Price         : Rs. {price:.2f}\n")
        file.write(f"=================================\n")
    print("Medicine added successfully.")

def view_stock():
    if not os.path.exists("medicines.txt"):
        print("No medicines found in the system.")
        return

    with open("medicines.txt", "r") as file:
        print("\n\t\t----- Medicine Stock -----\n")
        print(file.read())

def generate_bill():
    patient_id = input("Enter Patient ID for billing: ")
    calculate_total_bill(patient_id)

def calculate_total_bill(patient_id):
    if not os.path.exists("patients.txt"):
        print("Error: patients.txt not found.")
        return

    with open("patients.txt", "r") as file:
        patients = file.read()
        if patient_id not in patients:
            print("Error: Patient ID not found.")
            return

    room_charges = 1000
    test_charges = 200
    treatment_charges = 300
    medicine_charges = 150
    total_charges = room_charges + test_charges + treatment_charges + medicine_charges

    print("\n================================")
    print(f"Bill for Patient ID: {patient_id}")
    print("---------------------------------")
    print(f"Room Charges       : Rs. {room_charges:.2f}")
    print(f"Test Charges       : Rs. {test_charges:.2f}")
    print(f"Treatment Charges  : Rs. {treatment_charges:.2f}")
    print(f"Medicine Charges   : Rs. {medicine_charges:.2f}")
    print("---------------------------------")
    print(f"Total Charges      : Rs. {total_charges:.2f}")
    print("=================================")

def main():
    while True:
        choice = show_menu()

        if choice == 1:
            doctor_portal()
        elif choice == 2:
            pharmacy_management()
        elif choice == 3:
            generate_bill()
        elif choice == 4:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "_main_":
    main()