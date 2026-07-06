#!/usr/bin/env python3
class Plant:
    name = "plant"
    height = 0
    age = 0

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

# maybe not capitalize it from the start in the class for name
# sometimes in ex5 a lowercase is needed for a plantname
def ft_garden_data() -> None:
    rose = Plant()
    rose.name = "rose".capitalize()
    rose.height = 25
    rose.age = 30
    sunflower = Plant()
    sunflower.name = "sunflower".capitalize()
    sunflower.height = 80
    sunflower.age = 45
    cactus = Plant()
    cactus.name = "cactus".capitalize()
    cactus.height = 15
    cactus.age = 120
    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    ft_garden_data()
