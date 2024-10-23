
"""
Presentation Layer module.

This module provides the user interface for interacting with the fuel consumption record management system.

Author: Harsimranjit Singh
Student Number: 041100738
"""

from Business_Layer.business_layer import VehicleManeger
from Model_Layer.VehicleRecord import VehicleRecord


def display_records(records):
    """
    Author: Harsimranjit Singh
    Displays a list of fuel consumption records.

    Parameters:
    ----------
    records : list
        A list of TrafficRecord objects to display.
    """
    for index, record in enumerate(records):
        print(f"Index: {index}, Record: {record}")


def display_menu():
    """
    Author: Harsimranjit Singh
    Displays the main menu options to the user.
    """
    print("Author: Harsimranjit Singh")
    print("1. Reload data")
    print("2. Save data")
    print("3. Display all records")
    print("4. Display a single record")
    print("5. Add a new record")
    print("6. Update a record")
    print("7. Delete a record")
    print("8. Exit")


def main():
    """
    The main function of the presentation layer that provides a loop to handle user inputs and interact with the TrafficManager.
    """
    manager = VehicleManeger('Presentation_Layer\my2024-fuel-consumption-ratings.csv')

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            manager.reload_data()
            print("Data reloaded.")
        elif choice == '2':
            new_file_path = input("Enter the new file path: ")
            manager.save_data(new_file_path)
            print("Data saved.")
        elif choice == '3':
            display_records(manager.get_records())
        elif choice == '4':
            index = int(input("Enter the index of the record: "))
            record = manager.get_record(index)
            if record:
                print(record)
            else:
                print("Record not found.")
        elif choice == '5':
            model_year = input("Enter Model Year: ")
            make = input("Enter Make: ")
            model = input("Enter Model: ")
            vehicle_class = input("Enter Vehicle Class: ")
            engine_size = input("Enter Engine Size (L): ")
            cylinders = input("Enter Cylinders: ")
            transmission = input("Enter Transmission: ")
            fuel_type = input("Enter Fuel Type: ")
            
            
            new_record = VehicleRecord(
                model_year=model_year, 
                make=make, 
                model=model, 
                vehicle_class=vehicle_class, 
                engine_size=engine_size,
                cylinders=cylinders,
                transmission=transmission,
                fuel_type=fuel_type
                
            )
            manager.add_record(new_record)
            print("Record added.")
        elif choice == '6':
            index = int(input("Enter the index of the record to update: "))
            model_year = input("Enter new Model Year: ")
            make = input("Enter new Make: ")
            model = input("Enter new Model: ")
            vehicle_class = input("Enter new Vehicle Class: ")
            engine_size = input("Enter new Engine Size (L): ")
            cylinders = input("Enter new Cylinders: ")
            transmission = input("Enter new Transmission: ")
            fuel_type = input("Enter new Fuel Type: ")
            

            updated_record = VehicleRecord(
                model_year=model_year, 
                make=make, 
                model=model, 
                vehicle_class=vehicle_class, 
                engine_size=engine_size,
                cylinders=cylinders,
                transmission=transmission,
                fuel_type=fuel_type
            )
            manager.update_record(index, updated_record)
            print("Record updated.")
        elif choice == '7':
            index = int(input("Enter the index of the record to delete: "))
            manager.delete_record(index)
            print("Record deleted.")
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
