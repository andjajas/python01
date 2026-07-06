#!/usr/bin/env python3
class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        growth_rate: float = 0.8
         ):
        self._name = name
        self._height = height
        self._plant_age = plant_age
        self._growth_rate = growth_rate

    def grow(self) -> float:
        self.height += self.growth_rate
        return self.height

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

    def show(self) -> None:
        print(
            f"Plant created: {self._name.capitalize()}: "
            f"{self.get_height():0.1f}cm, "
            f"{self.get_age()} days old"
        )

    def show_state(self) -> None:
        print(
            f"\nCurrent state: {self._name.capitalize()}: "
            f"{self.get_height():0.1f}cm, "
            f"{self.get_age()} days old"
        )

    # def show_state(self) -> None:
    #     print(
    #         f"\nCurrent state: {self._name}: {self._height:0.1f}cm, "
    #         f"{self._plant_age} days old"
    #     )


def ft_garden_security() -> None:
    rose = Plant("rose", 15, 10)
    print("=== Garden Security System ===")
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-10)
    rose.set_age(-10)
    rose.show_state()


if __name__ == "__main__":
    ft_garden_security()
