
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

#vehicle data
file_name = "cars.txt"


def load_vehicles_from_file():
    try:
        with open(file_name, 'r') as file:
            for line in file:
                vehicle = line.strip()
                if vehicle and vehicle not in AllowedVehiclesList:
                    AllowedVehiclesList.append(vehicle)
    except FileNotFoundError:
        pass


def save_vehicles_to_file():
    with open(file_name, 'w') as file:
        for vehicle in AllowedVehiclesList:
            file.write(vehicle + '\n')

def add_vehicle():
    vehicle_name = input("Please Enter the full Vehicle name you would like to add: ").strip()
    if vehicle_name in AllowedVehiclesList:
        print(f'"{vehicle_name}" is already an authorized vehicle.')
    else:
        AllowedVehiclesList.append(vehicle_name)
        save_vehicles_to_file()
        print(f'You have added "{vehicle_name}" as an authorized vehicle.')


def remove_vehicle():
    vehicle_name = input("Please Enter the full Vehicle name you would like to REMOVE: ").strip()
    if vehicle_name in AllowedVehiclesList:
        confirmation = input(f'Are you sure you want to remove "{vehicle_name}" from the Authorized Vehicles List? (yes/no): ').strip().lower()
        if confirmation == 'yes':
            AllowedVehiclesList.remove(vehicle_name)
            save_vehicles_to_file()
            print(f'You have REMOVED "{vehicle_name}" as an authorized vehicle.')
        else:
            print(f'"{vehicle_name}" was not removed.')
    else:
        print(f'"{vehicle_name}" is NOT an authorized vehicle.')


def display_menu():
    print("\n___________________________")
    print("AutoCountry Vehicle Finder v0.4")
    print("_______________________________")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")


def print_authorized_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)


def search_vehicle():
    search_query = input("Please Enter the Full Vehicle Name: ").strip()
    if search_query in AllowedVehiclesList:
        print(f'\n"{search_query}" is an authorized vehicle.')
    else:
        print(f'\n"{search_query}" is NOT an authorized vehicle. Please check the spelling and try again.')


def main():
 
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
            remove_vehicle()
        elif entry == "5":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid entry. Please enter a number from the menu.")

if __name__ == "__main__":
    main()
