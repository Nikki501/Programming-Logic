
file_name = "cars.txt"

def load_vehicles_from_file():
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

# Save the list of vehicles back to the file
def save_vehicles_to_file(vehicle_list):
    with open(file_name, 'w') as file:
        for vehicle in vehicle_list:
            file.write(vehicle + '\n')

def display_menu():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.5")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")


def print_authorized_vehicles():
    vehicles = load_vehicles_from_file()
    if vehicles:
        print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for vehicle in vehicles:
            print(vehicle)
    else:
        print("\nNo authorized vehicles are currently listed.")


def search_vehicle():
    search_query = input("Please Enter the Full Vehicle Name: ").strip()
    vehicles = load_vehicles_from_file()
    if search_query in vehicles:
        print(f'\n"{search_query}" is an authorized vehicle.')
    else:
        print(f'\n"{search_query}" is NOT an authorized vehicle. Please check the spelling and try again.')


def add_vehicle():
    vehicle_name = input("Please Enter the full Vehicle name you would like to add: ").strip()
    vehicles = load_vehicles_from_file()
    if vehicle_name in vehicles:
        print(f'"{vehicle_name}" is already an authorized vehicle.')
    else:
        with open(file_name, 'a') as file:
            file.write(vehicle_name + '\n')
        print(f'You have added "{vehicle_name}" as an authorized vehicle.')

def remove_vehicle():
    vehicle_name = input("Please Enter the full Vehicle name you would like to REMOVE: ").strip()
    vehicles = load_vehicles_from_file()
    if vehicle_name in vehicles:
        confirmation = input(f'Are you sure you want to remove "{vehicle_name}" from the Authorized Vehicles List? (yes/no): ').strip().lower()
        if confirmation == 'yes':
            vehicles.remove(vehicle_name)
            save_vehicles_to_file(vehicles)
            print(f'You have REMOVED "{vehicle_name}" as an authorized vehicle.')
        else:
            print(f'"{vehicle_name}" was not removed.')
    else:
        print(f'"{vehicle_name}" is NOT an authorized vehicle.')


def main():
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
