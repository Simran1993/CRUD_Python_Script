


class VehicleRecord:
    """
    Author: Harsimranjit Singh
    A class to represent a fuel consumption record.

    Attributes:
    ----------
    model_year : str
        The model year of the vehicle.
    make : str
        The make of the vehicle.
    model : str
        The model of the vehicle.
    vehicle_class : str
        The vehicle class of the record.
    engine_size : str
        The engine size of the vehicle in liters.
    cylinders : str
        The number of cylinders in the vehicle.
    transmission : str
        The type of transmission of the vehicle.
    fuel_type : str
        The fuel type of the vehicle.
    city_L_100km : str
        The fuel consumption in city driving (L/100 km).
    highway_L_100km : str
        The fuel consumption in highway driving (L/100 km).
    smog_rating : str
        The smog rating of the vehicle.

    Methods:
    -------
    __str__():
        Returns a string representation of the fuel consumption record.
    """

    def __init__(self, model_year, make, model, vehicle_class, engine_size, cylinders, transmission, fuel_type):
        """
        Author: Harsimranjit Singh
        Initializes TrafficRecord with provided details.

        Parameters:
        ----------
        model_year : str
            The model year of the vehicle.
        make : str
            The make of the vehicle.
        model : str
            The model of the vehicle.
        vehicle_class : str
            The vehicle class of the record.
        engine_size : str
            The engine size of the vehicle in liters.
        cylinders : str
            The number of cylinders in the vehicle.
        transmission : str
            The type of transmission of the vehicle.
        fuel_type : str
            The fuel type of the vehicle.
        city_L_100km : str, optional
            The fuel consumption in city driving (L/100 km).
        highway_L_100km : str, optional
            The fuel consumption in highway driving (L/100 km).
        smog_rating : str, optional
            The smog rating of the vehicle.
        """
        self.model_year = model_year
        self.make = make
        self.model = model
        self.vehicle_class = vehicle_class
        self.engine_size = engine_size
        self.cylinders = cylinders
        self.transmission = transmission
        self.fuel_type = fuel_type

    def __str__(self):
        """
        Author: Harsimranjit Singh
        Returns a string representation of the fuel consumption record.

        Returns:
        -------
        str
            A string representation of the fuel consumption record.
        """
        return f"Model Year: {self.model_year}, Make: {self.make}, Model: {self.model}, Vehicle Class: {self.vehicle_class}, Engine Size (L): {self.engine_size}, Cylinders: {self.cylinders}, Transmission: {self.transmission}, Fuel Type: {self.fuel_type}"