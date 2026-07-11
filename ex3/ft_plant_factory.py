#!/usr/bin/env python3
class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        growth_rate: float = 0.8,
         ) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(
            f"Created: {self.name}: {self.height:0.1f}cm, "
            f"{self.plant_age} days old"
        )

    def grow(self) -> float:
        self.height += self.growth_rate
        return self.height

    def age(self) -> int:
        self.plant_age += 1
        return self.plant_age


def ft_plant_factory() -> None:
    rose = Plant("rose".capitalize(), 25, 30)
    oak = Plant("oak".capitalize(), 200, 365)
    cactus = Plant("cactus".capitalize(), 5, 90)
    sunflower = Plant("sunflower".capitalize(), 80, 45)
    fern = Plant("fern".capitalize(), 15, 120)
    print("=== Plant Factory Output ===")
    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()


if __name__ == "__main__":
    ft_plant_factory()
