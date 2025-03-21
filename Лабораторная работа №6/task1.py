import doctest

class Car:
    """
    Базовый класс для автомобилей.
    """
    
    def __init__(self, brand: str, max_speed: float) -> None:
        """
        Инициализация автомобиля.
        :param brand: Бренд автомобиля
        :param max_speed: Максимальная скорость автомобиля в км/ч
        """
        self._brand = brand  # Инкапсуляция, т.к. бренд не должен изменяться напрямую
        self.max_speed = max_speed
        self.current_speed = 0

    def __str__(self) -> str:
        """
        Человеко-читаемое представление автомобиля.
        """
        return f"Автомобиль {self._brand}, максимальная скорость {self.max_speed} км/ч"

    def __repr__(self) -> str:
        """
        Формальное представление объекта автомобиля.
        """
        return f"Car(brand='{self._brand}', max_speed={self.max_speed})"

    def accelerate(self, increase: float) -> str:
        """
        Увеличить скорость автомобиля.
        :param increase: Величина увеличения скорости в км/ч
        """
        self.current_speed = min(self.current_speed + increase, self.max_speed)
        return f"Автомобиль разогнался до {self.current_speed} км/ч."

    def brake(self, decrease: float) -> str:
        """
        Уменьшить скорость автомобиля.
        :param decrease: Величина уменьшения скорости в км/ч
        """
        self.current_speed = max(self.current_speed - decrease, 0)
        return f"Автомобиль замедлился до {self.current_speed} км/ч."

class ElectricCar(Car):
    """
    Электромобиль, наследуется от базового класса Car.
    """
    
    def __init__(self, brand: str, max_speed: float, battery_capacity: int) -> None:
        """
        Инициализация электромобиля.
        :param brand: Бренд электромобиля
        :param max_speed: Максимальная скорость в км/ч
        :param battery_capacity: Ёмкость батареи в кВт⋅ч
        """
        super().__init__(brand, max_speed)
        self.battery_capacity = battery_capacity
        self.battery_level = 100

    def __str__(self) -> str:
        """
        Перегрузка метода __str__, добавляя информацию о батарее.
        """
        return f"Электромобиль {self._brand}, батарея {self.battery_capacity} кВт⋅ч, макс. скорость {self.max_speed} км/ч"

    def charge(self, amount: int) -> str:
        """
        Зарядить электромобиль.
        :param amount: Величина заряда в процентах
        """
        self.battery_level = min(self.battery_level + amount, 100)
        return f"Батарея заряжена до {self.battery_level}%"

class SportsCar(Car):
    """
    Спортивный автомобиль, наследуется от базового класса Car.
    """
    
    def __init__(self, brand: str, max_speed: float, acceleration: float) -> None:
        """
        Инициализация спортивного автомобиля.
        :param brand: Бренд автомобиля
        :param max_speed: Максимальная скорость в км/ч
        :param acceleration: Время разгона 0-100 км/ч в секундах
        """
        super().__init__(brand, max_speed)
        self.acceleration = acceleration

    def __str__(self) -> str:
        """
        Перегрузка метода __str__, добавляя информацию о разгоне.
        """
        return f"Спортивный автомобиль {self._brand}, разгон 0-100 км/ч за {self.acceleration} сек, макс. скорость {self.max_speed} км/ч"

if __name__ == "__main__":
    # Пример использования
    car = ElectricCar("Tesla", 250, 100)
    sports_car = SportsCar("Ferrari", 340, 2.9)
    
    print(car)
    print(sports_car)
    print(car.charge(20))
    print(sports_car.accelerate(50))