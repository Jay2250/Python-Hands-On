#Smart Home Device management
from abc import ABC, abstractmethod


class SmartDevice(ABC):
    _name = ""
    _status = ""
    @abstractmethod
    def turn_on(self):
        pass
    def turn_off(self):
        pass
    def device_info(self):
        pass
class SmartLight(SmartDevice):
    def __init__(self,name):
        self._name=name
    def turn_on(device:SmartDevice):
        device._status = "ON"
        return "Smart light is now ON..."
    def turn_off(device:SmartDevice):
        device._status = "OFF"
        return "Smart Light is now OFF..."
    def device_info(device:SmartDevice):
        return f"The light {device._name} is {device._status}"

light1 = SmartLight("loyyed")
print(SmartLight.turn_on(light1))
print(SmartLight.device_info(light1))
print(SmartLight.turn_off(light1))
print(SmartLight.device_info(light1))


# ------------------------------------------------------------------


class SmartDevice(ABC):
    def __init__(self, name, status="OFF"):
        self._name = name
        self._status = status

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def device_info(self):
        return f"Device Name: {self._name}, Status: {self._status}"

class SmartLight(SmartDevice):
    def turn_on(self):
        self._status = "ON"
        return "Smart light is on"

    def turn_off(self):
        self._status = "OFF"
        return "Smart light is off"

light = SmartLight("Living Room Light")


print(light.device_info())
print(light.turn_on())
print(light.device_info())
print(light.turn_off())
print(light.device_info())

# -------------------------------------------------------------------


class SmartDevice(ABC):
    def __init__(self, name):
        self._name = name
        self._status = 'off'

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def device_info(self):
        return f"Device Name: {self._name}, Status: {self._status}"

class SmartLight(SmartDevice):
    def __init__(self, name, brightness=0):
        super().__init__(name)
        self._brightness = brightness

    def turn_on(self):
        self._status = 'on'
        return f"{self._name} is now on."

    def turn_off(self):
        self._status = 'off'
        return f"{self._name} is now off."


    def set_brightness(self, level):
        if 0 <= level <= 100:
            self._brightness = level
            return f"Brightness set to {level}%."
        else:
            return "Brightness level must be between 0 and 100."


    def device_info(self):
        return f"Device Name: {self._name}, Status: {self._status}, Brightness: {self._brightness}%"

smart_light = SmartLight("Living Room Light")
print(smart_light.device_info())
print(smart_light.turn_on())
print(smart_light.set_brightness(70))
print(smart_light.device_info())
print(smart_light.turn_off())
print(smart_light.device_info())