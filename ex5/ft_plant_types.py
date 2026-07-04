#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, plant_age: int):
        self._name = name.capitalize()
        self._height = height
        self._plant_age = plant_age
# you can set an attribute to an initial value, like 0 so
# if you call the class you don't need to give the value of the attribute
# as an argument
    def show(self) -> None:
        print(
            f"Plant created: {self._name}: {self._height:0.1f}cm, "
            f"{self._plant_age} days old"
        )

    def grow(self) -> float:
        self._height += 0.8
        return self._height

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print("Error: height can't be negative\nHeight update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")

    def get_height(self) -> float:
        return self._height

    def age(self) -> int:
        self._plant_age += 1
        return self._plant_age

    def set_age(self, new_plant_age: int) -> None:
        if new_plant_age < 0:
            print("Error, age can't be negative\nAge update rejected")
        else:
            self._plant_age = new_plant_age
            print(f"Age updated: {self._plant_age} days")

    def get_age(self) -> int:
        return self._plant_age

    def show_state(self) -> None:
        print(
            f"\nCurrent state: {self._name}: {self.get_height():0.1f}cm, "
            f"{self.get_age()} days old"
        )

class Flower(Plant):
    def __init__(self, name: str, height: float, plant_age: int, color: str):
		super().__init__(name, height, plant_age)
		self._color = color

	def bloom(self) -> None:
		print(f"The {self._color} {self._name} is blooming!")
