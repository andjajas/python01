#!/usr/bin/env python3
class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
         ):
        self.name = name
        self._height = height
        self._plant_age = plant_age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print("Error: height can't be negative\nHeight update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")

    def get_height(self) -> float:
        return self._height

    def grow(self, growth_rate: float = 0.8) -> float:
        new_height = self.get_height() + growth_rate
        self.set_height(new_height)
        return self.get_height()

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print("Error, age can't be negative\nAge update rejected")
        else:
            self._plant_age = new_age
            print(f"Age updated: {self._plant_age} days")

    def get_age(self) -> int:
        return self._plant_age

    def age(self) -> int:
        new_age = self.get_age() + 1
        self.set_age(new_age)
        return self.get_age()

    def show(self) -> None:
        print(
            f"Plant created: {self.name.capitalize()}: "
            f"{self.get_height():0.1f}cm, "
            f"{self.get_age()} days old"
        )

    def show_state(self) -> None:
        print(
            f"\nCurrent state: {self.name.capitalize()}: "
            f"{self.get_height():0.1f}cm, "
            f"{self.get_age()} days old"
        )


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        color: str
         ):
        super().__init__(name, height, plant_age)
        self._color = color

    def bloom(self) -> None:
        print(f"The {self._color} {self._name} is blooming!")
