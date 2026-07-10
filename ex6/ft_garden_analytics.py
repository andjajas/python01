#!/usr/bin/env python3
class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0

        def add_to_grow_count(self) -> None:
            self._grow_count += 1

        def add_to_age_count(self) -> None:
            self._age_count += 1

        def add_to_show_count(self) -> None:
            self._show_count += 1
        
        def show_stats(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, "
                f"{self._show_count} show"
            )

    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
         ) -> None:
        self.name = name
        self._height = height
        self._plant_age = plant_age
        self._stats = Plant.Stats()

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print("Error: height can't be negative\nHeight update rejected")
        else:
            self._height = new_height

    def get_height(self) -> float:
        return self._height

    def grow(self, growth_rate: float = 0.8) -> float:
        new_height = self.get_height() + growth_rate
        self.set_height(new_height)
        self._stats.add_to_grow_count()
        return self.get_height()

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print("Error, age can't be negative\nAge update rejected")
        else:
            self._plant_age = new_age

    def get_age(self) -> int:
        return self._plant_age

    def age(self) -> int:
        new_age = self.get_age() + 1
        self.set_age(new_age)
        self._stats.add_to_age_count()
        return self.get_age()

    def show(self) -> None:
        self._stats.add_to_show_count()
        print(
            f"{self.name.capitalize()}: "
            f"{self.get_height():0.1f}cm, "
            f"{self.get_age()} days old"
        )


    @staticmethod
    def older_than_year(age: int) -> bool:
        return age > 365

    def create_plant(cls) -> "Plant":
        return cls("Unknown plant", float(0), 0)
    create_plant = classmethod(create_plant)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        color: str
         ) -> None:
        super().__init__(name, height, plant_age)
        self.color = color
        self.is_bloomed: bool = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if not self.is_bloomed:
            print(f" {self.name.capitalize()} has not bloomed yet")
        else:
            print(f" {self.name.capitalize()} is blooming beautifully!")

    def bloom(self) -> None:
        if not self.is_bloomed:
            self.is_bloomed = True
            print(f"[asking the {self.name} to grow and bloom]")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        color: str
         ) -> None:
        super().__init__(name, height, plant_age, color)
        self.count: int = 0

    def show(self) -> None:
        super().show()
        if not self.is_bloomed:
            print(f" Seeds: {self.count}")
        else:
            self.count += 42
            print(f" Seeds: {self.count}")


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count: int = 0

        def add_to_shade_count(self) -> None:
            self._shade_count += 1

        def show_stats(self) -> None:
            super().show_stats()
            print(f" {self._shade_count} shade")

    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        trunk_diameter: float
         ) -> None:
        super().__init__(name, height, plant_age)
        self.trunk_diameter = trunk_diameter
        self._stats = Tree.TreeStats()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:0.1f}cm")

    def produce_shade(self, shade: bool) -> None:
        if shade:
            self._stats.add_to_shade_count()
            print(f"[asking the {self.name} to produce shade]")
            print(
                f"Tree {self.name.capitalize()} now produces a shade of "
                f"{self.get_height():0.1f}cm long and "
                f"{self.trunk_diameter:0.1f}cm wide."
            )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        harvest_season: str,
        nutritional_value: int
         ) -> None:
        super().__init__(name, height, plant_age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {self.nutritional_value}")

    def age(self) -> int:
        super().age()
        self.nutritional_value += 1
        return self.get_age()

    def grow_and_age(self, days: int, growth_rate: float) -> None:
        print(f"[make {self.name} grow and age for {days} days]")
        for _ in range(days):
            self.grow(growth_rate)
            self.age()


def ft_garden_analytics() -> None:
    print("=== Tree")
    oak = Tree("oak", 200, 365, 5)
    oak.show()
    oak._stats.show_stats()
    oak.produce_shade(True)
    oak._stats.show_stats()
    print("=== Anonymous")
    anonymous = Plant.create_plant()
    anonymous.show()


if __name__ == "__main__":
    ft_garden_analytics()
