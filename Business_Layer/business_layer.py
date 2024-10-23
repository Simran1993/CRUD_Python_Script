
from Persistence_Layer.persistence_layer import load_csv, save_csv

class VehicleManeger:

    def __init__(self, file_path):
        """
        Author: Harsimranjit Singh
        Initializes TrafficManager with a file path and loads data.

        Parameters:
        ----------
        file_path : str
            The path to the CSV file.
        """
        self.file_path = file_path
        self.records = load_csv(file_path)[:100]

    def reload_data(self):
        """
        Reloads data from the CSV file.
        """
        self.records = load_csv(self.file_path)[:100]

    def save_data(self, new_file_path):
        """
        Author: Harsimranjit Singh
        Saves data to a new CSV file.

        Parameters:
        ----------
        new_file_path : str
            The path to the new CSV file.
        """
        save_csv(new_file_path, self.records)

    def get_records(self):
        """
        Returns all records.

        Returns:
        -------
        list
            A list of all traffic records.
        """
        return self.records
    
    def get_record(self, index):
        """
        Author: Harsimranjit Singh
        Returns a specific record by index.

        Parameters:
        ----------
        index : int
            The index of the record.

        Returns:
        -------
        dict or None
            The traffic record if index is valid, otherwise None.
        """
        if 0 <= index < len(self.records):
            return self.records[index]
        else:
            return None
        
    def add_record(self, record):
        """
        Author: Harsimranjit Singh
        Adds a new record.

        Parameters:
        ----------
        record : dict
            The traffic record to be added.
        """
        self.records.append(record)

    def update_record(self, index, updated_record):
        """
        Updates an existing record.

        Parameters:
        ----------
        index : int
            The index of the record to be updated.
        updated_record : dict
            The updated traffic record.
        """
        if 0 <= index < len(self.records):
            self.records[index] = updated_record

    def delete_record(self, index):
        """
        Author: Harsimranjit Singh
        Deletes a record by index.

        Parameters:
        ----------
        index : int
            The index of the record to be deleted.
        """
        if 0 <= index < len(self.records):
            self.records.pop(index)