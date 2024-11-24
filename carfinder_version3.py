# Initial dataset
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

# File to store vehicle data
file_name = "cars3.txt"

# Load vehicles from the file
def load_vehicles_from_file():
    try:
        with open(file_name, 'r') as file:
            for line in file:
                vehicle = line.strip()
                if vehicle and vehicle not in AllowedVehiclesList:
                    AllowedVehiclesList.append(vehicle)
    except FileNotFoundError:
        # If the file doesn't exist, it will be created when adding new vehicles
        pass

# Append a new vehicle to the file and the list
def add_vehicle():
    vehicle_name = input("Please Enter the full Vehicle name you would like to add: ").strip()
    if vehicle_name in AllowedVehiclesList:
        print(f'"{vehicle_name}" is already an authorized vehicle.')
    else:
        AllowedVehiclesList.append(vehicle_name)
        with open(file_name, 'a') as file:
            file.write(vehicle_name + '\n')
        print(f'You have added "{vehicle_name}" as an authorized vehicle.')

# Display the menu options
def display_menu():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.3")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. Exit")
    print("********************************")

# Print the vehicle list
def print_authorized_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

# Search for an authorized vehicle
def search_vehicle():
    search_query = input("Please Enter the Full Vehicle Name: ").strip()
    if search_query in AllowedVehiclesList:
        print(f'\n"{search_query}" is an authorized vehicle.')
    else:
        print(f'\n"{search_query}" is NOT an authorized vehicle. Please check the spelling and try again.')

# Main program logic
def main():
    # Load vehicles from the file when the program starts
    load_vehicles_from_file()
    
    while True:
        display_menu()
        entry = input("Please Enter a Number from the Menu: ").strip()

        if entry == "1":
            print_authorized_vehicles()
        elif entry == "2":
            search_vehicle()
        elif entry == "3":
            add_vehicle()
        elif entry == "4":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid entry. Please enter a number from the menu.")

if __name__ == "__main__":
    main()
