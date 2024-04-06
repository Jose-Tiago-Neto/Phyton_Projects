#import library for working with Date/Time
from datetime import datetime


patients = {
        "P12345": {
            "name": "John Doe",
            "age": 35,
            "gender": "Male",
            "diagnosis": "Hypertension",
            "medications": ["Lisinopril", "Hydrochlorothiazide"],
            "allergies": ["Penicillin"],
            "blood_pressure_checks": [[130, 90],[146, 99],[138, 88],[128, 82]],
            "last_checkup_date": "2022-05-20",
            "next_appointment_date": "2023-11-15"
        },
        "P67890": {
            "name": "Jane Smith",
            "age": 41,
            "gender": "Female",
            "diagnosis": "Diabetes",
            "medications": ["Semaglutide", "Insulin"],
            "blood_pressure_checks": [[119, 79],[122, 77],[120, 81],[118, 85]],
            "allergies": ["Metformin"],
            "last_checkup_date": "2023-04-20",
            "next_appointment_date": "No-Date"
        },
        "P24680": {
            "name": "Robert Johnson",
            "age": 28,
            "gender": "Male",
            "diagnosis": "Asthma",
            "medications": ["Albuterol", "Prednisone"],
            "allergies": ["Peanuts"],
            "blood_pressure_checks": [[121, 80],[122, 78],[125, 80],[119, 83]],
            "last_checkup_date": "2022-06-08",
            "next_appointment_date": "2023-12-10"
        },
        "P18945": {
            "name": "Alice Davis",
            "age": 55,
            "gender": "Female",
            "diagnosis": "Diabetes",
            "medications": ["Metformin", "Insulin"],
            "allergies": ["Penicillin"],
            "blood_pressure_checks": [[122, 81],[122, 78],[123, 78],[119, 81]],
            "last_checkup_date": "2023-04-15",
            "next_appointment_date": "No-Date"
        },
        "P69918": {
            "name": "Michael Smith",
            "age": 42,
            "gender": "Male",
            "diagnosis": ["Hypertension","Celiac Disease"],
            "medications": ["Lisinopril", "Hydrochlorothiazide"],
            "allergies": [],
            "blood_pressure_checks": [[175, 95],[155, 89],[145, 100]],
            "last_checkup_date": "2023-05-20",
            "next_appointment_date": "2023-11-20"
        },
        "P13579": {
            "name": "Emily Johnson",
            "age": 33,
            "gender": "Female",
            "diagnosis": "Migraine",
            "medications": ["Sumatriptan", "Ibuprofen"],
            "allergies": ["Codeine"],
            "blood_pressure_checks": [[100, 72],[103, 76],[110, 69],[115, 68],[103, 76]],
            "last_checkup_date": "2023-01-05",
            "next_appointment_date": "2023-12-05"
        }
    }

while True:
   
    # Ask the user for the patient Id
    patient_id = input("Enter patient ID or 'Exit' to exit: ")
    if patient_id == "Exit":
        break
    else:
    # Getting patient information based on Id
        patient = patients.get(patient_id)

    # Print patient information
        if patient:
            print("Patient ID:", patient_id)
            print("Name:", patient["name"])
            print("Age:", patient["age"])
            print("Gender:", patient["gender"])
            print("Diagnosis:", patient["diagnosis"])
            print("Medications:", patient["medications"])
    
    # count the numbers of medications
            print("Number of medications: ", len(patient["medications"]))
            print("allergies:", patient["allergies"])
    
    # count the numbers of allergies
            print("Number of allergies: ", len(patient["allergies"]))
    
    # getting the systolic inside the list of blood presure checks
            systolic = [i[0] for i in patient["blood_pressure_checks"]]
    # average of systolic sum/len
            average_systolic = round(sum(systolic)/len(systolic),2)
    # getting the diastolic inside the list of blood presure checks
            diastolic = [i[1] for i in patient["blood_pressure_checks"]]
    # average of diastolic sum/len
            average_diastolic = round(sum(diastolic)/len(diastolic),2)
    # level of blood pressure
            if average_systolic > 125 and average_diastolic > 85:
                print("The patient average blood pressure is High:", average_systolic,"/",average_diastolic)
            elif 115 < average_systolic < 125 and 75 < average_diastolic < 85:
                print("The patient average blood pressure is Normal:", average_systolic,"/",average_diastolic)
            else:
                print("The patient average blood pressure is Low:", average_systolic,"/",average_diastolic)
            
    #checking if there is any invalid value (if there is an appontment date)
            if "next_appointment_date" in patient and len(patient["next_appointment_date"]) == 10:
        # Cast string to date/time
                next_appointment_date = datetime.strptime(patient["next_appointment_date"], "%Y-%m-%d")
                checkup_date = datetime.strptime(patient["last_checkup_date"], '%Y-%m-%d')
        # getting the time difference between the last checkup and appointment date 
                time_difference = (next_appointment_date - checkup_date).days 
                print("Time until next appointment:", time_difference,)
            else:
                print("There is no upcoming appointment for this patient.")
        # Ask the doctor for a new medication
            new_medication = input("Type the medication you would like to add for this patient list. ")
        # not adding medication to the list, check if is allergic or if this med is already on the list
            if new_medication == "none":
                print("This medication was not added for this patient.")
            elif new_medication in patient["medications"]:
                print("This medication was already prescripted for this patient.")
                print("This is the patient's medication list: ", patient["medications"])
            elif new_medication in patient["allergies"]:
                 print("The patient is allergic to", new_medication,".")
            else:
                patient["medications"].append(new_medication)
                print("This medication was added to the patient's medication list.")
                print("This is the patient's medication list: ", patient["medications"])
        # Ask the doctor for a medication to be removed
            remove_medication = input("Type the medication you Would like to remove from this list. ")
            if remove_medication == "none":
                exit
            elif remove_medication not in patient["medications"]:
                print("This medication is not in the patient's medication list.")
                print("This is the patient's medication list: ", patient["medications"])
            else:
                patient["medications"].remove(remove_medication)
                print("This medication was removed from the patient's medication list.")
                print("This is the new patient's medication list: ", patient["medications"])
        # 
         