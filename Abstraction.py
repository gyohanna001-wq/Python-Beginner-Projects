from abc import ABC, abstractmethod

class PlayStation(ABC):
    def __init__(self, brand):
        self.brand = brand
        self._is_running = False

    @abstractmethod
    def start_console(self):
        pass

    @abstractmethod
    def stop_console(self):
        pass

    def get_info(self):
        return f"{self.brand}"

    def get_status(self):
        status = "running" if self._is_running else "stopped"
        return f"Console is {status}"


class PlayStation4(PlayStation):
    def __init__(self, brand):
        super().__init__(brand)
        self.battery = 100

    def start_console(self):
        if self.battery <= 0:
            print("⚠️ No battery! Cannot start the console.")
            return

        self._check_battery()
        self._prime_battery_pump()
        self._engage_starter_button()

        self._is_running = True
        print(f"🎮 {self.brand} has been started!")

    def stop_console(self):
        if not self._is_running:
            print("⚠️ Warning: Console is already stopped.")
            return

        self._cut_battery_supply()
        self._stop_ignition()

        self._is_running = False
        print(f"🛑 {self.brand} console stopped!")


    def _check_battery(self):
        print("🔋 Checking: OK")

    def _prime_battery_pump(self):
        print("⛽ Battery pump primed.")

    def _engage_starter_button(self):
        print("🔌Starter button engaged.")

    def _cut_battery_supply(self):
        print("🔋 Battery supply cut off.")

    def _stop_ignition(self):
        print("🛑 Ignition stopped.")

    def refuel(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"🔋 Battery refueled to {self.battery}%.")




