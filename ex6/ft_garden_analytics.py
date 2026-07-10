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
#            print(f"Height updated: {self._height}cm")

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
#            print(f"Age updated: {self._plant_age} days")

    def get_age(self) -> int:
        return self._plant_age

    def age(self) -> int:
        new_age = self.get_age() + 1
        self.set_age(new_age)
        return self.get_age()

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.get_height():0.1f}cm, "
            f"{self.get_age()} days old"
        )

    def show_state(self) -> None:
        print(
            f"\nCurrent state: {self.name.capitalize()}: "
            f"{self.get_height():0.1f}cm, "
            f"{self.get_age()} days old"
        )

	@staticmethod
    def older_than_year(age):
        return age > 365


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

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")

    def bloom(self, bloomed: bool) -> None:
        if not bloomed:
            self.show()
            print(f" {self.name.capitalize()} has not bloomed yet")
        else:
            print(f"[asking the {self.name} to bloom]")
            self.show()
            print(f" {self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        trunk_diameter: float
         ):
        super().__init__(name, height, plant_age)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:0.1f}cm")

    def produce_shade(self, shade: bool) -> None:
        if shade:
            self.show()
            print(f"[asking the {self.name} to produce shade]")
            print(
                f"Tree {self.name.capitalize()} now produces a shade of "
                f"{self.get_height():0.1f}cm long and "
                f"{self._trunk_diameter:0.1f}cm wide."
            )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        harvest_season: str,
        nutritional_value: int
         ):
        super().__init__(name, height, plant_age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season.capitalize()}")
        print(f" Nutritional value: {self._nutritional_value}")

    def age(self) -> int:
        super().age()
        self._nutritional_value += 1
        return self.get_age()

    def grow_and_age(self, days: int, growth_rate: float) -> None:
        print(f"[make {self.name} grow and age for {days} days]")
        for _ in range(days):
            self.grow(growth_rate)
            self.age()


def ft_garden_analytics() -> None:


if __name__ == "__main__":
	ft_garden_analytics()
