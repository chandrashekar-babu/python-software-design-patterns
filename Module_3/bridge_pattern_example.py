from abc import ABC, abstractmethod

# The Implementation Interface
class Device(ABC):
    @abstractmethod
    def set_power(self, status: bool): pass
    
    @abstractmethod
    def set_volume(self, percent: int): pass

# Concrete Implementation 1
class TV(Device):
    def set_power(self, status): print(f"TV Power: {'ON' if status else 'OFF'}")
    def set_volume(self, percent): print(f"TV Volume: {percent}%")

# Concrete Implementation 2
class Radio(Device):
    def set_power(self, status): print(f"Radio Power: {'ON' if status else 'OFF'}")
    def set_volume(self, percent): print(f"Radio Volume: {percent}% (static hissing...)")

class RemoteControl:
    def __init__(self, device: Device):
        self.device = device  # This is the "Bridge" to the implementation

    def toggle_power(self):
        # High-level logic doesn't care if it's a TV or Radio
        self.device.set_power(True)

# We can extend the abstraction WITHOUT touching the devices
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        print("Advanced Remote: Muting device...")
        self.device.set_volume(0)

if __name__ == "__main__":
    # Create the devices (Implementations)
    my_tv = TV()
    my_radio = Radio()

    # Use a basic remote with the TV
    basic_remote = RemoteControl(my_tv)
    basic_remote.toggle_power()

    # Use an advanced remote with the Radio
    # Note how we didn't have to create a "RadioRemote" class!
    pro_remote = AdvancedRemoteControl(my_radio)
    pro_remote.toggle_power()
    pro_remote.mute()