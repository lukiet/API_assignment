# adding a new patient to the system
def new_patient(patients):
    patients_name = input("Enter name : ")
    age = input("Enter age : ")
    illness = input("Enter illness : ")

    patient = {
        "patients_name": patients_name,
        "age": age,
        "illness": illness,
    }
    patients.append(patient)
    print(f"{patients_name} has been registered succesfully")

# display all patients added to the system


def display_patients(patients):
    if not patients:
        print("No patient is registered")
    else:
        for patient in patients:
            print(f"Name : {patient['patients_name']},Age : {
                  patient['age']},Illness : {patient['illness']}")

# search for a patient by name


def search_patients(patients):
    search_name = input("Enter the patient's name : ")
    name_found = False
    for patient in patients:
        if patient['patients_name'].lower() == search_name.lower():
            print(f"Name : {patient['patients_name']},Age : {
                  patient['age']},Illness : {patient['illness']}")
            name_found = True
            break
    if not name_found:
        print(f"{search_name} is not available")

# remove a patient from the system


def remove_patient(patients):
    remove_name = input("Enter the name to be deleted : ")
    for patient in patients:
        if patient['patients_name'].lower() == remove_name.lower():
            patients.remove(patient)
            print(f"{remove_name} has been deleted")
            return
    print(f"{remove_name} is not available")

# keeping the system running until the user decides to exit


def running():
    patients = []
    while True:
        print("Welcome to HospitaliYetu")
        print("1.Add patient")
        print("2.Display patients")
        print("3.Search patient name")
        print("4.Remove patient name")
        print('5.Exit')

        choice = input("Choose a service : ")

        if choice == "1":
            new_patient(patients)
        elif choice == "2":
            display_patients(patients)
        elif choice == "3":
            search_patients(patients)
        elif choice == "4":
            remove_patient(patients)
        elif choice == "5":
            print("Exiting......")
            break
        else:
            print("Invalid, please choose another number")
