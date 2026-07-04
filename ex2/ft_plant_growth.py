#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, plant_age: int):
        self.name = name.capitalize()
        self.height = height
        self.plant_age = plant_age

    def show(self) -> None:
        print(f"{self.name}: {self.height:0.1f}cm, {self.plant_age} days old")

    def grow(self) -> float:
        self.height += 0.8
        return self.height
# better to not hardcode the growth rate with 0.8 to prepare for different
# plant types
    def age(self) -> int:
        self.plant_age += 1
        return self.plant_age


def ft_plant_growth() -> None:
    rose = Plant("rose", 25, 30)
    print("=== Garden Plant Growth ===")
    rose.show()
    start_height = rose.height
    for day in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {day} ===")
        rose.show()
    week_growth = rose.height - start_height
    print(f"Growth this week: {week_growth:0.1f}")


if __name__ == "__main__":
    ft_plant_growth()
