# test_business_layer.py
"""
Unit tests for TrafficManager.

Author: Harsimranjit Singh
"""

import unittest
from Business_Layer.business_layer import VehicleManeger
from Model_Layer.VehicleRecord import VehicleRecord  # Adjusted to VehicleRecord

class TestTrafficManager(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment by initializing a TrafficManager
        with a small set of test data.
        """
        self.manager = VehicleManeger('C:\Term4\Research Assignmnet\Project Assignment 2\PROJECT_ASSIGNMENT_2_HARSIMRANJIT_SINGH\Presentation_Layer\Unit_Testing\my2024-fuel-consumption-ratings.csv')
        self.manager.records = [
            VehicleRecord("2021", "Toyota", "Corolla", "Compact", "1.8", "4", "Automatic", "Gasoline"),
            VehicleRecord("2022", "Honda", "Civic", "Sedan", "2.0", "4", "Manual", "Diesel")
        ]

    def test_add_record(self):
        """
        Test if the program adds a new record into the sequential data structure.
        """
        new_record = VehicleRecord("2023", "Ford", "Fusion", "Sedan", "2.5", "6", "Automatic", "Gasoline")
        self.manager.add_record(new_record)
        
        self.assertEqual(len(self.manager.records), 3)
        self.assertEqual(self.manager.get_record(2).model_year, "2023")
        self.assertEqual(self.manager.get_record(2).make, "Ford")
        self.assertEqual(self.manager.get_record(2).model, "Fusion")
        self.assertEqual(self.manager.get_record(2).vehicle_class, "Sedan")
        self.assertEqual(self.manager.get_record(2).engine_size, "2.5")
        self.assertEqual(self.manager.get_record(2).cylinders, "6")
        self.assertEqual(self.manager.get_record(2).transmission, "Automatic")
        self.assertEqual(self.manager.get_record(2).fuel_type, "Gasoline")

    def test_update_record(self):
        """
        Test if the program updates a record in the sequential data structure as expected.
        """
        updated_record = VehicleRecord("2021", "Toyota", "Corolla", "Compact", "2.0", "4", "Automatic", "Gasoline")
        self.manager.update_record(0, updated_record)
        record = self.manager.get_record(0)

        self.assertEqual(record.model_year, "2021")
        self.assertEqual(record.make, "Toyota")
        self.assertEqual(record.model, "Corolla")
        self.assertEqual(record.vehicle_class, "Compact")
        self.assertEqual(record.engine_size, "2.0")
        self.assertEqual(record.cylinders, "4")
        self.assertEqual(record.transmission, "Automatic")
        self.assertEqual(record.fuel_type, "Gasoline")


if __name__ == '__main__':
    unittest.main()
