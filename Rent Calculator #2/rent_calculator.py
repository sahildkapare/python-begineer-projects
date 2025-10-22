while True:
    print("\n---Rent Calculator---")

    rent=int(input("Enter your hostel/flat rent="))
    food=int(input("Enter the amount of food ordered="))
    electricity_spent=int(input("Enter the total electricity units spent="))
    charge_per_unit=int(input("Enter the charge per unit="))
    persons=int(input("Enter the number of persons living in room/flat="))

    total_bill=electricity_spent*charge_per_unit
    output=(rent+food+total_bill)/persons
    print("\n Each person will pay=₹",round(output,2))

    choice=input("\n Do you want to calculate again?(yes/no):").strip().lower()
    if choice.startswith("y"):
        continue
    else:
        print("\n Thank you for using the Rent Calculator! Goodbye 👋")
        break
