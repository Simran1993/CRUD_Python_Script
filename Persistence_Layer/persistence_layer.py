import csv
from Model_Layer.VehicleRecord import VehicleRecord  # Ensure VehicleRecord matches updated structure


def load_csv(file_path, limit=100):
    """
    Author: Harsimranjit
    Loads fuel consumption records from a CSV file.

    Parameters:
    ----------
    file_path : str
        The path to the CSV file.
    limit : int, optional
        The maximum number of records to load (default is 100).

    Returns:
    -------
    list
        A list of TrafficRecord objects.
    """
    records = []
    try:
        with open(file_path, newline='', encoding='ISO-8859-1') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for i, row in enumerate(csvreader):
                if i >= limit:
                    break
                record = VehicleRecord(
                    model_year=row['Model year'],
                    make=row['Make'],
                    model=row['Model'],
                    vehicle_class=row['Vehicle class'],
                    engine_size=row['Engine size (L)'],
                    cylinders=row['Cylinders'],
                    transmission=row['Transmission'],
                    fuel_type=row['Fuel type']
                )
                records.append(record)
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return records


def save_csv(file_path, records):
    """
    Author: Harsimranjit
    Saves fuel consumption records to a CSV file.

    Parameters:
    ----------
    file_path : str
        The path to the CSV file.
    records : list
        A list of VehicleRecord objects to save.
    """
    try:
        with open(file_path, mode='w', newline='', encoding='ISO-8859-1') as csvfile:
            fieldnames = [
                'Model year', 'Make', 'Model', 'Vehicle class', 'Engine size (L)',
                'Cylinders', 'Transmission', 'Fuel type'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for record in records:
                writer.writerow({
                    'Model year': record.model_year,
                    'Make': record.make,
                    'Model': record.model,
                    'Vehicle class': record.vehicle_class,
                    'Engine size (L)': record.engine_size,
                    'Cylinders': record.cylinders,
                    'Transmission': record.transmission,
                    'Fuel type': record.fuel_type,
                    
                })
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")
