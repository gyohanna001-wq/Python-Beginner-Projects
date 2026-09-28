from abc import ABC, abstractmethod

# Abstract class - cannot be instantiated directly
class Vehicle(ABC):
    """
    Abstract base class for all vehicles.
    This demonstrates abstraction by defining a common interface
    for all vehicles while hiding implementation details.
    """
    
    def __init__(self, brand, model):
        """Initialize common attributes for all vehicles"""
        self.brand = brand
        self.model = model
        self._is_running = False  # Protected attribute
    
    @abstractmethod
    def start_engine(self):
        """
        Abstract method - must be implemented by all subclasses.
        This is the 'contract' that all vehicles must follow.
        Each vehicle type will start differently, but the interface is the same.
        """
        pass
    
    @abstractmethod
    def stop_engine(self):
        """
        Abstract method - stops the vehicle's engine.
        Every vehicle must implement this.
        """
        pass
    
    def get_info(self):
        """
        Concrete method - shared by all subclasses.
        This shows that abstract classes can have implemented methods too.
        """
        return f"{self.brand} {self.model}"
    
    def get_status(self):
        """Concrete method to check if engine is running"""
        status = "running" if self._is_running else "stopped"
        return f"Engine is {status}"


# Concrete class - implements the abstract methods
class Car(Vehicle):
    """
    Car class implements the Vehicle abstraction.
    It MUST provide implementations for all abstract methods.
    """
    
    def __init__(self, brand, model, doors=4):
        """Initialize car with its specific attributes"""
        super().__init__(brand, model)  # Call parent class init
        self.doors = doors
        self.fuel_level = 100
    
    def start_engine(self):
        """
        Implementation of start_engine for a car.
        The user doesn't need to know how the car's ECU works
        or how the starter motor operates.
        """
        if self.fuel_level <= 0:
            print("⚠️  No fuel! Cannot start engine.")
            return
        
        # Complex car-specific starting logic (hidden from user)
        self._check_battery()
        self._prime_fuel_pump()
        self._engage_starter_motor()
        
        self._is_running = True
        print(f"🚗 {self.brand} {self.model} engine started!")
    
    def stop_engine(self):
        """
        Implementation of stop_engine for a car.
        Hides the complexity of electronic fuel injection cutoff.
        """
        if not self._is_running:
            print("Engine is already stopped.")
            return
        
        # Complex car-specific stopping logic (hidden)
        self._cut_fuel_supply()
        self._stop_ignition()
        
        self._is_running = False
        print(f"🚗 {self.brand} {self.model} engine stopped!")
    
    # Private methods - hidden from the user
    def _check_battery(self):
        """Internal method - user doesn't need to know about this"""
        print("🔋 Battery check: OK")
    
    def _prime_fuel_pump(self):
        """Internal method - part of the hidden complexity"""
        print("⛽ Fuel pump primed")
    
    def _engage_starter_motor(self):
        """Internal method - part of the hidden complexity"""
        print("🔌 Starter motor engaged")
    
    def _cut_fuel_supply(self):
        """Internal method - part of the hidden complexity"""
        print("⛽ Fuel supply cut off")
    
    def _stop_ignition(self):
        """Internal method - part of the hidden complexity"""
        print("🔥 Ignition stopped")
    
    def refuel(self, amount):
        """Car-specific method - adds functionality"""
        self.fuel_level = min(100, self.fuel_level + amount)
        print(f"⛽ Refueled to {self.fuel_level}%")\
        