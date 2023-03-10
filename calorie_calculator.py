from find_temperature import Temperature


class CalorieCalculator:


    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature


    def calculate_calories(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return result


if __name__ == "__main__":
    temperature = Temperature(country="italy", city="rome").get()
    calorie = CalorieCalculator(temperature=temperature, weight=70, height=175, age=32)
    print(calorie.calculate_calories())


