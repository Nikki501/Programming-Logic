AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

#display the menu options
def display_menu():
    print("_____________________________________")
    print("AutoCountry Vehicle Finder v0.1")
    print("_____________________________________")
    print("Please Enter the following number below from the following menu: ")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")

#print the vechicle list
def print_authorized_vehicles():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

#user input based on menu options
def main():
    while True:
        display_menu()
        entry = input("Please Enter a Number from the Menu: ")

        if entry == "1":
            print_authorized_vehicles()
        elif entry =="2":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break

        else:
            print("Invalid entry. Please enter a number from the menu.")
            
if __name__ == "__main__":
    main()
