#Clinical Data Audit System

patientname = input("Enter patient name: ")
age = input("Enter patient age: ")

flags = []
warning = []
readings = []

#  AGE VALIDATION 
def validate():
    if not age.isdigit():
        flags.append("Invalid age")
        return

    age_val = int(age)
    if age_val < 0 or age_val > 120:
        flags.append("Invalid age")
        return


#  RECURSION FOR HEART RATE READINGS 
def reading(n):
    if n == 0:
        return

    heartrate = input("Enter heart rate reading: ")

    if not heartrate.isdigit():
        flags.append("Invalid heart rate")
        return

    heartrate = int(heartrate)

    if heartrate > 180:
        warning.append("High heart rate detected")

    readings.append(heartrate)

    reading(n - 1)


#  FUNCTION CALLS 
validate()

num = int(input("Enter number of heart rate readings: "))
reading(num)


# FINAL AUDIT STATUS 
print("\n--- CLINICAL AUDIT RESULT ---")
print("Patient :", patientname.title())

if flags:
    status = "FAIL"
elif warning:
    status = "REVIEW"
else:
    status = "PASS"

print("Status :", status)
print("Flags :", flags if flags else "None")
print("Warnings :", warning if warning else "None")
