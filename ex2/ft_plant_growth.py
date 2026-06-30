class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height:0.1f}cm, {self.age} days old")


ft_garden_growth()


if __name__ == "__main__":
    ft_garden_growth()