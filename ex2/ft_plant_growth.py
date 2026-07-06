#!/usr/bin/env python3
class Plant:
    name: str = "plant"
    height: float = 0
    plant_age: int = 0
    growth_rate: float = 0

    def show(self) -> None:
        print(f"{self.name}: {self.height:0.1f}cm, {self.plant_age} days old")

    def grow(self) -> float:
        self.height += self.growth_rate
        return self.height

    def age(self) -> int:
        self.plant_age += 1
        return self.plant_age


def ft_plant_growth() -> None:
    rose = Plant()
    rose.name = "rose".capitalize()
    rose.height = 25
    rose.plant_age = 30
    rose.growth_rate = 0.8
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
